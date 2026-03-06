Feature: Profiler Agent (Agent 1)
  Tests for the Profiler agent that extracts structured system profiles from raw PRD text.
  Agent 1 transforms unstructured product requirements into a SystemProfile data model.

  Background:
    Given the Profiler agent is initialized
    And a mock LLM is configured to return structured responses

  Scenario: Extracts tech stack from detailed PRD
    Given a detailed PRD describing a Node.js backend and React frontend with PostgreSQL
    And the domain is "general_software"
    And the safety level is "none"
    When the Profiler processes the PRD
    Then the SystemProfile should contain "Node.js" in backend_stack
    And the SystemProfile should contain "React" in frontend_stack
    And the SystemProfile should contain "PostgreSQL" in databases
    And the SystemProfile architecture_pattern should be "microservices" or "monolith"

  Scenario: Identifies security-sensitive data handling
    Given a PRD mentioning "user authentication", "payment processing", and "PII storage"
    And the domain is "financial"
    And the safety level is "high"
    When the Profiler processes the PRD
    Then the SystemProfile data_sensitivity should be "confidential" or "restricted"
    And the SystemProfile should contain at least one security-related risk in identified_risks
    And the SystemProfile data_types_handled should include "PII" or "financial"
    And the SystemProfile should identify "payment processing" as an integration point

  Scenario: Handles minimal input gracefully
    Given a very brief PRD with minimal technical details
    And the domain is "general_software"
    And the safety level is "none"
    When the Profiler processes the PRD
    Then the SystemProfile should be created without errors
    And the SystemProfile architecture_pattern should default to "unknown"
    And the SystemProfile should have an empty or default summary
    And the SystemProfile backend_stack should be empty or contain reasonable defaults
