Feature: End-to-End Pipeline Benchmark
  Tests the full AI QA Architect pipeline using real Mattermost PRD.
  These are integration tests that verify the complete pipeline flow.

  Background:
    Given the complete pipeline is initialized (Profiler → Researcher → Architect → Critic)
    And a Mattermost-style PRD is prepared as test data
    And real LLM APIs would be called (marked @wip when API key available)

  @wip
  Scenario: Full pipeline produces strategy from Mattermost PRD
    Given a realistic PRD for "Mattermost Team Collaboration Platform"
    Describing a Node.js backend, React frontend, and PostgreSQL database
    And the domain is "general_software"
    And the safety level is "none"
    When the pipeline runs end-to-end (Profiler → Researcher → Architect → Critic)
    Then the final output should be a StrategyResponse (not QuestionsResponse)
    And the strategy_markdown should be a substantial document (> 2000 characters)
    And the validation status should be "passed"
    And the pipeline should execute within reasonable time (< 60 seconds for mock)
    And all four agents should produce non-empty outputs

  @wip
  Scenario: Strategy contains security testing section
    Given the full pipeline is executed on the Mattermost PRD
    When the Architect agent generates the strategy
    Then the strategy_markdown should contain a section on "Security Testing"
    Or a section on "Application Security"
    Or a section on "OWASP" compliance
    And this section should include specific test cases for:
      | area                    |
      | authentication          |
      | authorization           |
      | input validation        |
      | injection attacks       |
    And the section should reference security standards

  @wip
  Scenario: Strategy references OWASP standards
    Given the Mattermost PRD processed through the full pipeline
    When the Architect generates the strategy
    Then the strategy_markdown should reference "OWASP Top 10"
    Or "OWASP Testing Guide"
    Or specific OWASP vulnerabilities (e.g., "A01:2021 - Broken Access Control")
    And the standards_cited list should include at least one OWASP standard
    And the Critic should validate these citations as correct

  @wip
  Scenario: Minimal PRD returns questions not strategy
    Given a very brief PRD with only "Collaboration platform" description
    And insufficient technical and operational details
    And the domain is "general_software"
    When the pipeline runs end-to-end
    Then the response should be a QuestionsResponse (not StrategyResponse)
    And the questions list should contain at least 2 questions
    Each question should ask about:
      | missing_info                           |
      | technology stack specifics             |
      | scalability requirements               |
      | security and authentication approach   |
      | deployment and infrastructure details  |
    And the gaps_summary should explain the information gaps

  Scenario: Pipeline executes all four agents in sequence
    Given a typical PRD input
    When the pipeline runs
    Then the Profiler should execute first and produce a SystemProfile
    And the Researcher should execute second and produce RetrievedStandards
    And the Architect should execute third and produce a PipelineResult
    And if result is StrategyResponse, the Critic should execute fourth
    And the Critic should validate the strategy and produce ValidationResult
    And all outputs should be properly serializable to JSON

  Scenario: Standards library is properly integrated
    Given the pipeline is running
    When the Researcher agent queries the StandardsLibrary
    Then the library should return standards sections with:
      | field        | requirement                        |
      | standard_id  | non-empty (e.g., "ISO 25010")     |
      | title        | descriptive title                  |
      | section_key  | section identifier                 |
      | content      | substantive standard guidance      |
    And the retrieved sections should be domain-specific
    And medical PRDs should retrieve IEC 62304 sections
    And automotive PRDs should retrieve ISO 26262 sections
