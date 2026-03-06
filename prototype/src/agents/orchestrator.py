"""
Pipeline Orchestrator — Coordinates the 4-agent pipeline.

Flow: Profiler → Researcher → Architect → Critic
With retry logic if the Critic rejects the strategy.
"""

import logging
from typing import AsyncGenerator

from src.agents.profiler import ProfilerAgent
from src.agents.researcher import ResearcherAgent, RetrievedStandards
from src.agents.architect import ArchitectAgent
from src.agents.critic import CriticAgent
from src.config import config
from src.models.domain_config import DomainConfig
from src.models.profile import SystemProfile
from src.models.strategy import (
    PipelineResult,
    QuestionsResponse,
    StrategyResponse,
    ValidationResult,
    ValidationStatus,
)
from src.standards.library import StandardsLibrary

logger = logging.getLogger(__name__)


class PipelineOrchestrator:
    """
    Orchestrates the full Profiler → Researcher → Architect → Critic pipeline.

    Manages agent instantiation, data flow between agents, and retry logic
    when the Critic agent rejects a strategy.
    """

    def __init__(self, library: StandardsLibrary | None = None) -> None:
        self._library = library or StandardsLibrary()
        self._profiler = ProfilerAgent()
        self._researcher = ResearcherAgent(self._library)
        self._architect = ArchitectAgent()
        self._critic = CriticAgent()

    def generate(
        self,
        prd_text: str,
        domain_config: DomainConfig,
        answered_questions: dict[str, str] | None = None,
        on_status: callable = None,
    ) -> tuple[PipelineResult, ValidationResult | None, SystemProfile | None, RetrievedStandards | None]:
        """
        Run the full pipeline synchronously.

        Args:
            prd_text: Raw PRD or system description.
            domain_config: User's domain and regulatory configuration.
            answered_questions: Previously answered clarifying questions.
            on_status: Optional callback for progress updates.

        Returns:
            Tuple of (result, validation, profile, standards).
            - result: QuestionsResponse or StrategyResponse
            - validation: ValidationResult (None if questions returned)
            - profile: SystemProfile from Profiler
            - standards: RetrievedStandards from Researcher
        """
        def status(msg: str) -> None:
            logger.info(f"[Pipeline] {msg}")
            if on_status:
                on_status(msg)

        # Step 1: Profile
        status("Profiling system under test...")
        profile = self._profiler.process(prd_text, domain_config)

        # Step 2: Research
        status("Retrieving relevant standards...")
        standards = self._researcher.process(profile, domain_config)

        # Step 3: Architect (may return questions or strategy)
        status("Generating test strategy...")
        result = self._architect.process(
            prd_text=prd_text,
            profile=profile,
            standards=standards,
            domain_config=domain_config,
            answered_questions=answered_questions,
        )

        # If questions returned, no validation needed
        if isinstance(result, QuestionsResponse):
            status(f"Gap analysis complete — {len(result.questions)} questions generated")
            return result, None, profile, standards

        # Step 4: Critic validation loop
        validation = None
        for attempt in range(1, config.max_critic_retries + 1):
            status(f"Validating strategy (attempt {attempt})...")
            validation = self._critic.process(
                strategy=result,
                prd_text=prd_text,
                standards=standards,
                domain_config=domain_config,
            )

            if validation.status == ValidationStatus.PASSED:
                status("Validation passed — strategy approved")
                break

            if attempt < config.max_critic_retries:
                # Retry: send critic feedback to architect
                feedback = (
                    f"Issues found:\n"
                    + "\n".join(
                        f"- [{i.severity}] {i.category}: {i.description}"
                        for i in validation.issues
                    )
                )
                status(f"Validation failed — retrying with critic feedback...")
                result = self._architect.process(
                    prd_text=prd_text,
                    profile=profile,
                    standards=standards,
                    domain_config=domain_config,
                    answered_questions=answered_questions,
                    critic_feedback=feedback,
                )

                # If architect switched to questions on retry, break
                if isinstance(result, QuestionsResponse):
                    return result, None, profile, standards
            else:
                status("Validation failed after max retries — returning with warnings")

        return result, validation, profile, standards
