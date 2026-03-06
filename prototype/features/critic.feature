Feature: Critic Agent (Agent 4)
  Tests for the Critic agent that validates generated strategies before delivery.
  Agent 4 is the quality gate ensuring no hallucinations or invalid citations reach the user.

  Background:
    Given the Critic agent is initialized
    And a mock LLM is configured for validation
    And retrieved standards are available for citation checking

  Scenario: Passes valid strategy with correct citations
    Given a StrategyResponse with well-cited standards
    And all citations match available standards from the Researcher
    And all required sections are present
    And no hallucinations are detected in the markdown
    When the Critic validates the strategy
    Then the ValidationResult status should be "passed"
    And citation_accuracy should be 1.0 (all citations valid)
    And structural_completeness should be 1.0 (all sections present)
    And the issues list should be empty
    And the summary should indicate a passing validation

  Scenario: Fails strategy with hallucinated citations
    Given a StrategyResponse citing "ISO 99999" which does not exist
    And citing "ACME Standard v7.2" which is not in retrieved standards
    And referencing sections not available in the Researcher's results
    When the Critic validates the strategy
    Then the ValidationResult status should be "failed"
    And citation_accuracy should be less than 0.5
    And the issues list should contain a "hallucination" or "citation_invalid" category
    And each issue should specify the invalid citation and location
    And the summary should explain the hallucination problem

  Scenario: Detects missing risk coverage
    Given a SystemProfile with identified_risks including "SQL injection" and "authentication bypass"
    And a StrategyResponse that only covers SQL injection testing
    When the Critic validates strategy completeness against the profile
    Then the ValidationResult status should be "failed"
    And the issues list should contain a "risk_mismatch" or "missing_section" issue
    And the issue description should mention "authentication bypass" is not covered
    And the severity should be "high" for critical missing risks
    And the structural_completeness should be less than 1.0

  Scenario: Flags incomplete sections in strategy
    Given a StrategyResponse missing required test strategy section headers
    And missing coverage for a domain-specific area (e.g., security for financial systems)
    When the Critic validates the strategy
    Then the ValidationResult status should be "failed"
    And the issues should report "missing_section" with high severity
    And the structural_completeness metric should quantify the gaps
    And the summary should suggest which sections need to be added

  Scenario: Validates citation accuracy metrics
    Given a StrategyResponse with 10 total citations
    And 8 citations correctly referencing available standards
    And 2 citations that are partially correct or ambiguous
    When the Critic validates citation accuracy
    Then the citation_accuracy should be 0.8 (8 out of 10)
    And each issue should be categorized appropriately
    And the summary should indicate an 80% accuracy rate
    And the validation status should depend on accuracy threshold (e.g., fails if < 0.85)
