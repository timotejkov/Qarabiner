"""
Text parser for PRD documents.

Handles raw text, Markdown, and GitHub URL inputs.
"""

import logging

from src.parsers.github_fetcher import fetch_github_content, is_github_url

logger = logging.getLogger(__name__)


def parse_text(content: str) -> str:
    """
    Clean and normalize PRD text input.

    If the input is a GitHub URL, fetches the file content first.
    Then handles plain text and Markdown by stripping excessive
    whitespace while preserving structure.

    Args:
        content: Raw text, Markdown, or a GitHub URL.

    Returns:
        Cleaned PRD text ready for the pipeline.

    Raises:
        ValueError: If a GitHub URL cannot be fetched.
    """
    content = content.strip()

    # Check if the input is a GitHub URL
    if is_github_url(content):
        logger.info(f"[TextParser] Detected GitHub URL, fetching content...")
        content = fetch_github_content(content)

    lines = content.strip().splitlines()
    cleaned = []
    for line in lines:
        stripped = line.rstrip()
        cleaned.append(stripped)
    return "\n".join(cleaned)
