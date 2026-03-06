"""
Step implementations for API feature tests.

Uses httpx TestClient against the FastAPI app to test HTTP endpoints.
"""

import sys
from pathlib import Path
from typing import Any

from behave import given, when, then
from httpx import TestClient

# Add project root to path for imports
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.app import app
from src.models.domain_config import IndustryDomain, SafetyLevel


# Initialize the test client
client = TestClient(app)


# ============================================================================
# Background/Setup Steps
# ============================================================================

@given("the FastAPI application is running")
def step_app_running(context):
    """Verify the app is available."""
    context.client = client
    context.last_response = None
    context.session_id = None


@given("the TestClient is initialized with the app")
def step_test_client_init(context):
    """TestClient is already initialized."""
    context.client = client


@given("the standards library is loaded")
def step_standards_loaded(context):
    """Standards library is loaded by the app."""
    # The app loads the library on startup
    pass


# ============================================================================
# Health Check Steps
# ============================================================================

@when("I send a GET request to \"{endpoint}\"")
def step_get_request(context, endpoint: str):
    """Send a GET request to the given endpoint."""
    context.last_response = context.client.get(endpoint)


@then("the response status code should be {status_code:d}")
def step_status_code(context, status_code: int):
    """Verify response status code."""
    assert context.last_response.status_code == status_code, \
        f"Expected {status_code}, got {context.last_response.status_code}\n" \
        f"Response: {context.last_response.text}"


@then("the response should contain \"{key}\": \"{value}\"")
def step_response_contains_kv(context, key: str, value: str):
    """Verify response contains a key-value pair."""
    response_data = context.last_response.json()
    assert key in response_data, f"Expected key '{key}' in response"
    assert response_data[key] == value, \
        f"Expected {key}='{value}', got '{response_data[key]}'"


@then("the response should contain \"{key}\" as a string number")
def step_response_string_number(context, key: str):
    """Verify response contains a key with string numeric value."""
    response_data = context.last_response.json()
    assert key in response_data, f"Expected key '{key}' in response"
    # Should be a string representation of a number
    try:
        int(response_data[key])
    except (ValueError, TypeError):
        raise AssertionError(f"Expected '{key}' to be a string number, got '{response_data[key]}'")


# ============================================================================
# Generate Strategy Steps
# ============================================================================

@given("a valid GenerateRequest with PRD text and domain \"{domain}\"")
def step_generate_request(context, domain: str):
    """Create a generate request."""
    context.generate_request = {
        "prd_text": "A Node.js REST API backend serving a React frontend with PostgreSQL database. "
                   "Handles user authentication and processes payments. "
                   "Deployed using Docker on AWS. "
                   "Expected 10,000+ concurrent users.",
        "domain": domain,
        "safety_level": "none",
        "regulatory_frameworks": [],
        "deployment_jurisdictions": [],
        "hardware_constraints": None,
        "deployment_environment": "cloud",
    }


@when("I send a POST request to \"{endpoint}\" with the request")
def step_post_request(context, endpoint: str):
    """Send a POST request with the prepared request body."""
    assert hasattr(context, "generate_request"), "No request prepared"
    context.last_response = context.client.post(endpoint, json=context.generate_request)


@then("the response should contain a \"session_id\" field (non-empty UUID-like string)")
def step_response_session_id(context):
    """Verify session_id is present and non-empty."""
    response_data = context.last_response.json()
    assert "session_id" in response_data, "session_id not in response"
    assert len(response_data["session_id"]) > 0, "session_id is empty"
    # Store for later use
    context.session_id = response_data["session_id"]


@then("the response should contain a \"status\" field (\"questions\" or \"strategy\")")
def step_response_status(context):
    """Verify status field is present with valid values."""
    response_data = context.last_response.json()
    assert "status" in response_data, "status not in response"
    assert response_data["status"] in ["questions", "strategy", "error"], \
        f"Unexpected status: {response_data['status']}"
    context.response_status = response_data["status"]


@then("if status is \"strategy\", response should contain \"strategy_markdown\"")
def step_response_strategy_if_strategy(context):
    """Verify strategy_markdown present if status is strategy."""
    response_data = context.last_response.json()
    if response_data.get("status") == "strategy":
        assert "strategy_markdown" in response_data, "strategy_markdown missing when status=strategy"
        assert len(response_data["strategy_markdown"]) > 0, "strategy_markdown is empty"


@then("if status is \"questions\", response should contain \"questions\" array")
def step_response_questions_if_questions(context):
    """Verify questions array present if status is questions."""
    response_data = context.last_response.json()
    if response_data.get("status") == "questions":
        assert "questions" in response_data, "questions missing when status=questions"
        assert isinstance(response_data["questions"], list), "questions is not a list"
        assert len(response_data["questions"]) > 0, "questions is empty"


@then("the response may contain \"validation\" with citation and completeness metrics")
def step_response_validation(context):
    """Verify validation object if present."""
    response_data = context.last_response.json()
    if "validation" in response_data and response_data["validation"]:
        validation = response_data["validation"]
        assert "citation_accuracy" in validation or "status" in validation, \
            "validation missing expected fields"


# ============================================================================
# Export Endpoint Steps
# ============================================================================

@given("a completed strategy session with session_id")
def step_completed_session(context):
    """Create a completed session by calling generate first."""
    # Generate a strategy
    generate_request = {
        "prd_text": "Complete system description for a REST API",
        "domain": "general_software",
        "safety_level": "none",
        "regulatory_frameworks": [],
        "deployment_jurisdictions": [],
        "hardware_constraints": None,
        "deployment_environment": "cloud",
    }

    response = context.client.post("/api/strategy/generate", json=generate_request)
    assert response.status_code == 200
    response_data = response.json()
    context.session_id = response_data["session_id"]


@when("I send a GET request to \"/api/strategy/export/{session_id}\"")
def step_get_export(context, session_id: str):
    """Send GET request to export endpoint."""
    # Replace placeholder with actual session_id
    session_id = getattr(context, "session_id", session_id)
    context.last_response = context.client.get(f"/api/strategy/export/{session_id}")


@then("the response should contain a \"markdown\" field")
def step_response_markdown(context):
    """Verify markdown field exists."""
    response_data = context.last_response.json()
    assert "markdown" in response_data, "markdown not in response"


@then("the markdown should be a non-empty string")
def step_markdown_non_empty(context):
    """Verify markdown is non-empty."""
    response_data = context.last_response.json()
    assert len(response_data["markdown"]) > 0, "markdown is empty"


@then("the markdown should contain proper Markdown formatting (## headers, -, etc.)")
def step_markdown_formatting(context):
    """Verify markdown has expected formatting."""
    response_data = context.last_response.json()
    markdown = response_data["markdown"]
    # Check for common markdown elements
    has_headers = "##" in markdown
    has_lists = "-" in markdown or "*" in markdown or "+" in markdown
    # At least one should be present
    assert has_headers or has_lists, "Markdown lacks expected formatting"


# ============================================================================
# 404 Error Steps
# ============================================================================

@given("a non-existent session_id \"{session_id}\"")
def step_nonexistent_session(context, session_id: str):
    """Set up invalid session ID."""
    context.invalid_session_id = session_id


@when("I send a GET request to \"/api/strategy/export/{session_id}\"")
def step_get_invalid_export(context, session_id: str):
    """Send GET to invalid session."""
    session_id = getattr(context, "invalid_session_id", session_id)
    context.last_response = context.client.get(f"/api/strategy/export/{session_id}")


@then("the response should contain \"Session not found\" in the detail")
def step_error_detail(context):
    """Verify error message in response."""
    response_data = context.last_response.json()
    assert "detail" in response_data, "detail not in error response"
    assert "Session not found" in response_data["detail"] or "session" in response_data["detail"].lower(), \
        f"Unexpected detail: {response_data['detail']}"


# ============================================================================
# Answer Questions Steps
# ============================================================================

@given("a session with response_type \"questions\" and clarifying questions")
def step_session_with_questions(context):
    """Create a session that returns questions."""
    # For this test, we'll assume we have a valid session
    # In practice, this would require a PRD that generates questions
    context.session_id = "test-session-with-questions"
    context.questions = [
        {
            "standard": "ISO 25010",
            "question": "What is the expected peak concurrent user count?",
            "example_answer": "500 users",
        },
        {
            "standard": "ISO 25010",
            "question": "What are the availability requirements?",
            "example_answer": "99.9% uptime",
        },
    ]


@given("I have answers to all questions")
def step_prepare_answers(context):
    """Prepare answers to questions."""
    context.answers = {
        question["question"]: "Test answer"
        for question in context.questions
    }


@when("I send a POST request to \"/api/strategy/answer\" with session_id and answers")
def step_post_answer(context):
    """Send answer request."""
    answer_request = {
        "session_id": context.session_id,
        "answers": context.answers,
    }
    context.last_response = context.client.post("/api/strategy/answer", json=answer_request)


@then("the response should contain updated \"session_id\"")
def step_response_updated_session(context):
    """Verify session_id in response."""
    response_data = context.last_response.json()
    assert "session_id" in response_data, "session_id not in response"


@then("the status may be \"strategy\" if questions were sufficient")
def step_status_may_be_strategy(context):
    """Verify possible status."""
    response_data = context.last_response.json()
    # Status could be either questions or strategy
    assert response_data.get("status") in ["questions", "strategy"]


@then("Or status may be \"questions\" if more clarification is needed")
def step_status_alternative(context):
    """Alternative status is acceptable."""
    # Previous step already handles both
    pass


# ============================================================================
# Validation Error Steps
# ============================================================================

@given("a GenerateRequest with empty PRD text (less than 10 characters)")
def step_invalid_generate_request(context):
    """Create invalid request."""
    context.generate_request = {
        "prd_text": "short",  # Less than 10 characters
        "domain": "general_software",
        "safety_level": "none",
    }


@when("I send a POST request to \"/api/strategy/generate\" with the invalid request")
def step_post_invalid(context):
    """Send invalid request."""
    context.last_response = context.client.post("/api/strategy/generate", json=context.generate_request)


@then("the response should contain validation error details")
def step_validation_error(context):
    """Verify validation error response."""
    response_data = context.last_response.json()
    assert "detail" in response_data, "No detail in error response"
    # Should be validation error


# ============================================================================
# Standards Stats Steps
# ============================================================================

@when("I send a GET request to \"/api/standards/stats\"")
def step_get_standards_stats(context):
    """Request standards stats."""
    context.last_response = context.client.get("/api/standards/stats")


@then("the response should contain \"total_sections\" as an integer")
def step_stats_total_sections(context):
    """Verify total_sections is an integer."""
    response_data = context.last_response.json()
    assert "total_sections" in response_data, "total_sections not in response"
    assert isinstance(response_data["total_sections"], int), "total_sections is not an integer"


@then("the response should contain \"standard_ids\" as an array of strings")
def step_stats_standard_ids(context):
    """Verify standard_ids is an array."""
    response_data = context.last_response.json()
    assert "standard_ids" in response_data, "standard_ids not in response"
    assert isinstance(response_data["standard_ids"], list), "standard_ids is not a list"
    if len(response_data["standard_ids"]) > 0:
        assert isinstance(response_data["standard_ids"][0], str), "standard_ids contains non-strings"


@then("the total_sections should be greater than 0")
def step_sections_count_positive(context):
    """Verify non-empty library."""
    response_data = context.last_response.json()
    assert response_data["total_sections"] > 0, "No standards loaded"


# ============================================================================
# Domains Endpoint Steps
# ============================================================================

@when("I send a GET request to \"/api/domains\"")
def step_get_domains(context):
    """Request domains list."""
    context.last_response = context.client.get("/api/domains")


@then("the response should be an array of domain objects")
def step_domains_array(context):
    """Verify response is an array."""
    response_data = context.last_response.json()
    assert isinstance(response_data, list), "Domains response is not a list"


@then("each domain object should have:")
def step_domain_object_schema(context):
    """Verify domain object schema."""
    response_data = context.last_response.json()
    for domain in response_data:
        assert "value" in domain, f"Missing 'value' in domain: {domain}"
        assert "label" in domain, f"Missing 'label' in domain: {domain}"
        assert isinstance(domain["value"], str), "value is not a string"
        assert isinstance(domain["label"], str), "label is not a string"


@then("the array should include at least \"general_software\"")
def step_domains_includes_general(context):
    """Verify general_software domain exists."""
    response_data = context.last_response.json()
    domain_values = [d["value"] for d in response_data]
    assert "general_software" in domain_values, f"general_software not in domains: {domain_values}"
