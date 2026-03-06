"""
Unit tests for text parser.

Tests text cleaning, whitespace handling, and markdown support.
"""

import pytest
from src.parsers.text_parser import parse_text


class TestParseText:
    """Tests for parse_text function."""

    def test_parse_text_strips_leading_whitespace(self):
        """Test that parse_text strips leading whitespace."""
        text = "   \n\n  Some content here"
        result = parse_text(text)

        assert result.startswith("Some content here")

    def test_parse_text_strips_trailing_whitespace(self):
        """Test that parse_text strips trailing whitespace."""
        text = "Some content here  \n\n   "
        result = parse_text(text)

        assert result.endswith("Some content here")

    def test_parse_text_preserves_structure(self):
        """Test that parse_text preserves line structure."""
        text = """Line 1
Line 2
Line 3"""
        result = parse_text(text)

        lines = result.split("\n")
        assert len(lines) == 3
        assert lines[0] == "Line 1"
        assert lines[1] == "Line 2"
        assert lines[2] == "Line 3"

    def test_parse_text_removes_trailing_spaces_per_line(self):
        """Test that parse_text removes trailing spaces from each line."""
        text = "Line 1   \nLine 2   \nLine 3   "
        result = parse_text(text)

        lines = result.split("\n")
        for line in lines:
            assert not line.endswith(" ")

    def test_parse_text_preserves_markdown_formatting(self):
        """Test that parse_text preserves markdown formatting."""
        text = """# Header 1
## Header 2

- Bullet point 1
- Bullet point 2

**Bold text** and *italic text*"""
        result = parse_text(text)

        assert "# Header 1" in result
        assert "## Header 2" in result
        assert "- Bullet point 1" in result
        assert "**Bold text**" in result
        assert "*italic text*" in result

    def test_parse_text_handles_empty_lines(self):
        """Test that parse_text handles empty lines correctly."""
        text = """Line 1

Line 2

Line 3"""
        result = parse_text(text)

        lines = result.split("\n")
        assert len(lines) == 5
        assert lines[1] == ""
        assert lines[3] == ""

    def test_parse_text_empty_input(self):
        """Test parse_text with empty input."""
        text = ""
        result = parse_text(text)

        assert result == ""

    def test_parse_text_whitespace_only_input(self):
        """Test parse_text with whitespace-only input."""
        text = "   \n\n   \n\t\t  "
        result = parse_text(text)

        assert result == ""

    def test_parse_text_preserves_indentation(self):
        """Test that parse_text preserves internal indentation."""
        text = """Line 1
    Indented line
        More indented
Line 4"""
        result = parse_text(text)

        lines = result.split("\n")
        assert lines[1].startswith("    ")
        assert lines[2].startswith("        ")

    def test_parse_text_handles_tabs(self):
        """Test that parse_text handles tabs."""
        text = "Line 1\n\tTabbed line\n\t\tDouble tabbed"
        result = parse_text(text)

        assert "\t" in result

    def test_parse_text_multiline_prd(self):
        """Test parse_text with realistic PRD content."""
        prd = """
        # Product Requirements Document

        ## Overview
        This is a test application.

        ## Features
        - Feature 1
        - Feature 2
            - Subfeature

        ## Technical Stack
        - Frontend: React
        - Backend: Node.js
        """
        result = parse_text(prd)

        assert "Product Requirements Document" in result
        assert "Features" in result
        assert "Feature 1" in result
        # No leading/trailing whitespace
        assert not result.startswith(" ")
        assert not result.startswith("\n")

    def test_parse_text_idempotent(self):
        """Test that parsing twice gives same result."""
        text = "  \n  Some content  \n  "
        result1 = parse_text(text)
        result2 = parse_text(result1)

        assert result1 == result2

    def test_parse_text_single_line(self):
        """Test parse_text with single line."""
        text = "Single line of text"
        result = parse_text(text)

        assert result == "Single line of text"

    def test_parse_text_single_word(self):
        """Test parse_text with single word."""
        text = "word"
        result = parse_text(text)

        assert result == "word"

    def test_parse_text_special_characters(self):
        """Test parse_text preserves special characters."""
        text = "Line with special chars: !@#$%^&*()\n"
        result = parse_text(text)

        assert "!@#$%^&*()" in result

    def test_parse_text_unicode_characters(self):
        """Test parse_text handles unicode characters."""
        text = "Unicode: café, naïve, 你好\nMore text"
        result = parse_text(text)

        assert "café" in result
        assert "你好" in result
