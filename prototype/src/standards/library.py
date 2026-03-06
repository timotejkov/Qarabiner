"""
Standards Library — hybrid keyword + semantic retrieval of QA standards content.

Supports both keyword-based matching (always available) and ChromaDB-powered
semantic search (when chromadb is installed). The semantic search is preferred
when available, with keyword matching as fallback.
"""

import logging
from dataclasses import dataclass, field
from typing import Optional

from src.models.domain_config import IndustryDomain
from src.standards import iso_29119, iso_25010, istqb, owasp, wcag
from src.standards import domain_medical, domain_automotive
from src.standards.vectorstore import StandardsVectorStore

logger = logging.getLogger(__name__)


@dataclass
class StandardSection:
    """A single retrievable section from a standard."""
    standard_id: str
    section_key: str
    title: str
    content: str
    keywords: list[str]
    part: str = ""
    clause: str = ""
    relevance_score: float = 0.0


class StandardsLibrary:
    """
    Curated standards library with hybrid keyword + semantic retrieval.

    On init, loads all standard modules and builds a ChromaDB semantic
    index (if available). The Researcher agent can then use either
    keyword or semantic search.

    Usage:
        library = StandardsLibrary()

        # Semantic search (preferred)
        sections = library.retrieve_semantic("SQL injection testing", max_results=10)

        # Keyword search (fallback)
        sections = library.retrieve(keywords=["injection", "sql"], max_results=10)
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
        self._vectorstore = StandardsVectorStore()

        # Load all modules
        self._load_modules(self.CORE_MODULES)
        for modules in self.DOMAIN_MODULES.values():
            self._load_modules(modules)

        logger.info(f"[StandardsLibrary] Loaded {len(self._sections)} sections from {len(self.get_all_standard_ids())} standards")

        # Build vector index (non-blocking — falls back to keyword if unavailable)
        self._vectorstore.build_index(self._sections)

    def _load_modules(self, modules: list) -> None:
        """Parse standard modules and index all sections, including sub-sections."""
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
                            part=sec.get("part", group.get("title", "")),
                            clause=sec.get("clause", sec_key),
                        ))
                        # Also index sub-characteristics (e.g., ISO 25010)
                        if "sub_characteristics" in sec:
                            for sub_key, sub in sec["sub_characteristics"].items():
                                # Build content from available fields
                                content_parts = []
                                if "content" in sub:
                                    content_parts.append(sub["content"])
                                if "definition" in sub:
                                    content_parts.append(sub["definition"])
                                if "quality_metrics" in sub and isinstance(sub["quality_metrics"], list):
                                    content_parts.append("Quality metrics: " + "; ".join(sub["quality_metrics"]))
                                if "testing_approaches" in sub and isinstance(sub["testing_approaches"], list):
                                    content_parts.append("Testing approaches: " + "; ".join(sub["testing_approaches"]))
                                if "common_defect_patterns" in sub and isinstance(sub["common_defect_patterns"], list):
                                    content_parts.append("Common defect patterns: " + "; ".join(sub["common_defect_patterns"]))

                                self._sections.append(StandardSection(
                                    standard_id=f"{standard_id} — {sec['title']}",
                                    section_key=sub_key,
                                    title=sub.get("title", sub_key.replace("_", " ").title()),
                                    content=" ".join(content_parts),
                                    keywords=sub.get("keywords", sec.get("keywords", [])),
                                    part=sec.get("part", group.get("title", "")),
                                    clause=sub.get("clause", sub_key),
                                ))

    def retrieve_semantic(
        self,
        query: str,
        domains: Optional[list[IndustryDomain]] = None,
        max_results: int = 20,
    ) -> list[StandardSection]:
        """
        Retrieve relevant standard sections using semantic search.

        Falls back to keyword search if ChromaDB is unavailable.

        Args:
            query: Natural language query describing what standards are needed.
            domains: Optional domain filter.
            max_results: Maximum number of sections to return.

        Returns:
            List of StandardSection objects sorted by relevance.
        """
        if self._vectorstore.available:
            results = self._vectorstore.search(query, n=max_results)
            if results:
                # Filter by domain if needed
                if domains:
                    results = self._filter_by_domain(results, domains)
                logger.info(f"[StandardsLibrary] Semantic search: '{query[:50]}...' → {len(results)} results")
                return results[:max_results]
            logger.warning("[StandardsLibrary] Semantic search returned no results, falling back to keyword")

        # Fallback: extract keywords from query and use keyword search
        keywords = [w.lower() for w in query.split() if len(w) > 3]
        return self.retrieve(domains=domains, keywords=keywords, max_results=max_results)

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

    def _filter_by_domain(
        self,
        sections: list[StandardSection],
        domains: list[IndustryDomain],
    ) -> list[StandardSection]:
        """Filter sections to include core + domain-specific standards."""
        active_domain_ids: set[str] = set()
        for domain in domains:
            for mod in self.DOMAIN_MODULES.get(domain, []):
                active_domain_ids.add(mod.STANDARD_ID)

        filtered = []
        for section in sections:
            is_core = any(
                section.standard_id.startswith(mod.STANDARD_ID)
                for mod in self.CORE_MODULES
            )
            is_active_domain = any(
                section.standard_id.startswith(did)
                for did in active_domain_ids
            )
            if is_core or is_active_domain:
                filtered.append(section)

        return filtered

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
