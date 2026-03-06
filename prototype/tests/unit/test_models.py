"""
Unit tests for Pydantic models.

Tests data validation, serialization, and enum values for all model classes.
"""

import pytest
from src.models.domain_config import DomainConfig, IndustryDomain, SafetyLevel
from src.models.profile import SystemProfile
from src.models.strategy import (
    ClarifyingQuestion,
    QuestionsResponse,
    StrategyResponse,
    ValidationResult,
    ValidationStatus,
    ValidationIssue,
)


class TestDomainConfigModel:
    """Tests for DomainConfig Pydantic model."""

    def test_domain_config_defaults(self):
        """Test that DomainConfig has sensible defaults."""
        config = DomainConfig()

        assert config.domain == IndustryDomain.GENERAL_SOFTWARE
        assert config.safety_level == SafetyLevel.NONE
        assert config.regulatory_frameworks == []
        assert config.deployment_jurisdictions == []
        assert config.hardware_constraints is None
        assert config.deployment_environment == "cloud"
        assert config.additional_context is None

    def test_domain_config_with_values(self):
        """Test DomainConfig with explicit values."""
        config = DomainConfig(
            domain=IndustryDomain.MEDICAL_DEVICE,
            safety_level=SafetyLevel.SIL_3,
            regulatory_frameworks=["IEC 62304", "FDA"],
            deployment_jurisdictions=["US"],
            hardware_constraints="ARM Cortex, 512MB RAM",
            deployment_environment="embedded",
            additional_context="Medical monitoring device",
        )

        assert config.domain == IndustryDomain.MEDICAL_DEVICE
        assert config.safety_level == SafetyLevel.SIL_3
        assert config.regulatory_frameworks == ["IEC 62304", "FDA"]
        assert config.deployment_jurisdictions == ["US"]
        assert config.hardware_constraints == "ARM Cortex, 512MB RAM"
        assert config.deployment_environment == "embedded"
        assert config.additional_context == "Medical monitoring device"

    def test_domain_config_serialization(self):
        """Test DomainConfig can be serialized to dict."""
        config = DomainConfig(
            domain=IndustryDomain.AUTOMOTIVE,
            safety_level=SafetyLevel.ASIL_D,
        )

        data = config.model_dump()

        assert isinstance(data, dict)
        assert data["domain"] == IndustryDomain.AUTOMOTIVE
        assert data["safety_level"] == SafetyLevel.ASIL_D


class TestIndustryDomainEnum:
    """Tests for IndustryDomain enum."""

    def test_industry_domain_values(self):
        """Test that all industry domains have expected values."""
        expected_domains = {
            IndustryDomain.GENERAL_SOFTWARE,
            IndustryDomain.MEDICAL_DEVICE,
            IndustryDomain.AUTOMOTIVE,
            IndustryDomain.AEROSPACE,
            IndustryDomain.FINANCIAL,
            IndustryDomain.EMBEDDED_IOT,
            IndustryDomain.TELECOM,
            IndustryDomain.RAILWAY,
            IndustryDomain.NUCLEAR,
            IndustryDomain.GAMING_GAMBLING,
            IndustryDomain.GOVERNMENT,
        }

        actual_domains = set(IndustryDomain)

        assert expected_domains == actual_domains

    def test_industry_domain_value_format(self):
        """Test that domain values are lowercase with underscores."""
        for domain in IndustryDomain:
            assert domain.value == domain.value.lower()
            assert domain.value.replace("_", "").isalnum()


class TestSafetyLevelEnum:
    """Tests for SafetyLevel enum."""

    def test_safety_level_generic_levels(self):
        """Test generic safety levels."""
        assert SafetyLevel.NONE.value == "none"
        assert SafetyLevel.LOW.value == "low"
        assert SafetyLevel.MEDIUM.value == "medium"
        assert SafetyLevel.HIGH.value == "high"
        assert SafetyLevel.CRITICAL.value == "critical"

    def test_safety_level_asil_levels(self):
        """Test ASIL (Automotive Safety Integrity Levels)."""
        assert SafetyLevel.ASIL_A.value == "asil_a"
        assert SafetyLevel.ASIL_B.value == "asil_b"
        assert SafetyLevel.ASIL_C.value == "asil_c"
        assert SafetyLevel.ASIL_D.value == "asil_d"

    def test_safety_level_sil_levels(self):
        """Test SIL (IEC 61508 Safety Integrity Levels)."""
        assert SafetyLevel.SIL_1.value == "sil_1"
        assert SafetyLevel.SIL_2.value == "sil_2"
        assert SafetyLevel.SIL_3.value == "sil_3"
        assert SafetyLevel.SIL_4.value == "sil_4"

    def test_safety_level_dal_levels(self):
        """Test DAL (Aerospace Design Assurance Levels)."""
        assert SafetyLevel.DAL_A.value == "dal_a"
        assert SafetyLevel.DAL_B.value == "dal_b"
        assert SafetyLevel.DAL_C.value == "dal_c"
        assert SafetyLevel.DAL_D.value == "dal_d"
        assert SafetyLevel.DAL_E.value == "dal_e"


class TestSystemProfileModel:
    """Tests for SystemProfile Pydantic model."""

    def test_system_profile_defaults(self):
        """Test that SystemProfile has sensible defaults."""
        profile = SystemProfile()

        assert profile.backend_stack == []
        assert profile.frontend_stack == []
        assert profile.databases == []
        assert profile.infrastructure == []
        assert profile.languages == []
        assert profile.message_queues == []
        assert profile.architecture_pattern == "unknown"
        assert profile.api_style == "unknown"
        assert profile.data_sensitivity == "internal"
        assert profile.identified_risks == []
        assert profile.data_types_handled == []
        assert profile.inferred_domain is None
        assert profile.user_roles == []
        assert profile.integration_points == []
        assert profile.expected_users is None
        assert profile.availability_requirements is None
        assert profile.summary == ""

    def test_system_profile_with_values(self):
        """Test SystemProfile with explicit values."""
        profile = SystemProfile(
            backend_stack=["Python", "Django"],
            frontend_stack=["Vue.js"],
            databases=["MongoDB", "Elasticsearch"],
            infrastructure=["Kubernetes", "GCP"],
            languages=["Python", "JavaScript"],
            message_queues=["Kafka"],
            architecture_pattern="microservices",
            api_style="REST",
            data_sensitivity="confidential",
            identified_risks=["Data breach", "API throttling"],
            data_types_handled=["PII"],
            inferred_domain="healthcare",
            user_roles=["doctor", "patient"],
            integration_points=["Email provider"],
            expected_users="10000",
            availability_requirements="99.99%",
            summary="Healthcare management system",
        )

        assert profile.backend_stack == ["Python", "Django"]
        assert profile.frontend_stack == ["Vue.js"]
        assert profile.databases == ["MongoDB", "Elasticsearch"]
        assert profile.architecture_pattern == "microservices"
        assert profile.inferred_domain == "healthcare"

    def test_system_profile_serialization(self):
        """Test SystemProfile can be serialized to dict."""
        profile = SystemProfile(
            backend_stack=["Node.js"],
            architecture_pattern="monolith",
        )

        data = profile.model_dump()

        assert isinstance(data, dict)
        assert data["backend_stack"] == ["Node.js"]
        assert data["architecture_pattern"] == "monolith"


class TestClarifyingQuestion:
    """Tests for ClarifyingQuestion model."""

    def test_clarifying_question_creation(self):
        """Test creating a ClarifyingQuestion."""
        question = ClarifyingQuestion(
            standard="ISO 25010 - Performance Efficiency",
            question="What is the expected response time for the API?",
            example_answer="Response should be < 500ms for 95th percentile.",
        )

        assert question.standard == "ISO 25010 - Performance Efficiency"
        assert question.question == "What is the expected response time for the API?"
        assert question.example_answer == "Response should be < 500ms for 95th percentile."

    def test_clarifying_question_without_example(self):
        """Test ClarifyingQuestion can have no example answer."""
        question = ClarifyingQuestion(
            standard="OWASP ASVS",
            question="What is the authentication mechanism?",
        )

        assert question.example_answer is None


class TestQuestionsResponse:
    """Tests for QuestionsResponse model."""

    def test_questions_response_creation(self):
        """Test creating a QuestionsResponse."""
        questions = [
            ClarifyingQuestion(
                standard="ISO 29119",
                question="What is the test scope?",
            ),
        ]

        response = QuestionsResponse(
            questions=questions,
            gaps_summary="Missing information about test scope and performance requirements.",
        )

        assert response.response_type == "questions"
        assert len(response.questions) == 1
        assert response.gaps_summary == "Missing information about test scope and performance requirements."

    def test_questions_response_default_type(self):
        """Test that QuestionsResponse has correct default response_type."""
        response = QuestionsResponse(questions=[])

        assert response.response_type == "questions"


class TestStrategyResponse:
    """Tests for StrategyResponse model."""

    def test_strategy_response_creation(self):
        """Test creating a StrategyResponse."""
        response = StrategyResponse(
            strategy_markdown="# Test Strategy\n\n## Overview\nThis is a test strategy.",
            standards_cited=["ISO 29119", "ISTQB"],
            domain_sections_included=["Performance Testing", "Security Testing"],
        )

        assert response.response_type == "strategy"
        assert "# Test Strategy" in response.strategy_markdown
        assert "ISO 29119" in response.standards_cited
        assert "Performance Testing" in response.domain_sections_included

    def test_strategy_response_defaults(self):
        """Test StrategyResponse default values."""
        response = StrategyResponse(strategy_markdown="# Test Strategy")

        assert response.response_type == "strategy"
        assert response.standards_cited == []
        assert response.domain_sections_included == []

    def test_strategy_response_serialization(self):
        """Test StrategyResponse can be serialized."""
        response = StrategyResponse(
            strategy_markdown="# Test Strategy",
            standards_cited=["ISO 29119"],
        )

        data = response.model_dump()

        assert isinstance(data, dict)
        assert data["response_type"] == "strategy"
        assert "ISO 29119" in data["standards_cited"]


class TestValidationStatus:
    """Tests for ValidationStatus enum."""

    def test_validation_status_values(self):
        """Test that ValidationStatus has expected values."""
        assert ValidationStatus.PASSED.value == "passed"
        assert ValidationStatus.FAILED.value == "failed"


class TestValidationIssue:
    """Tests for ValidationIssue model."""

    def test_validation_issue_creation(self):
        """Test creating a ValidationIssue."""
        issue = ValidationIssue(
            category="citation_invalid",
            description="Citation 'ISO 99999' does not exist in the standards library.",
            location="Section 3.2",
            severity="high",
        )

        assert issue.category == "citation_invalid"
        assert issue.description == "Citation 'ISO 99999' does not exist in the standards library."
        assert issue.location == "Section 3.2"
        assert issue.severity == "high"

    def test_validation_issue_default_severity(self):
        """Test ValidationIssue has default severity."""
        issue = ValidationIssue(
            category="missing_section",
            description="Security testing section is missing.",
        )

        assert issue.severity == "medium"
        assert issue.location is None


class TestValidationResult:
    """Tests for ValidationResult model."""

    def test_validation_result_passed(self):
        """Test a passed ValidationResult."""
        result = ValidationResult(
            status=ValidationStatus.PASSED,
            citation_accuracy=1.0,
            structural_completeness=1.0,
            summary="All checks passed.",
        )

        assert result.status == ValidationStatus.PASSED
        assert result.citation_accuracy == 1.0
        assert result.structural_completeness == 1.0
        assert result.issues == []

    def test_validation_result_failed_with_issues(self):
        """Test a failed ValidationResult with issues."""
        issues = [
            ValidationIssue(
                category="hallucination",
                description="Mentioned a non-existent standard.",
                severity="high",
            ),
        ]

        result = ValidationResult(
            status=ValidationStatus.FAILED,
            issues=issues,
            citation_accuracy=0.8,
            structural_completeness=0.9,
            summary="1 high-severity issue found.",
        )

        assert result.status == ValidationStatus.FAILED
        assert len(result.issues) == 1
        assert result.citation_accuracy == 0.8
        assert result.structural_completeness == 0.9

    def test_validation_result_default_values(self):
        """Test ValidationResult default values."""
        result = ValidationResult(status=ValidationStatus.PASSED)

        assert result.citation_accuracy == 1.0
        assert result.structural_completeness == 1.0
        assert result.summary == ""
        assert result.issues == []

    def test_validation_result_serialization(self):
        """Test ValidationResult can be serialized."""
        result = ValidationResult(
            status=ValidationStatus.PASSED,
            citation_accuracy=0.95,
        )

        data = result.model_dump()

        assert isinstance(data, dict)
        assert data["status"] == ValidationStatus.PASSED
        assert data["citation_accuracy"] == 0.95
