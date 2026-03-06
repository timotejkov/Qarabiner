"""
Agent 1: Profiler — Extracts structured system profile from raw PRD text.

Uses a fast/cheap model (Haiku) since the task is structured extraction,
not deep reasoning.
"""

import logging
from typing import Any

from src.agents.base import AgentBase
from src.config import config
from src.models.domain_config import DomainConfig
from src.models.profile import SystemProfile
from src.prompts.profiler import SYSTEM_PROMPT

logger = logging.getLogger(__name__)


class ProfilerAgent(AgentBase):
    """Extracts a structured SystemProfile from raw PRD text."""

    def __init__(self) -> None:
        super().__init__(
            model=config.llm.profiler,
            max_tokens=config.max_tokens_profile,
        )

    @property
    def system_prompt(self) -> str:
        return SYSTEM_PROMPT

    def process(self, prd_text: str, domain_config: DomainConfig) -> SystemProfile:
        """
        Analyze PRD text and extract a structured system profile.

        Args:
            prd_text: Raw PRD or system description text.
            domain_config: User-selected domain configuration.

        Returns:
            SystemProfile with extracted technology stack, risks, and metadata.
        """
        user_message = (
            f"Analyze this system description and extract the profile.\n\n"
            f"User-selected domain: {domain_config.domain.value}\n"
            f"User-selected safety level: {domain_config.safety_level.value}\n"
            f"User-specified regulatory frameworks: {', '.join(domain_config.regulatory_frameworks) or 'None specified'}\n\n"
            f"--- PRD / System Description ---\n{prd_text}"
        )

        profile_data = self._call_llm_json(user_message)
        profile = SystemProfile(**profile_data)

        logger.info(f"[Profiler] Extracted profile: {profile.architecture_pattern}, "
                     f"sensitivity={profile.data_sensitivity}, "
                     f"risks={len(profile.identified_risks)}")
        return profile
