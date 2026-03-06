"""
Agent 1: Profiler — Extracts structured system profile from raw PRD text.

Uses a fast/cheap model (Haiku) since the task is structured extraction,
not deep reasoning. Now also infers domain, safety level, deployment
environment, and regulatory frameworks from the PRD content.
"""

import logging
from typing import Any

from src.agents.base import AgentBase
from src.config import config
from src.models.domain_config import DomainConfig, IndustryDomain, SafetyLevel
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

    def process(self, prd_text: str, domain_config: DomainConfig | None = None) -> SystemProfile:
        """
        Analyze PRD text and extract a structured system profile.

        Infers domain, safety level, deployment environment, and regulatory
        frameworks directly from the PRD. If domain_config is provided with
        non-default values, those are passed as hints.

        Args:
            prd_text: Raw PRD or system description text.
            domain_config: Optional user-provided domain configuration (overrides).

        Returns:
            SystemProfile with extracted technology stack, risks, and metadata.
        """
        if domain_config and domain_config.domain != IndustryDomain.GENERAL_SOFTWARE:
            user_message = (
                f"Analyze this system description and extract the profile.\n\n"
                f"User-provided hints (use as guidance but verify against PRD):\n"
                f"- Domain hint: {domain_config.domain.value}\n"
                f"- Safety level hint: {domain_config.safety_level.value}\n"
                f"- Regulatory frameworks hint: {', '.join(domain_config.regulatory_frameworks) or 'None specified'}\n\n"
                f"--- PRD / System Description ---\n{prd_text}"
            )
        else:
            user_message = (
                f"Analyze this system description and extract the profile.\n"
                f"Infer the domain, safety level, deployment environment, and "
                f"regulatory frameworks from the PRD content.\n\n"
                f"--- PRD / System Description ---\n{prd_text}"
            )

        profile_data = self._call_llm_json(user_message)
        profile = SystemProfile(**profile_data)

        logger.info(f"[Profiler] Extracted profile: {profile.architecture_pattern}, "
                     f"domain={profile.inferred_domain}, "
                     f"safety={profile.inferred_safety_level}, "
                     f"deployment={profile.inferred_deployment_environment}, "
                     f"sensitivity={profile.data_sensitivity}, "
                     f"risks={len(profile.identified_risks)}")
        return profile
