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
        result_data = self._call_llm_json(user_message, temperature=0.3)

        if result_data.get("response_type") == "questions":
            questions = [
                ClarifyingQuestion(**q) for q in result_data.get("questions", [])
            ]
            return QuestionsResponse(
                questions=questions,
                gaps_summary=result_data.get("gaps_summary", ""),
            )
        else:
            return StrategyResponse(
                strategy_markdown=result_data.get("strategy_markdown", ""),
                standards_cited=result_data.get("standards_cited", []),
                domain_sections_included=result_data.get("domain_sections_included", []),
            )
