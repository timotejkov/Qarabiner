"""
Agent 3: Architect — Generates the test strategy.

This is the core reasoning engine. Uses the strongest available model
to produce a comprehensive, standards-compliant test strategy.
"""

import json
import logging

from src.agents.base import AgentBase
from src.agents.researcher import RetrievedStandards
from src.config import config
from src.models.domain_config import DomainConfig
from src.models.profile import SystemProfile
from src.models.strategy import (
    ClarifyingQuestion,
    PipelineResult,
    QuestionsResponse,
    StrategyResponse,
)
from src.prompts.architect import SYSTEM_PROMPT
from src.prompts.templates import get_output_template

logger = logging.getLogger(__name__)


class ArchitectAgent(AgentBase):
    """Generates test strategies or clarifying questions based on context completeness."""

    def __init__(self) -> None:
        super().__init__(
            model=config.llm.architect,
            max_tokens=config.max_tokens_strategy,
        )

    @property
    def system_prompt(self) -> str:
        return SYSTEM_PROMPT

    def process(
        self,
        prd_text: str,
        profile: SystemProfile,
        standards: RetrievedStandards,
        domain_config: DomainConfig,
        answered_questions: dict[str, str] | None = None,
        critic_feedback: str | None = None,
    ) -> PipelineResult:
        """
        Generate a test strategy or clarifying questions.

        Args:
            prd_text: Original PRD text.
            profile: Structured system profile from Profiler.
            standards: Retrieved standards from Researcher.
            domain_config: User's domain configuration.
            answered_questions: Previously answered clarifying questions.
            critic_feedback: Feedback from the Critic agent (on retry).

        Returns:
            Either QuestionsResponse (gaps found) or StrategyResponse (full strategy).
        """
        output_template = get_output_template(domain_config.domain)

        # Build the user message with all context
        parts = [
            "<user_context>",
            prd_text,
            "</user_context>",
            "",
            "<domain_config>",
            f"Domain: {domain_config.domain.value}",
            f"Safety Level: {domain_config.safety_level.value}",
            f"Regulatory Frameworks: {', '.join(domain_config.regulatory_frameworks) or 'None specified'}",
            f"Deployment Jurisdictions: {', '.join(domain_config.deployment_jurisdictions) or 'None specified'}",
            f"Hardware Constraints: {domain_config.hardware_constraints or 'None'}",
            f"Deployment Environment: {domain_config.deployment_environment}",
            "</domain_config>",
            "",
            "<retrieved_standards>",
            standards.to_prompt_text(),
            "</retrieved_standards>",
            "",
            "<output_template>",
            output_template,
            "</output_template>",
        ]

        if answered_questions:
            parts.extend([
                "",
                "<answered_questions>",
                json.dumps(answered_questions, indent=2),
                "</answered_questions>",
            ])

        if critic_feedback:
            parts.extend([
                "",
                "<critic_feedback>",
                "The Critic agent found issues with your previous output. Fix them:",
                critic_feedback,
                "</critic_feedback>",
            ])

        user_message = "\n".join(parts)

        # Call LLM and parse response
        try:
            result_data = self._call_llm_json(user_message, temperature=0.3)
        except Exception as e:
            logger.error(f"[Architect] LLM call failed: {e}")
            raise RuntimeError(f"Architect agent failed to generate output: {e}") from e

        if not isinstance(result_data, dict):
            logger.error(f"[Architect] LLM returned non-dict: {type(result_data)}")
            raise RuntimeError("Architect returned invalid response format")

        if result_data.get("response_type") == "questions":
            questions_raw = result_data.get("questions", [])
            if not questions_raw:
                logger.warning("[Architect] Questions response with empty questions list")
                raise RuntimeError("Architect returned questions response but no questions were generated")
            questions = []
            for q in questions_raw:
                try:
                    questions.append(ClarifyingQuestion(**q))
                except Exception as e:
                    logger.warning(f"[Architect] Skipping malformed question: {e}")
            if not questions:
                raise RuntimeError("Architect returned questions but all were malformed")
            return QuestionsResponse(
                questions=questions,
                gaps_summary=result_data.get("gaps_summary", ""),
            )
        else:
            strategy_md = result_data.get("strategy_markdown", "")
            if not strategy_md or len(strategy_md.strip()) < 50:
                logger.error(
                    f"[Architect] Strategy markdown is empty or too short "
                    f"({len(strategy_md)} chars). Keys in response: {list(result_data.keys())}"
                )
                raise RuntimeError(
                    "Architect generated an empty or near-empty strategy. "
                    "This usually means the LLM response was truncated or malformed."
                )
            return StrategyResponse(
                strategy_markdown=strategy_md,
                standards_cited=result_data.get("standards_cited", []),
                domain_sections_included=result_data.get("domain_sections_included", []),
            )
