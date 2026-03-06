"""Simple text parser for PRD documents."""


def parse_text(content: str) -> str:
    """
    Clean and normalize PRD text input.

    Handles plain text and Markdown. Strips excessive whitespace
    while preserving structure.
    """
    lines = content.strip().splitlines()
    cleaned = []
    for line in lines:
        stripped = line.rstrip()
        cleaned.append(stripped)
    return "\n".join(cleaned)
