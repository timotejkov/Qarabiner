"""
Integration tests for the full pipeline.

Tests the Profiler → Researcher → Architect → Critic pipeline with mocked LLM calls.
"""

import json
import pytest
from unittest.mock import patch, MagicMock

from src.agents.orchestrator import PipelineOrchestrator
from src.models.domain_config import DomainConfig, IndustryDomain, SafetyLevel
from src.models.strategy import QuestionsResponse, StrategyResponse
from src.standards.library import StandardsLibrary


class TestPipelineOrchestrator:
    """Tests for PipelineOrchestrator."""

    def test_orchestrator_initialization(self):
        """Test that orchestrator initializes correctly."""
        library = StandardsLibrary()
        orchestrator = PipelineOrchestrator(library)

        assert orchestrator is not None

    def test_orchestrator_with_default_library(self):
        """Test that orchestrator can initialize with default library."""
        orchestrator = PipelineOrchestrator()

        assert orchestrator is not None

    @patch("src.agents.profiler.ProfilerAgent.process")
    @patch("src.agents.researcher.ResearcherAgent.process")
    @patch("src.agents.architect.ArchitectAgent.process")
    @patch("src.agents.critic.CriticAgent.process")
    def test_pipeline_returns_questions_for_vague_input(
        self,
        mock_critic,
        mock_architect,
        mock_researcher,
        mock_profiler,
    ):
        """Test that pipeline returns questions when PRD is vague."""
        from src.models.profile import SystemProfile
        from src.models.strategy import ClarifyingQuestion, ValidationResult, ValidationStatus

        # Mock profiler
        profile = SystemProfile(
            backend_stack=[],
            architecture_pattern="unknown",
            summary="Unclear requirements",
        )
        mock_profiler.return_value = profile

        # Mock researcher
        mock_researcher.return_value = []

        # Mock architect - returns questions
        questions = QuestionsResponse(
            questions=[
                ClarifyingQuestion(
                    standard="ISO 29119",
                    question="What is the technology stack?",
                    example_answer="Node.js backend with React frontend",
                ),
                ClarifyingQuestion(
                    standard="ISO 25010",
                    question="What are the performance requirements?",
                    example_answer="Response time < 500ms",
                ),
            ],
            gaps_summary="Missing technical details and performance requirements.",
        )
        mock_architect.return_value = questions

        # Mock critic
        validation = ValidationResult(status=ValidationStatus.PASSED)
        mock_critic.return_value = validation

        orchestrator = PipelineOrchestrator()
        prd_text = "We want to build something."
        domain_config = DomainConfig()

        result, validation, profile, standards = orchestrator.generate(prd_text, domain_config)

        assert isinstance(result, QuestionsResponse)
        assert len(result.questions) == 2
        assert result.response_type == "questions"

    @patch("src.agents.profiler.ProfilerAgent.process")
    @patch("src.agents.researcher.ResearcherAgent.process")
    @patch("src.agents.architect.ArchitectAgent.process")
    @patch("src.agents.critic.CriticAgent.process")
    def test_pipeline_returns_strategy_for_detailed_input(
        self,
        mock_critic,
        mock_architect,
        mock_researcher,
        mock_profiler,
    ):
        """Test that pipeline returns strategy for detailed PRD."""
        from src.models.profile import SystemProfile
        from src.models.strategy import ValidationResult, ValidationStatus

        # Mock profiler
        profile = SystemProfile(
            backend_stack=["Node.js", "Express"],
            frontend_stack=["React"],
            databases=["PostgreSQL"],
            infrastructure=["Docker", "AWS"],
            architecture_pattern="microservices",
            api_style="REST",
            data_sensitivity="confidential",
            identified_risks=["Data breach", "SQL injection"],
            summary="E-commerce platform with multiple microservices",
        )
        mock_profiler.return_value = profile

        # Mock researcher
        retrieved_standards = [
            MagicMock(
                standard_id="ISO 29119",
                title="Software Testing Standard",
                content="Testing best practices",
                relevance_score=0.9,
            ),
        ]
        mock_researcher.return_value = retrieved_standards

        # Mock architect - returns strategy
        strategy = StrategyResponse(
            strategy_markdown="""# Test Strategy

## Overview
Comprehensive test strategy for e-commerce platform.

## Test Levels
- Unit testing
- Integration testing
- System testing
- Performance testing
- Security testing

## Standards Cited
- ISO 29119 - Software Testing Standard
- OWASP ASVS - Application Security
""",
            standards_cited=["ISO 29119", "OWASP ASVS"],
            domain_sections_included=["E-commerce specific tests", "Payment processing tests"],
        )
        mock_architect.return_value = strategy

        # Mock critic
        validation = ValidationResult(
            status=ValidationStatus.PASSED,
            citation_accuracy=1.0,
            structural_completeness=1.0,
        )
        mock_critic.return_value = validation

        orchestrator = PipelineOrchestrator()
        prd_text = """
        # E-Commerce Platform

        ## Technology Stack
        - Backend: Node.js with Express
        - Frontend: React
        - Database: PostgreSQL
        - Infrastructure: Docker, AWS

        ## Features
        - User authentication with OAuth2
        - Product catalog with search
        - Shopping cart
        - Payment processing (Stripe)
        - Order tracking

        ## Non-Functional Requirements
        - 99.9% uptime SLA
        - 1000 concurrent users
        - GDPR compliance
        - PCI-DSS for payments
        """
        domain_config = DomainConfig(
            domain=IndustryDomain.FINANCIAL,
            safety_level=SafetyLevel.HIGH,
            regulatory_frameworks=["GDPR", "PCI-DSS"],
        )

        result, validation, returned_profile, standards = orchestrator.generate(prd_text, domain_config)

        assert isinstance(result, StrategyResponse)
        assert "# Test Strategy" in result.strategy_markdown
        assert "ISO 29119" in result.standards_cited
        assert result.response_type == "strategy"
        assert validation.status == ValidationStatus.PASSED

    @patch("src.agents.profiler.ProfilerAgent.process")
    @patch("src.agents.researcher.ResearcherAgent.process")
    @patch("src.agents.architect.ArchitectAgent.process")
    @patch("src.agents.critic.CriticAgent.process")
    def test_pipeline_with_answered_questions(
        self,
        mock_critic,
        mock_architect,
        mock_researcher,
        mock_profiler,
    ):
        """Test that pipeline incorporates answered questions."""
        from src.models.profile import SystemProfile
        from src.models.strategy import ValidationResult, ValidationStatus

        # Mock profiler
        profile = SystemProfile(
            backend_stack=["Python", "Django"],
            summary="Web application",
        )
        mock_profiler.return_value = profile

        # Mock researcher
        mock_researcher.return_value = []

        # Mock architect - returns strategy with answered questions
        strategy = StrategyResponse(
            strategy_markdown="# Test Strategy\nBased on responses...",
        )
        mock_architect.return_value = strategy

        # Mock critic
        validation = ValidationResult(status=ValidationStatus.PASSED)
        mock_critic.return_value = validation

        orchestrator = PipelineOrchestrator()
        prd_text = "A web application"
        domain_config = DomainConfig()
        answered_questions = {
            "What is the technology stack?": "Python Django with PostgreSQL",
            "What are the performance requirements?": "500ms response time",
        }

        result, validation, profile, standards = orchestrator.generate(
            prd_text,
            domain_config,
            answered_questions=answered_questions,
        )

        assert isinstance(result, StrategyResponse)
        # Verify architect was called (questions were passed to it)
        assert mock_architect.called

    @patch("src.agents.profiler.ProfilerAgent.process")
    @patch("src.agents.researcher.ResearcherAgent.process")
    @patch("src.agents.architect.ArchitectAgent.process")
    @patch("src.agents.critic.CriticAgent.process")
    def test_pipeline_profile_extraction(
        self,
        mock_critic,
        mock_architect,
        mock_researcher,
        mock_profiler,
    ):
        """Test that pipeline extracts system profile."""
        from src.models.profile import SystemProfile
        from src.models.strategy import ValidationResult, ValidationStatus

        expected_profile = SystemProfile(
            backend_stack=["Go"],
            frontend_stack=["Angular"],
            databases=["CockroachDB"],
            infrastructure=["Kubernetes"],
            languages=["Go", "TypeScript"],
            architecture_pattern="microservices",
            data_sensitivity="internal",
            identified_risks=["Rate limiting"],
            summary="Microservices platform",
        )
        mock_profiler.return_value = expected_profile
        mock_researcher.return_value = []
        mock_architect.return_value = StrategyResponse(strategy_markdown="# Test Strategy")
        mock_critic.return_value = ValidationResult(status=ValidationStatus.PASSED)

        orchestrator = PipelineOrchestrator()
        prd_text = "A microservices platform in Go"
        domain_config = DomainConfig()

        result, validation, returned_profile, standards = orchestrator.generate(prd_text, domain_config)

        assert returned_profile is not None
        assert returned_profile.backend_stack == ["Go"]
        assert returned_profile.frontend_stack == ["Angular"]
        assert returned_profile.architecture_pattern == "microservices"

    @patch("src.agents.profiler.ProfilerAgent.process")
    @patch("src.agents.researcher.ResearcherAgent.process")
    @patch("src.agents.architect.ArchitectAgent.process")
    def test_pipeline_domain_config_propagation(
        self,
        mock_architect,
        mock_researcher,
        mock_profiler,
    ):
        """Test that domain config is propagated through the pipeline."""
        from src.models.profile import SystemProfile

        profile = SystemProfile()
        mock_profiler.return_value = profile
        mock_researcher.return_value = []
        mock_architect.return_value = StrategyResponse(strategy_markdown="# Strategy")

        orchestrator = PipelineOrchestrator()
        domain_config = DomainConfig(
            domain=IndustryDomain.MEDICAL_DEVICE,
            safety_level=SafetyLevel.SIL_3,
            regulatory_frameworks=["IEC 62304"],
        )
        prd_text = "Medical device"

        orchestrator.generate(prd_text, domain_config)

        # Verify profiler was called with domain config
        assert mock_profiler.called
        call_args = mock_profiler.call_args
        assert call_args[0][1] == domain_config

    @patch("src.agents.profiler.ProfilerAgent.process")
    @patch("src.agents.researcher.ResearcherAgent.process")
    @patch("src.agents.architect.ArchitectAgent.process")
    @patch("src.agents.critic.CriticAgent.process")
    def test_pipeline_standards_retrieved(
        self,
        mock_critic,
        mock_architect,
        mock_researcher,
        mock_profiler,
    ):
        """Test that pipeline retrieves standards."""
        from src.models.profile import SystemProfile
        from src.standards.library import StandardSection
        from src.models.strategy import ValidationResult, ValidationStatus

        profile = SystemProfile()
        mock_profiler.return_value = profile

        # Mock researcher returns standards
        mock_section = StandardSection(
            standard_id="ISO 29119",
            section_key="test_planning",
            title="Test Planning",
            content="Create a test plan",
            keywords=["testing", "planning"],
            relevance_score=0.9,
        )
        mock_researcher.return_value = [mock_section]

        mock_architect.return_value = StrategyResponse(strategy_markdown="# Strategy")
        mock_critic.return_value = ValidationResult(status=ValidationStatus.PASSED)

        orchestrator = PipelineOrchestrator()
        prd_text = "An application"
        domain_config = DomainConfig()

        result, validation, profile, standards = orchestrator.generate(prd_text, domain_config)

        # Verify standards were returned
        assert len(standards) > 0
        assert standards[0].standard_id == "ISO 29119"
