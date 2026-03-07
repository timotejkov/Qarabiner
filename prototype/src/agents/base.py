"""
Base agent class — LLM abstraction layer.

Uses Python's built-in urllib for HTTP calls to the Anthropic Messages API.
Zero external dependencies for the core LLM client — no SDK version issues,
no httpx required. Just standard library.
"""

import json
import logging
import urllib.request
import urllib.error
from abc import ABC, abstractmethod
from typing import Any

from src.config import config

logger = logging.getLogger(__name__)

# Anthropic API constants
ANTHROPIC_API_URL = "https://api.anthropic.com/v1/messages"
ANTHROPIC_VERSION = "2023-06-01"


class AgentBase(ABC):
    """
    Abstract base class for all pipeline agents.

    Subclasses must implement:
        - system_prompt: The agent's system prompt.
        - process(): The main execution method.
    """

    def __init__(self, model: str, max_tokens: int = 4096) -> None:
        """
        Initialize agent with a specific model and token limit.

        Args:
            model: The Claude model identifier (e.g., 'claude-sonnet-4-5-20250929').
            max_tokens: Maximum tokens in the response.
        """
        self.model = model
        self.max_tokens = max_tokens

    @property
    @abstractmethod
    def system_prompt(self) -> str:
        """The system prompt that defines this agent's behavior."""
        ...

    @abstractmethod
    def process(self, **kwargs: Any) -> Any:
        """Execute the agent's primary function."""
        ...

    def _call_llm(
        self,
        user_message: str,
        temperature: float = 0.2,
        timeout: int = 600,
        max_retries: int = 3,
    ) -> str:
        """
        Call the LLM with the agent's system prompt and a user message.

        Uses Python's built-in urllib — zero external dependencies.
        Retries automatically on timeouts and transient errors (429, 500, 529)
        with exponential backoff.

        Args:
            user_message: The user/input message to send.
            temperature: Sampling temperature (lower = more deterministic).
            timeout: Per-request timeout in seconds (default 600 = 10 min).
            max_retries: Maximum number of retry attempts.

        Returns:
            The LLM's text response.

        Raises:
            RuntimeError: On API communication failure after all retries exhausted.
        """
        import time

        logger.info(f"[{self.__class__.__name__}] Calling {self.model} ({len(user_message)} chars input)")

        payload = json.dumps({
            "model": self.model,
            "max_tokens": self.max_tokens,
            "temperature": temperature,
            "system": self.system_prompt,
            "messages": [{"role": "user", "content": user_message}],
        }).encode("utf-8")

        last_error = None
        for attempt in range(1, max_retries + 1):
            req = urllib.request.Request(
                ANTHROPIC_API_URL,
                data=payload,
                headers={
                    "Content-Type": "application/json",
                    "x-api-key": config.anthropic_api_key,
                    "anthropic-version": ANTHROPIC_VERSION,
                },
            )

            try:
                with urllib.request.urlopen(req, timeout=timeout) as resp:
                    data = json.loads(resp.read().decode("utf-8"))

                text = data["content"][0]["text"]
                usage = data.get("usage", {})
                stop_reason = data.get("stop_reason", "unknown")
                logger.info(
                    f"[{self.__class__.__name__}] Response: {len(text)} chars, "
                    f"stop_reason={stop_reason}, "
                    f"usage: {usage.get('input_tokens', '?')}in/{usage.get('output_tokens', '?')}out"
                )
                if stop_reason == "max_tokens":
                    logger.warning(
                        f"[{self.__class__.__name__}] Response truncated at max_tokens "
                        f"({self.max_tokens}). Output may be incomplete."
                    )
                return text

            except urllib.error.HTTPError as e:
                error_body = e.read().decode("utf-8", errors="replace")[:500]
                last_error = RuntimeError(f"Anthropic API returned {e.code}: {error_body}")

                # Retry on rate limit (429), server error (500), or overloaded (529)
                if e.code in (429, 500, 529) and attempt < max_retries:
                    # Check for Retry-After header
                    retry_after = e.headers.get("retry-after")
                    if retry_after:
                        wait = min(int(retry_after), 60)
                    else:
                        wait = min(2 ** attempt * 5, 60)  # 10s, 20s, 40s capped at 60
                    logger.warning(
                        f"[{self.__class__.__name__}] HTTP {e.code} on attempt {attempt}/{max_retries}, "
                        f"retrying in {wait}s..."
                    )
                    time.sleep(wait)
                    continue

                logger.error(f"[{self.__class__.__name__}] API error {e.code}: {error_body}")
                raise last_error from e

            except (urllib.error.URLError, TimeoutError, ConnectionError, OSError) as e:
                last_error = RuntimeError(f"LLM API request failed: {e}")
                if attempt < max_retries:
                    wait = min(2 ** attempt * 5, 60)
                    logger.warning(
                        f"[{self.__class__.__name__}] {type(e).__name__} on attempt {attempt}/{max_retries}, "
                        f"retrying in {wait}s..."
                    )
                    time.sleep(wait)
                    continue

                logger.error(f"[{self.__class__.__name__}] Failed after {max_retries} attempts: {e}")
                raise last_error from e

        raise last_error or RuntimeError("LLM call failed after all retries")

    def _call_llm_json(self, user_message: str, temperature: float = 0.1) -> Any:
        """
        Call LLM and parse the response as JSON.

        Handles common issues like markdown code fences around JSON.

        Args:
            user_message: The user/input message.
            temperature: Sampling temperature.

        Returns:
            Parsed JSON object.

        Raises:
            json.JSONDecodeError: If response cannot be parsed as JSON.
        """
        raw = self._call_llm(user_message, temperature=temperature)

        # Strip markdown code fences if present
        cleaned = raw.strip()
        if cleaned.startswith("```"):
            # Remove first line (```json or ```) and last line (```)
            lines = cleaned.split("\n")
            cleaned = "\n".join(lines[1:-1] if lines[-1].strip() == "```" else lines[1:])

        try:
            return json.loads(cleaned)
        except json.JSONDecodeError as parse_err:
            # Response may have been truncated by max_tokens.
            # Try to salvage what we can.
            logger.warning(f"[{self.__class__.__name__}] JSON parse failed, attempting truncation recovery")

            # Recovery 1: Strategy response — extract strategy_markdown
            marker = '"strategy_markdown"'
            if marker in cleaned:
                idx = cleaned.index(marker) + len(marker)
                rest = cleaned[idx:].lstrip().lstrip(":")
                rest = rest.lstrip()
                if rest.startswith('"'):
                    # Find the end of the JSON string value properly.
                    # Walk character by character looking for unescaped closing quote.
                    md_raw = rest[1:]  # skip opening quote
                    end_pos = None
                    i = 0
                    while i < len(md_raw):
                        if md_raw[i] == '\\':
                            i += 2  # skip escaped character
                            continue
                        if md_raw[i] == '"':
                            end_pos = i
                            break
                        i += 1

                    if end_pos is not None:
                        # Properly closed string — extract just the value
                        md_content = md_raw[:end_pos]
                    else:
                        # Truncated mid-string — take everything we have
                        md_content = md_raw
                        # Strip trailing incomplete escape sequences
                        if md_content.endswith('\\'):
                            md_content = md_content[:-1]

                    # Unescape JSON string escapes
                    md_content = md_content.replace('\\"', '"').replace("\\n", "\n").replace("\\t", "\t").replace("\\\\", "\\")

                    if len(md_content.strip()) >= 50:
                        logger.info(f"[{self.__class__.__name__}] Recovered {len(md_content)} chars of strategy markdown")
                        return {
                            "response_type": "strategy",
                            "strategy_markdown": md_content,
                            "standards_cited": [],
                            "domain_sections_included": [],
                            "_truncation_recovered": True,
                        }
                    else:
                        logger.warning(f"[{self.__class__.__name__}] Recovery 1 extracted only {len(md_content)} chars — too short, trying other recovery")

            # Recovery 2: Critic/validation response — try to fix truncated JSON
            if '"status"' in cleaned and ('"issues"' in cleaned or '"citation_accuracy"' in cleaned):
                logger.info(f"[{self.__class__.__name__}] Attempting critic JSON recovery")
                # Try to close any open arrays/objects to make it valid
                fixed = cleaned.rstrip()
                # Remove trailing incomplete string/value
                for _ in range(5):
                    try:
                        return json.loads(fixed + ']}}')
                    except json.JSONDecodeError:
                        pass
                    try:
                        return json.loads(fixed + ']}')
                    except json.JSONDecodeError:
                        pass
                    try:
                        return json.loads(fixed + '"}]}')
                    except json.JSONDecodeError:
                        pass
                    try:
                        return json.loads(fixed + '}')
                    except json.JSONDecodeError:
                        pass
                    # Strip last character and retry
                    fixed = fixed[:-1].rstrip().rstrip(',')

                # Last resort: extract status field and return minimal valid result
                import re
                status_match = re.search(r'"status"\s*:\s*"(passed|failed)"', cleaned)
                if status_match:
                    logger.warning(f"[{self.__class__.__name__}] Returning minimal critic result (status={status_match.group(1)})")
                    return {
                        "status": status_match.group(1),
                        "issues": [],
                        "citation_accuracy": 0.8 if status_match.group(1) == "passed" else 0.5,
                        "structural_completeness": 0.8 if status_match.group(1) == "passed" else 0.5,
                        "summary": "Validation response was truncated; partial result returned.",
                        "_truncation_recovered": True,
                    }

            # If we can't recover, re-raise with context
            logger.error(f"[{self.__class__.__name__}] JSON recovery failed. First 500 chars: {cleaned[:500]}")
            raise
