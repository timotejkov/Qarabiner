"""
Standards Library — keyword-based retrieval of QA standards content.

For the prototype, this replaces a Vector DB with simple keyword matching.
In production, this would be backed by Pinecone/Qdrant with semantic search.
"""

from dataclasses import dataclass
from typing import Optional

from src.models.domain_config import IndustryDomain
from src.standards import iso_29119, iso_25010, istqb, owasp, wcag
from src.standards import domain_medical, domain_automotive


@dataclass
class StandardSection:
    """A single retrievable section from a standard."""
    standard_id: str
    section_key: str
    title: str
    content: str
    keywords: list[str]
    relevance_score: float = 0.0


class StandardsLibrary:
    """
    Curated standards library with keyword-based retrieval.

    Usage:
        library = StandardsLibrary()
        sections = library.retrieve(
            domains=[IndustryDomain.MEDICAL_DEVICE],
            keywords=["risk", "verification", "validation"],
            max_results=10,
        )
    """

    # Maps domain → module(s) to load
    DOMAIN_MODULES = {
        IndustryDomain.MEDICAL_DEVICE: [domain_medical],
        IndustryDomain.AUTOMOTIVE: [domain_automotive],
    }

    # Core modules always loaded
    CORE_MODULES = [iso_29119, iso_25010, istqb, owasp, wcag]

    def __init__(self) -> None:
        self._sections: list[StandardSection] = []
        self._load_modules(self.CORE_MODULES)
        for modules in self.DOMAIN_MODULES.values():
            self._load_modules(modules)

    def _load_modules(self, modules: list) -> None:
        """Parse standard modules and index all sections."""
        for module in modules:
            standard_id = module.STANDARD_ID
            for group_key, group in module.SECTIONS.items():
                if "sections" in group:
                    for sec_key, sec in group["sections"].items():
                        self._sections.append(StandardSection(
                            standard_id=f"{standard_id} — {group.get('title', group_key)}",
                            section_key=sec_key,
                            title=sec["title"],
                            content=sec["content"],
                            keywords=sec.get("keywords", []),
                        ))

    def retrieve(
        self,
        domains: Optional[list[IndustryDomain]] = None,
        keywords: Optional[list[str]] = None,
        max_results: int = 20,
    ) -> list[StandardSection]:
        """
        Retrieve relevant standard sections by domain and keywords.

        Args:
            domains: Industry domains to include domain-specific standards for.
                     Core standards are always included.
            keywords: Search keywords to match against section content and keywords.
            max_results: Maximum number of sections to return.

        Returns:
            List of StandardSection objects sorted by relevance score (descending).
        """
        results: list[StandardSection] = []

        # Determine which domain modules are active
        active_domain_ids: set[str] = set()
        if domains:
            for domain in domains:
                for mod in self.DOMAIN_MODULES.get(domain, []):
                    active_domain_ids.add(mod.STANDARD_ID)

        for section in self._sections:
            # Core standards always included; domain standards only if domain is active
            is_core = any(
                section.standard_id.startswith(mod.STANDARD_ID)
                for mod in self.CORE_MODULES
            )
            is_active_domain = any(
                section.standard_id.startswith(did)
                for did in active_domain_ids
            )

            if not is_core and not is_active_domain:
                continue

            # Score by keyword overlap
            score = 0.0
            if keywords:
                kw_lower = [k.lower() for k in keywords]
                section_text = (section.content + " " + " ".join(section.keywords)).lower()
                for kw in kw_lower:
                    if kw in section_text:
                        score += 1.0
                    # Partial match on section keywords
                    for sk in section.keywords:
                        if kw in sk.lower():
                            score += 0.5
            else:
                score = 1.0  # If no keywords, include everything equally

            if score > 0:
                section.relevance_score = score
                results.append(section)

        # Sort by relevance
        results.sort(key=lambda s: s.relevance_score, reverse=True)
        return results[:max_results]

    def verify_citation(self, citation: str) -> bool:
        """
        Verify that a standard citation exists in the library.

        Args:
            citation: A citation string like "ISO 29119-2, Section 6.2"
                      or "OWASP ASVS Level 2" or "ISTQB Foundation 4.2"

        Returns:
            True if the citation can be matched to a section in the library.
        """
        citation_lower = citation.lower()
        for section in self._sections:
            # Check if citation matches standard_id + section_key
            sid_lower = section.standard_id.lower()
            title_lower = section.title.lower()
            key_lower = section.section_key.lower()

            if (any(part in citation_lower for part in sid_lower.split(" — "))
                    or key_lower in citation_lower
                    or title_lower in citation_lower):
                return True
        return False

    def get_all_standard_ids(self) -> list[str]:
        """Return all unique standard IDs in the library."""
        return list(set(s.standard_id for s in self._sections))

    @property
    def total_sections(self) -> int:
        """Total number of indexed sections."""
        return len(self._sections)
