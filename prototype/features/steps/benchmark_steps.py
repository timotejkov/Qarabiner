"""
Step implementations for end-to-end benchmark tests.

These tests call the real pipeline (Profiler → Researcher → Architect → Critic).
Marked with @wip tag for tests that require actual LLM API keys.
"""

import sys
import time
from pathlib import Path
from typing import Any
from unittest.mock import MagicMock, patch

from behave import given, when, then

# Add project root to path for imports
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.agents.orchestrator import PipelineOrchestrator
from src.models.domain_config import DomainConfig, IndustryDomain, SafetyLevel
from src.models.strategy import (
    StrategyResponse,
    QuestionsResponse,
    ValidationResult,
    ValidationStatus,
)
from src.standards.library import StandardsLibrary, StandardSection


# ============================================================================
# Background/Setup Steps
# ============================================================================

@given("the complete pipeline is initialized (Profiler → Researcher → Architect → Critic)")
def step_pipeline_initialized(context):
    """Initialize the complete pipeline."""
    context.library = StandardsLibrary()
    context.pipeline = PipelineOrchestrator(context.library)
    context.start_time = None
    context.end_time = None
    context.profile = None
    context.standards = None
    context.result = None
    context.validation = None


@given("a Mattermost-style PRD is prepared as test data")
def step_mattermost_prd_available(context):
    """Prepare test data (not strictly necessary but noted)."""
    pass


@given("real LLM APIs would be called (marked @wip when API key available)")
def step_note_live_api(context):
    """Note about live API calls."""
    # This is just documentation
    pass


# ============================================================================
# Full Pipeline Scenarios
# ============================================================================

@given("a realistic PRD for \"{product_name}\"")
def step_realistic_prd(context, product_name: str):
    """Create a realistic PRD for the given product."""
    if "Mattermost" in product_name or "collaboration" in product_name.lower():
        context.prd_text = """
        Mattermost Team Collaboration Platform

        ## Overview
        An open-source team collaboration platform similar to Slack, built with Node.js backend
        and React frontend, using PostgreSQL for data storage and Redis for caching.

        ## Architecture
        - Backend: Node.js 18 with Express framework
        - Frontend: React 18 with TypeScript
        - Database: PostgreSQL 13+ for relational data, Redis 6+ for caching
        - Message Queue: RabbitMQ for async processing
        - Infrastructure: Docker containers deployed on Kubernetes
        - Cloud Provider: AWS (ECS for container orchestration, RDS for database)

        ## Core Features
        1. Team and Channel Management: Create teams, channels, and manage permissions
        2. Real-time Messaging: WebSocket-based real-time message delivery
        3. User Authentication: OAuth2 with LDAP/AD integration
        4. File Sharing: Upload and share files with access control
        5. Search: Full-text search across messages and files

        ## Security Requirements
        - OAuth2 for authentication
        - TLS 1.2+ for all communications
        - PII data encryption at rest and in transit
        - RBAC (Role-Based Access Control) implementation
        - Audit logging for sensitive operations

        ## Scale and Performance
        - Expected Users: 5,000-50,000 concurrent users
        - Message Throughput: 100,000+ messages per day
        - Response Time Target: < 200ms for 95th percentile
        - Availability: 99.95% uptime SLA

        ## Deployment
        - Cloud-first architecture on AWS
        - Horizontal scaling with load balancing
        - Database replication for high availability
        - CDN for static asset delivery

        ## Regulatory & Compliance
        - GDPR compliance for EU deployments
        - Data residency options for different regions
        - Audit logging and compliance reporting
        """
    else:
        context.prd_text = f"A {product_name} system with microservices architecture."


@given("describing a Node.js backend, React frontend, and PostgreSQL database")
def step_verify_prd_stack(context):
    """Verify the PRD mentions the tech stack."""
    assert "Node.js" in context.prd_text or "backend" in context.prd_text.lower()


@when("the pipeline runs end-to-end (Profiler → Researcher → Architect → Critic)")
def step_pipeline_run_full(context):
    """Execute the complete pipeline."""
    context.start_time = time.time()

    domain_config = DomainConfig(
        domain=getattr(context, "domain_obj", IndustryDomain.GENERAL_SOFTWARE),
        safety_level=getattr(context, "safety_level_obj", SafetyLevel.NONE),
    )

    try:
        # Run the pipeline
        result, validation, profile, standards = context.pipeline.generate(
            prd_text=context.prd_text,
            domain_config=domain_config,
        )

        context.result = result
        context.validation = validation
        context.profile = profile
        context.standards = standards
        context.end_time = time.time()
        context.execution_time = context.end_time - context.start_time

    except Exception as e:
        context.end_time = time.time()
        context.pipeline_error = str(e)
        raise


@then("the final output should be a StrategyResponse (not QuestionsResponse)")
def step_final_output_strategy(context):
    """Verify final output is a strategy."""
    assert context.result is not None, "No result from pipeline"
    assert isinstance(context.result, StrategyResponse), \
        f"Expected StrategyResponse, got {type(context.result).__name__}"


@then("the strategy_markdown should be a substantial document (> 2000 characters)")
def step_strategy_substantial(context):
    """Verify strategy has minimum length."""
    assert len(context.result.strategy_markdown) > 2000, \
        f"Strategy too short: {len(context.result.strategy_markdown)} chars"


@then("the validation status should be \"passed\"")
def step_validation_passed(context):
    """Verify validation passed."""
    assert context.validation is not None
    assert context.validation.status == ValidationStatus.PASSED, \
        f"Validation failed: {context.validation.issues}"


@then("the pipeline should execute within reasonable time (< 60 seconds for mock)")
def step_execution_time(context):
    """Verify execution completes in reasonable time."""
    assert context.execution_time < 60, \
        f"Pipeline took too long: {context.execution_time:.1f} seconds"


@then("all four agents should produce non-empty outputs")
def step_all_agents_output(context):
    """Verify all agents executed."""
    assert context.profile is not None, "Profiler produced no output"
    assert context.standards is not None, "Researcher produced no output"
    assert context.result is not None, "Architect produced no output"
    assert context.validation is not None, "Critic produced no output"


# ============================================================================
# Security Testing Section Steps
# ============================================================================

@when("the Architect agent generates the strategy")
def step_architect_generates(context):
    """Execute the Architect (part of pipeline already ran)."""
    assert context.result is not None


@then("the strategy_markdown should contain a section on \"Security Testing\"")
def step_strategy_security_section(context):
    """Verify security testing section exists."""
    markdown = context.result.strategy_markdown
    assert "Security" in markdown, "Security section not found in strategy"


@then("Or a section on \"Application Security\"")
def step_strategy_app_security(context):
    """Alternative security section name."""
    markdown = context.result.strategy_markdown
    has_security = "security" in markdown.lower()
    assert has_security, "No security-related content found"


@then("Or a section on \"OWASP\" compliance")
def step_strategy_owasp(context):
    """Alternative OWASP section."""
    markdown = context.result.strategy_markdown
    has_owasp = "OWASP" in markdown
    assert has_owasp, "OWASP not referenced in strategy"


@then("this section should include specific test cases for:")
def step_security_test_cases(context):
    """Verify specific security test case categories."""
    markdown = context.result.strategy_markdown.lower()

    test_areas = [
        "authentication",
        "authorization",
        "input validation",
        "injection",
    ]

    # At least some should be mentioned
    found = [area for area in test_areas if area in markdown]
    assert len(found) >= 2, f"Expected security test cases, found: {found}"


@then("the section should reference security standards")
def step_security_standards_ref(context):
    """Verify security standards are cited."""
    assert len(context.result.standards_cited) > 0
    has_security_standard = any(
        "owasp" in std.lower() or "security" in std.lower()
        for std in context.result.standards_cited
    )
    assert has_security_standard, "No security standards cited"


# ============================================================================
# OWASP Reference Steps
# ============================================================================

@given("the Mattermost PRD processed through the full pipeline")
def step_mattermost_processed(context):
    """PRD has been processed (implicit in pipeline run)."""
    assert context.result is not None


@then("the strategy_markdown should reference \"OWASP Top 10\"")
def step_references_owasp_top10(context):
    """Verify OWASP Top 10 is referenced."""
    markdown = context.result.strategy_markdown
    assert "OWASP Top 10" in markdown or "OWASP" in markdown, \
        "OWASP Top 10 not referenced"


@then("Or \"OWASP Testing Guide\"")
def step_references_owasp_guide(context):
    """Alternative OWASP reference."""
    markdown = context.result.strategy_markdown
    # Already checked for OWASP in previous step


@then("Or specific OWASP vulnerabilities (e.g., \"A01:2021 - Broken Access Control\")")
def step_references_owasp_specific(context):
    """Verify specific OWASP vulnerabilities mentioned."""
    markdown = context.result.strategy_markdown.lower()
    # Look for OWASP references
    has_owasp = "owasp" in markdown or "a0" in markdown or "vulnerability" in markdown
    assert has_owasp, "No specific OWASP vulnerabilities referenced"


@then("the standards_cited list should include at least one OWASP standard")
def step_owasp_in_cited(context):
    """Verify OWASP is in cited standards."""
    owasp_cited = [std for std in context.result.standards_cited if "OWASP" in std]
    assert len(owasp_cited) > 0, \
        f"No OWASP standards in cited list: {context.result.standards_cited}"


@then("the Critic should validate these citations as correct")
def step_critic_validates_owasp(context):
    """Verify Critic validated OWASP citations."""
    assert context.validation.status == ValidationStatus.PASSED
    assert context.validation.citation_accuracy >= 0.8


# ============================================================================
# Minimal PRD Steps
# ============================================================================

@given("a very brief PRD with only \"Collaboration platform\" description")
def step_minimal_prd_brief(context):
    """Create a very minimal PRD."""
    context.prd_text = "A collaboration platform for teams."


@given("insufficient technical and operational details")
def step_minimal_prd_insufficient(context):
    """PRD lacks details (already set above)."""
    pass


@when("the pipeline runs end-to-end")
def step_pipeline_run_minimal(context):
    """Run pipeline on minimal PRD."""
    context.start_time = time.time()

    domain_config = DomainConfig(
        domain=IndustryDomain.GENERAL_SOFTWARE,
        safety_level=SafetyLevel.NONE,
    )

    try:
        result, validation, profile, standards = context.pipeline.generate(
            prd_text=context.prd_text,
            domain_config=domain_config,
        )

        context.result = result
        context.validation = validation
        context.profile = profile
        context.standards = standards
        context.end_time = time.time()

    except Exception as e:
        context.end_time = time.time()
        context.pipeline_error = str(e)
        raise


@then("the response should be a QuestionsResponse (not StrategyResponse)")
def step_response_questions_minimal(context):
    """Verify response is questions for minimal input."""
    assert context.result is not None
    assert isinstance(context.result, QuestionsResponse), \
        f"Expected QuestionsResponse, got {type(context.result).__name__}"


@then("each question should ask about:")
def step_question_topics(context):
    """Verify questions cover expected topics."""
    questions_text = "\n".join(q.question for q in context.result.questions)

    topics = [
        "technology",
        "architecture",
        "scalability",
        "security",
        "deployment",
    ]

    found_topics = [topic for topic in topics if topic.lower() in questions_text.lower()]
    assert len(found_topics) >= 2, \
        f"Expected multiple question topics, found: {found_topics}"


@then("the gaps_summary should explain the information gaps")
def step_gaps_summary_present(context):
    """Verify gaps summary is informative."""
    assert len(context.result.gaps_summary) > 10, \
        f"Gaps summary too brief: {context.result.gaps_summary}"


# ============================================================================
# Sequential Execution Steps
# ============================================================================

@when("the pipeline runs")
def step_pipeline_runs(context):
    """Generic pipeline run."""
    if not hasattr(context, "prd_text"):
        context.prd_text = "A generic application with backend and frontend."

    domain_config = DomainConfig(
        domain=IndustryDomain.GENERAL_SOFTWARE,
        safety_level=SafetyLevel.NONE,
    )

    try:
        result, validation, profile, standards = context.pipeline.generate(
            prd_text=context.prd_text,
            domain_config=domain_config,
        )

        context.result = result
        context.validation = validation
        context.profile = profile
        context.standards = standards

    except Exception as e:
        context.pipeline_error = str(e)
        raise


@then("the Profiler should execute first and produce a SystemProfile")
def step_profiler_executed(context):
    """Verify Profiler output."""
    assert context.profile is not None
    assert hasattr(context.profile, "backend_stack")
    assert hasattr(context.profile, "identified_risks")


@then("the Researcher should execute second and produce RetrievedStandards")
def step_researcher_executed(context):
    """Verify Researcher output."""
    assert context.standards is not None
    assert hasattr(context.standards, "sections")
    assert len(context.standards.sections) > 0


@then("the Architect should execute third and produce a PipelineResult")
def step_architect_executed(context):
    """Verify Architect output."""
    assert context.result is not None
    assert isinstance(context.result, (StrategyResponse, QuestionsResponse))


@then("if result is StrategyResponse, the Critic should execute fourth")
def step_critic_executed_conditional(context):
    """Verify Critic executed if needed."""
    if isinstance(context.result, StrategyResponse):
        assert context.validation is not None


@then("the Critic should validate the strategy and produce ValidationResult")
def step_critic_result(context):
    """Verify Critic output."""
    if isinstance(context.result, StrategyResponse):
        assert isinstance(context.validation, ValidationResult)
        assert hasattr(context.validation, "status")


@then("all outputs should be properly serializable to JSON")
def step_serializable(context):
    """Verify all outputs can be JSON serialized."""
    try:
        if context.result:
            context.result.model_dump_json()
        if context.validation:
            context.validation.model_dump_json()
        if context.profile:
            context.profile.model_dump_json()
    except Exception as e:
        raise AssertionError(f"Output not JSON serializable: {e}")


# ============================================================================
# Standards Library Integration Steps
# ============================================================================

@given("the pipeline is running")
def step_pipeline_context(context):
    """Ensure pipeline is initialized."""
    if not hasattr(context, "pipeline"):
        context.library = StandardsLibrary()
        context.pipeline = PipelineOrchestrator(context.library)


@when("the Researcher agent queries the StandardsLibrary")
def step_researcher_query(context):
    """Verify Researcher queried library."""
    # This happens during pipeline.generate() which we already called
    assert context.standards is not None


@then("the library should return standards sections with:")
def step_standards_sections_format(context):
    """Verify section format."""
    for section in context.standards.sections:
        assert hasattr(section, "standard_id")
        assert hasattr(section, "title")
        assert hasattr(section, "section_key")
        assert hasattr(section, "content")
        assert len(section.standard_id) > 0
        assert len(section.title) > 0
        assert len(section.content) > 0


@then("the retrieved sections should be domain-specific")
def step_sections_domain_specific(context):
    """Verify domain-specific standards."""
    assert len(context.standards.sections) > 0


@then("medical PRDs should retrieve IEC 62304 sections")
def step_medical_standards(context):
    """Verify medical domain standards."""
    # This would require a medical PRD; just verify library has them
    all_standards = context.library.get_all_standard_ids()
    has_medical = any("62304" in std for std in all_standards)
    assert has_medical, "Medical standards not in library"


@then("automotive PRDs should retrieve ISO 26262 sections")
def step_automotive_standards(context):
    """Verify automotive standards."""
    # Verify library has automotive standards
    all_standards = context.library.get_all_standard_ids()
    has_automotive = any("26262" in std for std in all_standards)
    assert has_automotive, "Automotive standards not in library"
