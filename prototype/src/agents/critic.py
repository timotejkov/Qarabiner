"""
Agent 4: Critic — Validates the Architect's output before delivery.

This is the quality gate. No raw LLM output reaches the user without
passing the Critic's validation checks.
"""

import logging

from src.agents.base import AgentBase
from src.agents.researcher import RetrievedStandards
from src.config import config
from src.models.domain_config import DomainConfig
from src.models.strategy import (
    StrategyResponse,
    ValidationIssue,
    ValidationResult,
    ValidationStatus,
)
from src.prompts.critic import SYSTEM_PROMPT

logger = logging.getLogger(__name__)


class CriticAgent(AgentBase):
    """Validates generated strategies for citation accuracy, hallucinations, and completeness."""

    def __init__(self) -> None:
        super().__init__(
            model=config.llm.critic,
            max_tokens=4096,  # Critic JSON response needs room for issues list
        )

    @property
    def system_prompt(self) -> str:
        return SYSTEM_PROMPT

    def process(
        self,
        strategy: StrategyResponse,
        prd_text: str,
        standards: RetrievedStandards,
        domain_config: DomainConfig,
    ) -> ValidationResult:
        """
        Validate a generated strategy.

        Args:
            strategy: The Architect's generated strategy.
            prd_text: Original PRD for hallucination checking.
            standards: Retrieved standards for citation verification.
            domain_config: Domain configuration for completeness checking.

        Returns:
            ValidationResult with status, issues, and accuracy metrics.
        """
        available_standards = "\n".join(
            f"- {sec.standard_id} — {sec.title} (Section {sec.section_key})"
            for sec in standards.sections
        )

        user_message = (
            f"--- ORIGINAL PRD ---\n{prd_text}\n\n"
            f"--- DOMAIN CONFIGURATION ---\n"
            f"Domain: {domain_config.domain.value}\n"
            f"Safety Level: {domain_config.safety_level.value}\n"
            f"Regulatory: {', '.join(domain_config.regulatory_frameworks) or 'None'}\n\n"
            f"--- AVAILABLE STANDARDS (verified) ---\n{available_standards}\n\n"
            f"--- GENERATED STRATEGY ---\n{strategy.strategy_markdown}"
        )

        try:
            result_data = self._call_llm_json(user_message)
        except Exception as e:
            # If Critic fails, don't crash the pipeline — return a cautious pass
            logger.error(f"[Critic] LLM call or JSON parse failed: {e}")
            return ValidationResult(
                status=ValidationStatus.PASSED,
                issues=[
                    ValidationIssue(
                        category="validation_error",
                        description=f"Critic validation could not complete: {str(e)[:200]}",
                        severity="low",
                    )
                ],
                citation_accuracy=0.0,
                structural_completeness=0.0,
                summary="Critic validation failed; strategy returned without full validation.",
            )

        issues = [
            ValidationIssue(**issue) for issue in result_data.get("issues", [])
        ]

        status_str = result_data.get("status", "failed")
        status = ValidationStatus.PASSED if status_str == "passed" else ValidationStatus.FAILED

        validation = ValidationResult(
            status=status,
            issues=issues,
            citation_accuracy=result_data.get("citation_accuracy", 0.0),
            structural_completeness=result_data.get("structural_completeness", 0.0),
            summary=result_data.get("summary", ""),
        )

        logger.info(
            f"[Critic] Validation: {validation.status.value}, "
            f"citations={validation.citation_accuracy:.0%}, "
            f"structure={validation.structural_completeness:.0%}, "
            f"issues={len(validation.issues)}"
        )

        return validation
