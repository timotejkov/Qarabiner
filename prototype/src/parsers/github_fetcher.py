"""
GitHub content fetcher — resolves GitHub URLs to raw file content.

Supports:
- github.com/user/repo/blob/branch/path/file.md
- raw.githubusercontent.com/user/repo/branch/path/file.md
- github.com/user/repo (fetches README.md)
"""

import logging
import re
import urllib.request
import urllib.error

logger = logging.getLogger(__name__)

# Patterns for GitHub URL detection
_GITHUB_URL_RE = re.compile(
    r"^https?://(www\.)?(github\.com|raw\.githubusercontent\.com)/",
    re.IGNORECASE,
)


def is_github_url(text: str) -> bool:
    """Check if text looks like a GitHub URL (not raw PRD text)."""
    text = text.strip()
    if "\n" in text:
        return False  # Multi-line text is not a URL
    return bool(_GITHUB_URL_RE.match(text))


def _to_raw_url(url: str) -> str:
    """Convert a GitHub web URL to a raw content URL."""
    url = url.strip()

    # Already a raw URL
    if "raw.githubusercontent.com" in url:
        return url

    # github.com/user/repo/blob/branch/path → raw.githubusercontent.com/user/repo/branch/path
    if "/blob/" in url:
        return url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")

    # github.com/user/repo/raw/branch/path → raw.githubusercontent.com/user/repo/branch/path
    if "/raw/" in url:
        return url.replace("github.com", "raw.githubusercontent.com").replace("/raw/", "/")

    # github.com/user/repo → try to fetch README.md from main branch
    # Strip trailing slash
    url = url.rstrip("/")
    parts = url.replace("https://github.com/", "").replace("http://github.com/", "").split("/")
    if len(parts) >= 2:
        user, repo = parts[0], parts[1]
        return f"https://raw.githubusercontent.com/{user}/{repo}/main/README.md"

    raise ValueError(f"Cannot resolve GitHub URL: {url}")


def fetch_github_content(url: str, timeout: int = 15) -> str:
    """
    Fetch raw file content from a GitHub URL.

    Args:
        url: GitHub URL (web or raw).
        timeout: Request timeout in seconds.

    Returns:
        Raw text content of the file.

    Raises:
        ValueError: If the URL is invalid or the file cannot be fetched.
    """
    raw_url = _to_raw_url(url)
    logger.info(f"[GitHubFetcher] Fetching: {raw_url}")

    req = urllib.request.Request(
        raw_url,
        headers={"User-Agent": "Qarabiner/0.1"},
    )

    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            content = response.read().decode("utf-8")
            logger.info(f"[GitHubFetcher] Fetched {len(content)} chars from {raw_url}")
            return content
    except urllib.error.HTTPError as e:
        if e.code == 404:
            # If we guessed README.md on main, try master branch
            if "/main/README.md" in raw_url:
                alt_url = raw_url.replace("/main/README.md", "/master/README.md")
                logger.info(f"[GitHubFetcher] main not found, trying master: {alt_url}")
                try:
                    alt_req = urllib.request.Request(
                        alt_url, headers={"User-Agent": "Qarabiner/0.1"}
                    )
                    with urllib.request.urlopen(alt_req, timeout=timeout) as response:
                        return response.read().decode("utf-8")
                except Exception:
                    pass
            raise ValueError(f"GitHub file not found (404): {raw_url}")
        raise ValueError(f"GitHub fetch error (HTTP {e.code}): {e.reason}")
    except urllib.error.URLError as e:
        raise ValueError(f"Network error fetching GitHub content: {e.reason}")
