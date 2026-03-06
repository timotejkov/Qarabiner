"""
Shared pytest fixtures for Qarabiner tests.

Provides fixtures for:
- Sample PRD text
- Domain configuration
- System profile
- Standards library
- FastAPI test client
"""

import pytest
import asyncio
from httpx import AsyncClient

from src.app import app
from src.models.domain_config import DomainConfig, IndustryDomain, SafetyLevel
from src.models.profile import SystemProfile
from src.standards.library import StandardsLibrary


@pytest.fixture
def event_loop():
    """Create an event loop for async tests."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def sample_prd_text() -> str:
    """Sample PRD text for testing."""
    return """
    # E-Commerce Platform Requirements

    ## Overview
    A cloud-based e-commerce platform built with Node.js backend, React frontend,
    and PostgreSQL database. Handles user authentication, product catalog, shopping cart,
    and payment processing.

    ## Technology Stack
    - Backend: Node.js with Express
    - Frontend: React with Next.js
    - Database: PostgreSQL
    - Infrastructure: Docker, AWS (EC2, RDS, CloudFront)
    - Message Queue: RabbitMQ for order processing
    - Cache: Redis

    ## Key Features
    - User registration and login (OAuth2 + JWT)
    - Product search and filtering
    - Shopping cart and checkout
    - Payment integration (Stripe API)
    - Order tracking
    - Admin dashboard

    ## Non-Functional Requirements
    - Expected 1000 concurrent users
    - 99.9% uptime SLA
    - Support for US and EU regions
    - GDPR compliance required for EU users
    - PCI-DSS v4.0 for payment processing
    - Data encryption at rest and in transit

    ## Security Considerations
    - User PII and payment data must be protected
    - API rate limiting required
    - CORS configured for specific domains
    - SQL injection and XSS prevention
    """


@pytest.fixture
def sample_domain_config() -> DomainConfig:
    """Sample domain configuration for testing."""
    return DomainConfig(
        domain=IndustryDomain.FINANCIAL,
        safety_level=SafetyLevel.HIGH,
        regulatory_frameworks=["GDPR", "PCI-DSS v4.0"],
        deployment_jurisdictions=["EU", "US"],
        deployment_environment="cloud",
        additional_context="Payment processing is critical for this e-commerce platform.",
    )


@pytest.fixture
def sample_profile() -> SystemProfile:
    """Sample system profile for testing."""
    return SystemProfile(
        backend_stack=["Node.js", "Express"],
        frontend_stack=["React", "Next.js"],
        databases=["PostgreSQL", "Redis"],
        infrastructure=["Docker", "AWS", "EC2", "RDS"],
        languages=["JavaScript", "TypeScript"],
        message_queues=["RabbitMQ"],
        architecture_pattern="microservices",
        api_style="REST",
        data_sensitivity="confidential",
        identified_risks=["Payment data breach", "SQL injection", "XSS attacks"],
        data_types_handled=["PII", "financial"],
        inferred_domain="financial",
        user_roles=["admin", "customer", "vendor"],
        integration_points=["Stripe API", "OAuth2 provider"],
        expected_users="1000 concurrent",
        availability_requirements="99.9% uptime",
        summary="Cloud-based e-commerce platform with Node.js/React stack and payment processing.",
    )


@pytest.fixture
def standards_library() -> StandardsLibrary:
    """Load and return the standards library."""
    return StandardsLibrary()


@pytest.fixture
async def test_client():
    """Create an async test client for FastAPI."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client
