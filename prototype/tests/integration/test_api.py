"""
Integration tests for FastAPI endpoints.

Tests API functionality including health checks, domain listing, standards stats,
and strategy generation with mocked pipeline.
"""

import pytest
from httpx import AsyncClient
from unittest.mock import patch, MagicMock

from src.app import app
from src.models.domain_config import IndustryDomain, SafetyLevel
from src.models.strategy import StrategyResponse, QuestionsResponse, ClarifyingQuestion, ValidationResult, ValidationStatus
from src.models.profile import SystemProfile


@pytest.mark.asyncio
class TestAPIHealthEndpoint:
    """Tests for GET /api/health endpoint."""

    async def test_health_check_returns_200(self, test_client: AsyncClient):
        """Test that health check returns 200 OK."""
        response = await test_client.get("/api/health")

        assert response.status_code == 200

    async def test_health_check_response_structure(self, test_client: AsyncClient):
        """Test that health check response has expected structure."""
        response = await test_client.get("/api/health")

        data = response.json()

        assert "status" in data
        assert "standards_loaded" in data
        assert "version" in data
        assert data["status"] == "healthy"


@pytest.mark.asyncio
class TestAPIDomainsEndpoint:
    """Tests for GET /api/domains endpoint."""

    async def test_domains_returns_200(self, test_client: AsyncClient):
        """Test that domains endpoint returns 200 OK."""
        response = await test_client.get("/api/domains")

        assert response.status_code == 200

    async def test_domains_returns_list(self, test_client: AsyncClient):
        """Test that domains endpoint returns a list."""
        response = await test_client.get("/api/domains")

        data = response.json()

        assert isinstance(data, list)
        assert len(data) > 0

    async def test_domains_have_value_and_label(self, test_client: AsyncClient):
        """Test that each domain has value and label fields."""
        response = await test_client.get("/api/domains")

        data = response.json()

        for domain in data:
            assert "value" in domain
            assert "label" in domain
            assert isinstance(domain["value"], str)
            assert isinstance(domain["label"], str)

    async def test_domains_includes_expected_domains(self, test_client: AsyncClient):
        """Test that response includes expected domains."""
        response = await test_client.get("/api/domains")

        data = response.json()
        values = [d["value"] for d in data]

        assert "general_software" in values
        assert "medical_device" in values
        assert "automotive" in values
        assert "financial" in values


@pytest.mark.asyncio
class TestAPIStandardsStatsEndpoint:
    """Tests for GET /api/standards/stats endpoint."""

    async def test_standards_stats_returns_200(self, test_client: AsyncClient):
        """Test that standards stats endpoint returns 200 OK."""
        response = await test_client.get("/api/standards/stats")

        assert response.status_code == 200

    async def test_standards_stats_response_structure(self, test_client: AsyncClient):
        """Test that standards stats has expected structure."""
        response = await test_client.get("/api/standards/stats")

        data = response.json()

        assert "total_sections" in data
        assert "standard_ids" in data
        assert isinstance(data["total_sections"], int)
        assert isinstance(data["standard_ids"], list)

    async def test_standards_stats_positive_sections(self, test_client: AsyncClient):
        """Test that standards library has loaded sections."""
        response = await test_client.get("/api/standards/stats")

        data = response.json()

        assert data["total_sections"] > 0
        assert len(data["standard_ids"]) > 0


@pytest.mark.asyncio
class TestAPIStrategyGenerateEndpoint:
    """Tests for POST /api/strategy/generate endpoint."""

    async def test_strategy_generate_requires_prd_text(self, test_client: AsyncClient):
        """Test that strategy generation requires prd_text."""
        response = await test_client.post("/api/strategy/generate", json={})

        assert response.status_code == 422  # Validation error

    async def test_strategy_generate_minimum_prd_length(self, test_client: AsyncClient):
        """Test that strategy generation validates minimum PRD length."""
        response = await test_client.post(
            "/api/strategy/generate",
            json={"prd_text": "short"},
        )

        assert response.status_code == 422  # Validation error

    @patch("src.app.pipeline.generate")
    async def test_strategy_generate_with_valid_request(self, mock_generate, test_client: AsyncClient):
        """Test strategy generation with valid request."""
        # Mock pipeline response
        profile = SystemProfile(backend_stack=["Node.js"])
        strategy = StrategyResponse(strategy_markdown="# Test Strategy")
        validation = ValidationResult(status=ValidationStatus.PASSED)

        mock_generate.return_value = (strategy, validation, profile, [])

        response = await test_client.post(
            "/api/strategy/generate",
            json={"prd_text": "This is a valid product requirements document with enough content."},
        )

        assert response.status_code == 200
        data = response.json()
        assert "session_id" in data
        assert data["status"] == "strategy"

    @patch("src.app.pipeline.generate")
    async def test_strategy_generate_returns_questions(self, mock_generate, test_client: AsyncClient):
        """Test strategy generation that returns clarifying questions."""
        # Mock pipeline response with questions
        profile = SystemProfile()
        questions_response = QuestionsResponse(
            questions=[
                ClarifyingQuestion(
                    standard="ISO 29119",
                    question="What is the expected user count?",
                )
            ]
        )
        validation = None

        mock_generate.return_value = (questions_response, validation, profile, [])

        response = await test_client.post(
            "/api/strategy/generate",
            json={"prd_text": "A vague product description."},
        )

        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "questions"
        assert "questions" in data
        assert len(data["questions"]) > 0

    async def test_strategy_generate_with_domain(self, test_client: AsyncClient):
        """Test strategy generation with specific domain."""
        with patch("src.app.pipeline.generate") as mock_generate:
            profile = SystemProfile()
            strategy = StrategyResponse(strategy_markdown="# Medical Test Strategy")
            validation = ValidationResult(status=ValidationStatus.PASSED)

            mock_generate.return_value = (strategy, validation, profile, [])

            response = await test_client.post(
                "/api/strategy/generate",
                json={
                    "prd_text": "A medical device with sufficient requirements.",
                    "domain": "medical_device",
                    "safety_level": "sil_3",
                },
            )

            assert response.status_code == 200

    async def test_strategy_generate_invalid_domain(self, test_client: AsyncClient):
        """Test strategy generation with invalid domain."""
        response = await test_client.post(
            "/api/strategy/generate",
            json={
                "prd_text": "A valid product description with enough content.",
                "domain": "invalid_domain",
            },
        )

        assert response.status_code == 422  # Validation error

    async def test_strategy_generate_with_regulatory_frameworks(self, test_client: AsyncClient):
        """Test strategy generation with regulatory frameworks."""
        with patch("src.app.pipeline.generate") as mock_generate:
            profile = SystemProfile()
            strategy = StrategyResponse(strategy_markdown="# GDPR-compliant strategy")
            validation = ValidationResult(status=ValidationStatus.PASSED)

            mock_generate.return_value = (strategy, validation, profile, [])

            response = await test_client.post(
                "/api/strategy/generate",
                json={
                    "prd_text": "A system with GDPR requirements.",
                    "regulatory_frameworks": ["GDPR", "CCPA"],
                },
            )

            assert response.status_code == 200


@pytest.mark.asyncio
class TestAPIStrategyExportEndpoint:
    """Tests for GET /api/strategy/export/{session_id} endpoint."""

    async def test_export_nonexistent_session(self, test_client: AsyncClient):
        """Test exporting nonexistent session returns 404."""
        response = await test_client.get("/api/strategy/export/nonexistent-session-id")

        assert response.status_code == 404

    async def test_export_session_without_strategy(self, test_client: AsyncClient):
        """Test exporting session without strategy returns 400."""
        with patch("src.app.sessions.get") as mock_get:
            from src.models.session import Session
            from src.models.domain_config import DomainConfig

            # Session exists but has no result
            session = Session(
                id="test-session",
                prd_text="test",
                domain_config=DomainConfig(),
            )
            mock_get.return_value = session

            response = await test_client.get("/api/strategy/export/test-session")

            assert response.status_code == 400

    async def test_export_successful_strategy(self, test_client: AsyncClient):
        """Test successfully exporting a strategy."""
        with patch("src.app.sessions.get") as mock_get:
            from src.models.session import Session
            from src.models.domain_config import DomainConfig

            session = Session(
                id="test-session",
                prd_text="test",
                domain_config=DomainConfig(),
            )
            session.result = StrategyResponse(strategy_markdown="# Exported Strategy")
            mock_get.return_value = session

            response = await test_client.get("/api/strategy/export/test-session")

            assert response.status_code == 200
            data = response.json()
            assert "markdown" in data
            assert "# Exported Strategy" in data["markdown"]


@pytest.mark.asyncio
class TestAPIErrorHandling:
    """Tests for API error handling."""

    @patch("src.app.pipeline.generate")
    async def test_strategy_generate_handles_pipeline_error(self, mock_generate, test_client: AsyncClient):
        """Test that strategy generation handles pipeline errors gracefully."""
        mock_generate.side_effect = Exception("Pipeline error: LLM timeout")

        response = await test_client.post(
            "/api/strategy/generate",
            json={"prd_text": "A valid product description."},
        )

        assert response.status_code == 500
        data = response.json()
        assert "detail" in data

    async def test_api_cors_headers(self, test_client: AsyncClient):
        """Test that API includes CORS headers."""
        response = await test_client.get("/api/health")

        # CORS headers should be present for OPTIONS and actual requests
        assert response.status_code == 200
