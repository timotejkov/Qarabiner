Feature: REST API Endpoints
  Tests for the FastAPI application endpoints.
  Validates HTTP contract, request/response models, and error handling.

  Background:
    Given the FastAPI application is running
    And the TestClient is initialized with the app
    And the standards library is loaded

  Scenario: Health check returns healthy
    When I send a GET request to "/api/health"
    Then the response status code should be 200
    And the response should contain "status": "healthy"
    And the response should contain "version": "0.1.0"
    And the response should contain "standards_loaded" as a string number

  Scenario: Generate endpoint returns session ID
    Given a valid GenerateRequest with PRD text and domain "general_software"
    When I send a POST request to "/api/strategy/generate" with the request
    Then the response status code should be 200
    And the response should contain a "session_id" field (non-empty UUID-like string)
    And the response should contain a "status" field ("questions" or "strategy")
    And if status is "strategy", response should contain "strategy_markdown"
    And if status is "questions", response should contain "questions" array
    And the response may contain "validation" with citation and completeness metrics

  Scenario: Export returns markdown
    Given a completed strategy session with session_id
    When I send a GET request to "/api/strategy/export/{session_id}"
    Then the response status code should be 200
    And the response should contain a "markdown" field
    And the markdown should be a non-empty string
    And the markdown should contain proper Markdown formatting (## headers, -, etc.)

  Scenario: Invalid session returns 404
    Given a non-existent session_id "invalid-session-uuid-12345"
    When I send a GET request to "/api/strategy/export/{session_id}"
    Then the response status code should be 404
    And the response should contain "Session not found" in the detail

  Scenario: Answer endpoint updates session with answers
    Given a session with response_type "questions" and clarifying questions
    And I have answers to all questions
    When I send a POST request to "/api/strategy/answer" with session_id and answers
    Then the response status code should be 200
    And the response should contain updated "session_id"
    And the response should contain a "status" field
    And the status may be "strategy" if questions were sufficient
    Or status may be "questions" if more clarification is needed

  Scenario: Invalid request body returns 422
    Given a GenerateRequest with empty PRD text (less than 10 characters)
    When I send a POST request to "/api/strategy/generate" with the invalid request
    Then the response status code should be 422
    And the response should contain validation error details

  Scenario: Standards stats endpoint returns library info
    When I send a GET request to "/api/standards/stats"
    Then the response status code should be 200
    And the response should contain "total_sections" as an integer
    And the response should contain "standard_ids" as an array of strings
    And the total_sections should be greater than 0

  Scenario: Domains endpoint lists supported domains
    When I send a GET request to "/api/domains"
    Then the response status code should be 200
    And the response should be an array of domain objects
    Each domain object should have:
      | field | requirement                                     |
      | value | domain name (e.g., "general_software")         |
      | label | human-readable label (e.g., "General Software") |
    And the array should include at least "general_software"
