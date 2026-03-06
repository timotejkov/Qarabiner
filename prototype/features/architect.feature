Feature: Architect Agent (Agent 3)
  Tests for the Architect agent that generates test strategies or clarifying questions.
  Agent 3 is the core reasoning engine that produces either a comprehensive strategy or identifies gaps.

  Background:
    Given the Architect agent is initialized
    And a mock LLM is configured for strategy generation

  Scenario: Generates complete strategy with all required sections
    Given a complete SystemProfile for a microservices REST API
    And retrieved standards for "general_software" domain
    And adequate context for test strategy generation
    When the Architect generates a strategy
    Then the response should have response_type="strategy"
    And the strategy_markdown should include "## Test Coverage Areas"
    And the strategy_markdown should include "## Unit Testing"
    And the strategy_markdown should include "## Integration Testing"
    And the strategy_markdown should include "## Security Testing"
    And the strategy_markdown should include "## Performance Testing"
    And the standards_cited should contain at least 3 standards
    And the domain_sections_included should list applicable domain-specific sections

  Scenario: Returns clarifying questions for vague PRD
    Given a minimal PRD with insufficient technical or operational details
    And retrieved standards that require additional context
    And the profile indicates missing critical information
    When the Architect attempts to generate a strategy
    Then the response should have response_type="questions"
    And the questions list should contain at least 2 clarifying questions
    Each question should have:
      | field              | requirement                                        |
      | standard           | the relevant standard requiring the info          |
      | question           | a specific question for the product owner         |
      | example_answer     | an example of a sufficient answer                 |
    And the gaps_summary should explain what information is needed

  Scenario: Incorporates answered questions into strategy
    Given a previous QuestionsResponse with 3 clarifying questions
    And user-provided answers to all clarifying questions
    When the Architect regenerates the strategy with answered_questions
    Then the response should have response_type="strategy"
    And the strategy_markdown should incorporate details from the answers
    And the strategy_markdown should reference the answered parameters
    And the citation accuracy should remain high (>0.85)
    And the structural_completeness should be 1.0

  Scenario: Adapts strategy to different deployment environments
    Given a SystemProfile for a web application
    And the domain is "general_software"
    And deployment_environment is "on-premise" vs "cloud"
    When the Architect generates strategies for each environment
    Then on-premise strategy should emphasize infrastructure testing
    And cloud strategy should emphasize cloud provider API testing
    And both should cite relevant deployment standards
    And security testing focus should differ appropriately

  Scenario: Reflects critic feedback in regenerated strategy
    Given a previous StrategyResponse that failed critic validation
    And critic_feedback identifying hallucinated standards and missing sections
    When the Architect regenerates with critic feedback
    Then the new strategy_markdown should address identified issues
    And hallucinated standards should be removed
    And missing required sections should be added
    And the validation result should improve
