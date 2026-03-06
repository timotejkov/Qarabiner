"""
Application configuration.

Reads settings from environment variables with sensible defaults.
"""

import os
from dataclasses import dataclass, field
from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class LLMConfig:
    """LLM model configuration for each agent role."""
    profiler: str = field(default_factory=lambda: os.environ.get(
        "LLM_MODEL_PROFILER", "claude-haiku-4-5-20251001"))
    researcher: str = field(default_factory=lambda: os.environ.get(
        "LLM_MODEL_RESEARCHER", "claude-sonnet-4-5-20250929"))
    architect: str = field(default_factory=lambda: os.environ.get(
        "LLM_MODEL_ARCHITECT", "claude-sonnet-4-5-20250929"))
    critic: str = field(default_factory=lambda: os.environ.get(
        "LLM_MODEL_CRITIC", "claude-haiku-4-5-20251001"))
    reviewer: str = field(default_factory=lambda: os.environ.get(
        "LLM_MODEL_REVIEWER", "claude-sonnet-4-5-20250929"))


@dataclass(frozen=True)
class AppConfig:
    """Top-level application configuration."""
    anthropic_api_key: str = field(default_factory=lambda: os.environ.get(
        "ANTHROPIC_API_KEY", ""))
    llm: LLMConfig = field(default_factory=LLMConfig)
    max_critic_retries: int = 2
    max_tokens_strategy: int = 16384
    max_tokens_profile: int = 2048
    max_tokens_questions: int = 2048
    server_host: str = "0.0.0.0"
    server_port: int = 8000


# Singleton config instance
config = AppConfig()
