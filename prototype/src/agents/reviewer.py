"""
Peer Review Agent — Evaluates strategy quality across 5 dimensions.

This is a separate agent used for benchmarking and quality assurance,
not part of the main generation pipeline.
"""

import logging
from typing import Any

from src.agents.base import AgentBase
from src.config import config
from src.models.domain_config import DomainConfig
from src.prompts.reviewer import SYSTEM_PROMPT

logger = logging.getLogger(__name__)


class ReviewerAgent(AgentBase):
    """Peer-reviews generated strategies for quality benchmarking."""

    def __init__(self) -> None:
        super().__init__(
            model=config.llm.reviewer,
            max_tokens=config.max_tokens_profile,
        )

    @property
    def system_prompt(self) -> str:
        return SYSTEM_PROMPT

    def process(
        self,
        prd_text: str,
        domain_config: DomainConfig,
        strategy_markdown: str,
    ) -> dict[str, Any]:
        """
        Peer-review a generated strategy.

        Args:
            prd_text: Original PRD.
            domain_config: Domain configuration.
            strategy_markdown: The generated strategy to review.

        Returns:
            Review report dict with grades, strengths, weaknesses, recommendations.
        """
        user_message = (
            f"--- ORIGINAL PRD ---\n{prd_text}\n\n"
            f"--- DOMAIN CONFIGURATION ---\n"
            f"Domain: {domain_config.domain.value}\n"
            f"Safety Level: {domain_config.safety_level.value}\n"
            f"Regulatory: {', '.join(domain_config.regulatory_frameworks) or 'None'}\n\n"
            f"--- GENERATED TEST STRATEGY ---\n{strategy_markdown}"
        )

        review = self._call_llm_json(user_message)
        grade = review.get("overall_grade", 0)

        logger.info(f"[Reviewer] Overall grade: {grade}/10")
        return review
