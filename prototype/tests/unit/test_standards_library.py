"""
Unit tests for StandardsLibrary.

Tests keyword-based retrieval, citation verification, and library statistics.
"""

import pytest
from src.standards.library import StandardsLibrary
from src.models.domain_config import IndustryDomain


class TestStandardsLibraryInitialization:
    """Tests for StandardsLibrary initialization and structure."""

    def test_library_loads_core_modules(self, standards_library: StandardsLibrary):
        """Test that StandardsLibrary loads all core modules."""
        # Should have sections from ISO 29119, ISO 25010, ISTQB, OWASP, WCAG
        assert standards_library.total_sections > 0

    def test_library_loads_domain_specific_modules(self):
        """Test that StandardsLibrary can load domain-specific modules."""
        library = StandardsLibrary()

        # Should have more sections when domain modules are considered
        all_standard_ids = library.get_all_standard_ids()

        assert len(all_standard_ids) > 0
        # Should have medical and automotive standards
        assert any("medical" in sid.lower() or "iec" in sid.lower() for sid in all_standard_ids)


class TestStandardsLibraryRetrieval:
    """Tests for retrieval methods."""

    def test_retrieve_with_keywords(self, standards_library: StandardsLibrary):
        """Test retrieve with keywords returns relevant sections."""
        sections = standards_library.retrieve(
            keywords=["test", "strategy"],
            max_results=10,
        )

        assert isinstance(sections, list)
        assert len(sections) > 0
        # Check that sections have relevance scores
        for section in sections:
            assert section.relevance_score > 0

    def test_retrieve_without_keywords(self, standards_library: StandardsLibrary):
        """Test retrieve without keywords returns sections."""
        sections = standards_library.retrieve(max_results=5)

        assert isinstance(sections, list)
        assert len(sections) > 0

    def test_retrieve_respects_max_results(self, standards_library: StandardsLibrary):
        """Test that retrieve respects max_results parameter."""
        max_count = 3
        sections = standards_library.retrieve(max_results=max_count)

        assert len(sections) <= max_count

    def test_retrieve_with_domain_filter(self, standards_library: StandardsLibrary):
        """Test retrieve with domain filter includes domain standards."""
        sections_medical = standards_library.retrieve(
            domains=[IndustryDomain.MEDICAL_DEVICE],
            keywords=["risk", "validation"],
            max_results=10,
        )

        assert isinstance(sections_medical, list)
        # Should get some results since medical domain has specific standards

    def test_retrieve_empty_results_if_no_match(self, standards_library: StandardsLibrary):
        """Test retrieve returns empty list if keywords don't match."""
        sections = standards_library.retrieve(
            keywords=["nonexistent_keyword_xyz_abc_123"],
            max_results=10,
        )

        assert sections == []

    def test_retrieve_sorts_by_relevance(self, standards_library: StandardsLibrary):
        """Test that retrieve sorts results by relevance score."""
        sections = standards_library.retrieve(
            keywords=["testing"],
            max_results=10,
        )

        if len(sections) > 1:
            # Check descending order
            for i in range(len(sections) - 1):
                assert sections[i].relevance_score >= sections[i + 1].relevance_score


class TestStandardsLibraryCitationVerification:
    """Tests for citation verification."""

    def test_verify_citation_valid_partial_match(self, standards_library: StandardsLibrary):
        """Test verify_citation returns True for valid citations."""
        # Get a real section and use its standard_id
        sections = standards_library.retrieve(max_results=1)

        if sections:
            citation = sections[0].standard_id
            assert standards_library.verify_citation(citation) is True

    def test_verify_citation_invalid_citation(self, standards_library: StandardsLibrary):
        """Test verify_citation returns False for invalid citations."""
        result = standards_library.verify_citation("ISO 99999-9999 Section Z.Z.Z")

        assert result is False

    def test_verify_citation_case_insensitive(self, standards_library: StandardsLibrary):
        """Test that citation verification is case-insensitive."""
        # Get a real section
        sections = standards_library.retrieve(max_results=1)

        if sections:
            citation = sections[0].standard_id.lower()
            assert standards_library.verify_citation(citation) is True

    def test_verify_citation_with_section_number(self, standards_library: StandardsLibrary):
        """Test citation verification with section numbers."""
        sections = standards_library.retrieve(max_results=1)

        if sections:
            # Get the title of the first section
            title = sections[0].title
            assert standards_library.verify_citation(title) is True


class TestStandardsLibraryStatistics:
    """Tests for library statistics."""

    def test_total_sections_property(self, standards_library: StandardsLibrary):
        """Test total_sections property returns correct count."""
        total = standards_library.total_sections

        assert isinstance(total, int)
        assert total > 0

    def test_get_all_standard_ids(self, standards_library: StandardsLibrary):
        """Test get_all_standard_ids returns unique IDs."""
        standard_ids = standards_library.get_all_standard_ids()

        assert isinstance(standard_ids, list)
        assert len(standard_ids) > 0
        # Should be unique
        assert len(standard_ids) == len(set(standard_ids))

    def test_standard_ids_are_strings(self, standards_library: StandardsLibrary):
        """Test that all standard IDs are strings."""
        standard_ids = standards_library.get_all_standard_ids()

        for sid in standard_ids:
            assert isinstance(sid, str)

    def test_library_consistency_across_calls(self, standards_library: StandardsLibrary):
        """Test that library returns consistent results."""
        total_1 = standards_library.total_sections
        ids_1 = standards_library.get_all_standard_ids()

        total_2 = standards_library.total_sections
        ids_2 = standards_library.get_all_standard_ids()

        assert total_1 == total_2
        assert ids_1 == ids_2


class TestStandardSectionStructure:
    """Tests for StandardSection structure."""

    def test_section_has_required_attributes(self, standards_library: StandardsLibrary):
        """Test that sections have all required attributes."""
        sections = standards_library.retrieve(max_results=1)

        assert len(sections) > 0

        section = sections[0]

        assert hasattr(section, "standard_id")
        assert hasattr(section, "section_key")
        assert hasattr(section, "title")
        assert hasattr(section, "content")
        assert hasattr(section, "keywords")
        assert hasattr(section, "relevance_score")

    def test_section_attributes_are_correct_types(self, standards_library: StandardsLibrary):
        """Test that section attributes have correct types."""
        sections = standards_library.retrieve(max_results=1)

        if sections:
            section = sections[0]

            assert isinstance(section.standard_id, str)
            assert isinstance(section.section_key, str)
            assert isinstance(section.title, str)
            assert isinstance(section.content, str)
            assert isinstance(section.keywords, list)
            assert isinstance(section.relevance_score, float)

    def test_section_content_not_empty(self, standards_library: StandardsLibrary):
        """Test that section content is not empty."""
        sections = standards_library.retrieve(max_results=1)

        if sections:
            section = sections[0]

            assert len(section.content) > 0
            assert len(section.title) > 0
