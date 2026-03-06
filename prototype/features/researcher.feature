Feature: Researcher Agent (Agent 2)
  Tests for the Researcher agent that retrieves relevant standards based on system profile.
  Agent 2 bridges the gap between technical profiles and applicable regulatory/quality standards.

  Background:
    Given the Researcher agent is initialized with a StandardsLibrary
    And a mock LLM is configured to return standard selection decisions

  Scenario: Returns core standards for general software
    Given a SystemProfile for a general Node.js REST API application
    And the domain is "general_software"
    And the safety level is "none"
    When the Researcher retrieves applicable standards
    Then the retrieved standards should include "ISO 25010" for software quality
    And the retrieved standards should include "OWASP Top 10" for security
    And the retrieved standards should include "ISO/IEC/IEEE 29119" for testing
    And the standard sections should be formatted with standard_id, title, and content

  Scenario: Includes medical domain standards for medical device
    Given a SystemProfile for a medical imaging device
    And the domain is "medical_device"
    And the safety level is "high"
    When the Researcher retrieves applicable standards
    Then the retrieved standards should include "IEC 62304" for medical device software
    And the retrieved standards should include "ISO 13485" for medical device quality
    And the retrieved standards should include "21 CFR Part 11" for FDA compliance
    And the standard sections should be prioritized by domain relevance

  Scenario: Includes automotive standards for automotive domain
    Given a SystemProfile for an automotive infotainment system
    And the domain is "automotive"
    And the safety level is "asil_b"
    When the Researcher retrieves applicable standards
    Then the retrieved standards should include "ISO 26262" for functional safety
    And the retrieved standards should include "SOTIF" for intended functionality
    And the retrieved standards should include "ISO 26262 ASIL B" severity level
    And the standard sections should address both safety and security concerns
    And the total number of retrieved sections should not exceed 25

  Scenario: Retrieves standards for embedded IoT with hardware constraints
    Given a SystemProfile for an embedded IoT device with "32KB RAM, RTOS" constraints
    And the domain is "embedded_iot"
    And hardware constraints are specified
    When the Researcher retrieves applicable standards
    Then the retrieved standards should include resource-constrained testing approaches
    And the standards should address real-time systems testing
    And the standard sections should be properly formatted for prompt injection
