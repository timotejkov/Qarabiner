"""
Agent 2: Researcher — Retrieves relevant standards based on system profile.

Uses the StandardsLibrary with hybrid retrieval: semantic search via
ChromaDB (when available) with keyword matching as fallback.
"""

import logging
from dataclasses import dataclass

from src.agents.base import AgentBase
from src.config import config
from src.models.domain_config import DomainConfig
from src.models.profile import SystemProfile
from src.prompts.researcher import SYSTEM_PROMPT
from src.standards.library import StandardsLibrary, StandardSection

logger = logging.getLogger(__name__)


@dataclass
class RetrievedStandards:
    """Package of standards retrieved for the Architect."""
    sections: list[StandardSection]
    search_keywords: list[str]
    standard_families: list[str]
    justification: str

    def to_prompt_text(self, max_sections: int = 15, max_chars_per_section: int = 800) -> str:
        """Format retrieved standards for injection into the Architect prompt.

        Caps the number of sections and truncates long content to keep
        the Architect's input under ~20K chars and avoid timeouts.

        Args:
            max_sections: Maximum number of sections to include.
            max_chars_per_section: Truncate section content beyond this length.
        """
        lines = []
        for sec in self.sections[:max_sections]:
            content = sec.content
            if len(content) > max_chars_per_section:
                content = content[:max_chars_per_section].rsplit(" ", 1)[0] + "..."
            lines.append(
                f"**{sec.standard_id} — {sec.title}** (Section {sec.section_key}):\n"
                f"{content}\n"
            )
        return "\n".join(lines)

    def get_standard_ids(self) -> list[str]:
        """Get unique standard IDs for citation verification."""
        return list(set(sec.standard_id for sec in self.sections))


class ResearcherAgent(AgentBase):
    """Determines which standards to retrieve, then queries the library."""

    def __init__(self, library: StandardsLibrary) -> None:
        super().__init__(
            model=config.llm.researcher,
            max_tokens=config.max_tokens_profile,
        )
        self._library = library

    @property
    def system_prompt(self) -> str:
        return SYSTEM_PROMPT

    def process(
        self,
        profile: SystemProfile,
        domain_config: DomainConfig,
    ) -> RetrievedStandards:
        """
        Identify relevant standards and retrieve them from the library.

        Args:
            profile: Structured system profile from the Profiler.
            domain_config: User-selected domain and regulatory context.

        Returns:
            RetrievedStandards with sections ready for injection into the Architect prompt.
        """
        # Ask the LLM which keywords and standards to search for
        user_message = (
            f"System Profile:\n{profile.model_dump_json(indent=2)}\n\n"
            f"Domain Configuration:\n"
            f"  Domain: {domain_config.domain.value}\n"
            f"  Safety Level: {domain_config.safety_level.value}\n"
            f"  Regulatory: {', '.join(domain_config.regulatory_frameworks) or 'None'}\n"
            f"  Hardware Constraints: {domain_config.hardware_constraints or 'None'}\n"
        )

        research_plan = self._call_llm_json(user_message)
        keywords = research_plan.get("search_keywords", [])
        families = research_plan.get("required_standard_families", [])
        justification = research_plan.get("justification", "")

        logger.info(f"[Researcher] Search keywords: {keywords}")
        logger.info(f"[Researcher] Required families: {families}")

        # Build a semantic search query from the profile summary + keywords
        semantic_query = (
            f"{profile.summary} "
            f"Domain: {domain_config.domain.value}. "
            f"Key areas: {', '.join(keywords[:10])}."
        )

        # Try semantic search first, fall back to keyword search
        sections = self._library.retrieve_semantic(
            query=semantic_query,
            domains=[domain_config.domain],
            max_results=25,
        )

        # If semantic returned few results, supplement with keyword search
        if len(sections) < 10:
            keyword_sections = self._library.retrieve(
                domains=[domain_config.domain],
                keywords=keywords,
                max_results=25 - len(sections),
            )
            # Merge without duplicates
            seen_keys = {(s.standard_id, s.section_key) for s in sections}
            for ks in keyword_sections:
                if (ks.standard_id, ks.section_key) not in seen_keys:
                    sections.append(ks)
                    seen_keys.add((ks.standard_id, ks.section_key))

        logger.info(f"[Researcher] Retrieved {len(sections)} standard sections (semantic+keyword)")

        return RetrievedStandards(
            sections=sections,
            search_keywords=keywords,
            standard_families=families,
            justification=justification,
        )
