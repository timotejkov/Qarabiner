"""
Unit tests for ProfilerAgent.

Tests profile extraction with mocked LLM calls.
"""

import json
import pytest
from unittest.mock import patch, MagicMock

from src.agents.profiler import ProfilerAgent
from src.models.domain_config import DomainConfig, IndustryDomain, SafetyLevel
from src.models.profile import SystemProfile


class TestProfilerAgent:
    """Tests for ProfilerAgent with mocked LLM."""

    def test_profiler_initialization(self):
        """Test that ProfilerAgent initializes correctly."""
        agent = ProfilerAgent()

        assert agent.model is not None
        assert agent.max_tokens > 0
        assert agent.system_prompt is not None

    def test_profiler_has_system_prompt(self):
        """Test that profiler has a system prompt."""
        agent = ProfilerAgent()

        prompt = agent.system_prompt

        assert isinstance(prompt, str)
        assert len(prompt) > 0

    @patch("src.agents.base.anthropic.Anthropic.messages.create")
    def test_profiler_process_returns_system_profile(self, mock_create):
        """Test that process returns a SystemProfile."""
        # Mock LLM response
        mock_response = MagicMock()
        mock_response.content = [MagicMock()]
        mock_response.content[0].text = json.dumps({
            "backend_stack": ["Node.js", "Express"],
            "frontend_stack": ["React"],
            "databases": ["PostgreSQL"],
            "infrastructure": ["Docker", "AWS"],
            "languages": ["JavaScript"],
            "message_queues": [],
            "architecture_pattern": "REST API",
            "api_style": "REST",
            "data_sensitivity": "internal",
            "identified_risks": [],
            "data_types_handled": [],
            "inferred_domain": "general_software",
            "user_roles": [],
            "integration_points": [],
            "expected_users": None,
            "availability_requirements": None,
            "summary": "A simple REST API",
        })
        mock_response.usage.input_tokens = 100
        mock_response.usage.output_tokens = 50

        mock_create.return_value = mock_response

        agent = ProfilerAgent()
        domain_config = DomainConfig()
        prd_text = "A simple Node.js REST API"

        profile = agent.process(prd_text, domain_config)

        assert isinstance(profile, SystemProfile)
        assert "Node.js" in profile.backend_stack
        assert "React" in profile.frontend_stack

    @patch("src.agents.base.anthropic.Anthropic.messages.create")
    def test_profiler_extracts_technology_stack(self, mock_create):
        """Test that profiler extracts technology stack."""
        mock_response = MagicMock()
        mock_response.content = [MagicMock()]
        mock_response.content[0].text = json.dumps({
            "backend_stack": ["Python", "FastAPI"],
            "frontend_stack": ["Vue.js"],
            "databases": ["MongoDB", "Redis"],
            "infrastructure": ["Kubernetes", "GCP"],
            "languages": ["Python", "JavaScript"],
            "message_queues": ["RabbitMQ"],
            "architecture_pattern": "microservices",
            "api_style": "REST",
            "data_sensitivity": "confidential",
            "identified_risks": ["Data breach"],
            "data_types_handled": ["PII"],
            "inferred_domain": None,
            "user_roles": ["admin"],
            "integration_points": ["Payment gateway"],
            "expected_users": "1000",
            "availability_requirements": "99.9%",
            "summary": "Healthcare application",
        })
        mock_response.usage.input_tokens = 100
        mock_response.usage.output_tokens = 50

        mock_create.return_value = mock_response

        agent = ProfilerAgent()
        domain_config = DomainConfig()
        prd_text = "Healthcare app with Python backend"

        profile = agent.process(prd_text, domain_config)

        assert profile.backend_stack == ["Python", "FastAPI"]
        assert profile.frontend_stack == ["Vue.js"]
        assert profile.databases == ["MongoDB", "Redis"]
        assert profile.infrastructure == ["Kubernetes", "GCP"]
        assert profile.message_queues == ["RabbitMQ"]

    @patch("src.agents.base.anthropic.Anthropic.messages.create")
    def test_profiler_extracts_architecture_and_api(self, mock_create):
        """Test that profiler extracts architecture and API style."""
        mock_response = MagicMock()
        mock_response.content = [MagicMock()]
        mock_response.content[0].text = json.dumps({
            "backend_stack": [],
            "frontend_stack": [],
            "databases": [],
            "infrastructure": [],
            "languages": [],
            "message_queues": [],
            "architecture_pattern": "serverless",
            "api_style": "GraphQL",
            "data_sensitivity": "internal",
            "identified_risks": [],
            "data_types_handled": [],
            "inferred_domain": None,
            "user_roles": [],
            "integration_points": [],
            "expected_users": None,
            "availability_requirements": None,
            "summary": "Serverless GraphQL API",
        })
        mock_response.usage.input_tokens = 100
        mock_response.usage.output_tokens = 50

        mock_create.return_value = mock_response

        agent = ProfilerAgent()
        domain_config = DomainConfig()
        prd_text = "Serverless GraphQL application"

        profile = agent.process(prd_text, domain_config)

        assert profile.architecture_pattern == "serverless"
        assert profile.api_style == "GraphQL"

    @patch("src.agents.base.anthropic.Anthropic.messages.create")
    def test_profiler_extracts_security_and_risks(self, mock_create):
        """Test that profiler extracts security and risk information."""
        mock_response = MagicMock()
        mock_response.content = [MagicMock()]
        mock_response.content[0].text = json.dumps({
            "backend_stack": [],
            "frontend_stack": [],
            "databases": [],
            "infrastructure": [],
            "languages": [],
            "message_queues": [],
            "architecture_pattern": "unknown",
            "api_style": "unknown",
            "data_sensitivity": "restricted",
            "identified_risks": ["Data breach", "SQL injection", "DDoS"],
            "data_types_handled": ["PII", "financial", "medical"],
            "inferred_domain": "healthcare",
            "user_roles": ["doctor", "patient", "admin"],
            "integration_points": ["LDAP", "Email provider"],
            "expected_users": "10000",
            "availability_requirements": "99.99%",
            "summary": "Healthcare management system",
        })
        mock_response.usage.input_tokens = 100
        mock_response.usage.output_tokens = 50

        mock_create.return_value = mock_response

        agent = ProfilerAgent()
        domain_config = DomainConfig()
        prd_text = "Healthcare management system"

        profile = agent.process(prd_text, domain_config)

        assert profile.data_sensitivity == "restricted"
        assert len(profile.identified_risks) == 3
        assert "Data breach" in profile.identified_risks
        assert "PII" in profile.data_types_handled
        assert profile.inferred_domain == "healthcare"
        assert "doctor" in profile.user_roles

    @patch("src.agents.base.anthropic.Anthropic.messages.create")
    def test_profiler_with_domain_config(self, mock_create):
        """Test that profiler respects domain configuration."""
        mock_response = MagicMock()
        mock_response.content = [MagicMock()]
        mock_response.content[0].text = json.dumps({
            "backend_stack": [],
            "frontend_stack": [],
            "databases": [],
            "infrastructure": [],
            "languages": [],
            "message_queues": [],
            "architecture_pattern": "unknown",
            "api_style": "unknown",
            "data_sensitivity": "internal",
            "identified_risks": [],
            "data_types_handled": [],
            "inferred_domain": None,
            "user_roles": [],
            "integration_points": [],
            "expected_users": None,
            "availability_requirements": None,
            "summary": "Medical device",
        })
        mock_response.usage.input_tokens = 100
        mock_response.usage.output_tokens = 50

        mock_create.return_value = mock_response

        agent = ProfilerAgent()
        domain_config = DomainConfig(
            domain=IndustryDomain.MEDICAL_DEVICE,
            safety_level=SafetyLevel.SIL_3,
            regulatory_frameworks=["IEC 62304"],
        )
        prd_text = "Medical device PRD"

        profile = agent.process(prd_text, domain_config)

        # Verify the call was made
        assert mock_create.called
        # Check that domain info was passed to LLM
        call_args = mock_create.call_args
        messages = call_args.kwargs["messages"]
        assert len(messages) > 0
        assert "MEDICAL_DEVICE" in messages[0]["content"]

    @patch("src.agents.base.anthropic.Anthropic.messages.create")
    def test_profiler_handles_markdown_code_fence_response(self, mock_create):
        """Test that profiler handles JSON in markdown code fences."""
        # Mock response with JSON in code fence
        mock_response = MagicMock()
        mock_response.content = [MagicMock()]
        mock_response.content[0].text = """```json
{
    "backend_stack": ["Node.js"],
    "frontend_stack": [],
    "databases": ["MongoDB"],
    "infrastructure": [],
    "languages": ["JavaScript"],
    "message_queues": [],
    "architecture_pattern": "unknown",
    "api_style": "unknown",
    "data_sensitivity": "internal",
    "identified_risks": [],
    "data_types_handled": [],
    "inferred_domain": null,
    "user_roles": [],
    "integration_points": [],
    "expected_users": null,
    "availability_requirements": null,
    "summary": "Node.js app"
}
```"""
        mock_response.usage.input_tokens = 100
        mock_response.usage.output_tokens = 50

        mock_create.return_value = mock_response

        agent = ProfilerAgent()
        domain_config = DomainConfig()
        prd_text = "Node.js application"

        profile = agent.process(prd_text, domain_config)

        assert isinstance(profile, SystemProfile)
        assert profile.backend_stack == ["Node.js"]
        assert profile.databases == ["MongoDB"]
