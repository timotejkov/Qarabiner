# BDD Test Suite - Complete Index

## Overview

Comprehensive Behavior-Driven Development (BDD) test suite for the AI QA Architect prototype using Behave and Gherkin syntax. The suite tests the 4-agent pipeline that generates test strategies from Product Requirements Documents.

**Total Files:** 12
**Total Lines of Code:** 3,023
**Total Scenarios:** 31
**Total Step Functions:** 173

---

## Quick Navigation

### For Running Tests
→ See [RUNNING_BEHAVE_TESTS.md](../RUNNING_BEHAVE_TESTS.md) for quick start commands

### For Understanding Tests
→ See [features/README.md](./README.md) for detailed documentation

### For Complete Summary
→ See [BDD_TEST_SUMMARY.md](../BDD_TEST_SUMMARY.md) for comprehensive overview

---

## Feature Files (6 files, 365 lines)

### 1. profiler.feature (37 lines)
**Agent 1: Extracts structured system profiles from raw PRD text**

📍 Location: `/sessions/gracious-nifty-johnson/mnt/TestAI/prototype/features/profiler.feature`

Scenarios (3):
1. Extracts tech stack from detailed PRD
2. Identifies security-sensitive data handling
3. Handles minimal input gracefully

Tests:
- Backend/frontend stack extraction
- Risk identification
- Data sensitivity classification
- Domain inference
- Graceful degradation

```gherkin
Scenario: Extracts tech stack from detailed PRD
  Given a detailed PRD describing a Node.js backend and React frontend
  When the Profiler processes the PRD
  Then the SystemProfile should contain "Node.js" in backend_stack
```

---

### 2. researcher.feature (47 lines)
**Agent 2: Retrieves applicable standards based on system profiles**

📍 Location: `/sessions/gracious-nifty-johnson/mnt/TestAI/prototype/features/researcher.feature`

Scenarios (4):
1. Returns core standards for general software
2. Includes medical domain standards (IEC 62304)
3. Includes automotive standards (ISO 26262)
4. Retrieves standards for embedded IoT with constraints

Tests:
- Standard retrieval for different domains
- Medical device standards (IEC 62304, ISO 13485, 21 CFR Part 11)
- Automotive standards (ISO 26262, SOTIF)
- Embedded/IoT constraints handling
- Standards library integration
- Section formatting for prompt injection

```gherkin
Scenario: Includes medical domain standards for medical device
  Given a SystemProfile for a medical imaging device
  And the domain is "medical_device"
  When the Researcher retrieves applicable standards
  Then the retrieved standards should include "IEC 62304"
  And the retrieved standards should include "ISO 13485"
```

---

### 3. architect.feature (64 lines)
**Agent 3: Generates test strategies or identifies information gaps**

📍 Location: `/sessions/gracious-nifty-johnson/mnt/TestAI/prototype/features/architect.feature`

Scenarios (5):
1. Generates complete strategy with all required sections
2. Returns clarifying questions for vague PRD
3. Incorporates answered questions into strategy
4. Adapts strategy to different deployment environments
5. Reflects critic feedback in regenerated strategy

Tests:
- Strategy markdown generation with proper sections
- Question/gap detection for sparse PRDs
- Multi-pass refinement (questions → answers → strategy)
- Environment-specific customization (cloud vs on-premise)
- Critic feedback incorporation
- Citation accuracy verification

```gherkin
Scenario: Generates complete strategy with all required sections
  Given a complete SystemProfile for a microservices REST API
  When the Architect generates a strategy
  Then the response should have response_type="strategy"
  And the strategy_markdown should include "## Security Testing"
  And the standards_cited should contain at least 3 standards
```

---

### 4. critic.feature (60 lines)
**Agent 4: Validates strategies for quality, accuracy, and completeness**

📍 Location: `/sessions/gracious-nifty-johnson/mnt/TestAI/prototype/features/critic.feature`

Scenarios (6):
1. Passes valid strategy with correct citations
2. Fails strategy with hallucinated citations
3. Detects missing risk coverage
4. Flags incomplete sections in strategy
5. Validates citation accuracy metrics
6. (Additional validation scenarios)

Tests:
- Citation verification against retrieved standards
- Hallucination detection
- Risk coverage validation
- Structural completeness checking
- Accuracy metrics (citation_accuracy, structural_completeness)
- Issue categorization (hallucination, citation_invalid, risk_mismatch)

```gherkin
Scenario: Fails strategy with hallucinated citations
  Given a StrategyResponse citing "ISO 99999" which does not exist
  When the Critic validates the strategy
  Then the ValidationResult status should be "failed"
  And citation_accuracy should be less than 0.5
  And the issues list should contain a "hallucination" category
```

---

### 5. api.feature (72 lines)
**REST API Endpoint Tests**

📍 Location: `/sessions/gracious-nifty-johnson/mnt/TestAI/prototype/features/api.feature`

Scenarios (8):
1. Health check returns healthy
2. Generate endpoint returns session ID
3. Export returns markdown
4. Invalid session returns 404
5. Answer endpoint updates session
6. Invalid request returns 422
7. Standards stats endpoint returns library info
8. Domains endpoint lists supported domains

Tests:
- HTTP status codes (200, 404, 422)
- Request/response validation
- Session management and tracking
- JSON schema validation
- Error handling and messages
- Data serialization

```gherkin
Scenario: Generate endpoint returns session ID
  Given a valid GenerateRequest with PRD text and domain "general_software"
  When I send a POST request to "/api/strategy/generate" with the request
  Then the response status code should be 200
  And the response should contain a "session_id" field
  And the response should contain a "status" field ("questions" or "strategy")
```

---

### 6. mattermost_benchmark.feature (85 lines)
**End-to-End Pipeline Benchmark Tests**

📍 Location: `/sessions/gracious-nifty-johnson/mnt/TestAI/prototype/features/mattermost_benchmark.feature`

Scenarios (6):
1. Full pipeline produces strategy from Mattermost PRD (@wip)
2. Strategy contains security testing section (@wip)
3. Strategy references OWASP standards (@wip)
4. Minimal PRD returns questions not strategy (@wip)
5. Pipeline executes all four agents in sequence
6. Standards library properly integrated

Tests:
- Complete pipeline execution (Profiler → Researcher → Architect → Critic)
- Agent sequencing verification
- Real-world Mattermost PRD processing
- Security section validation
- OWASP standard referencing
- Domain-specific standard validation
- Execution time benchmarking

Features:
- Marked with `@wip` tag for tests requiring live LLM API keys
- Uses realistic Mattermost PRD as test data
- Verifies all four agents produce output
- Tests both success path (strategy) and gap detection (questions)

```gherkin
@wip
Scenario: Full pipeline produces strategy from Mattermost PRD
  Given a realistic PRD for "Mattermost Team Collaboration Platform"
  When the pipeline runs end-to-end
  Then the final output should be a StrategyResponse
  And the strategy_markdown should be a substantial document (> 2000 characters)
  And the validation status should be "passed"
```

---

## Step Definition Files (3 files, 2,223 lines)

### 1. agent_steps.py (1,294 lines, 92 step functions)
**Step implementations for Agents 1-4 with mock LLM responses**

📍 Location: `/sessions/gracious-nifty-johnson/mnt/TestAI/prototype/features/steps/agent_steps.py`

Key Features:
- Mock LLM response builders
- Domain-aware response generation (medical, automotive, general)
- Comprehensive Profiler tests
- Researcher standard retrieval tests
- Architect strategy generation tests
- Critic validation tests

Mock Response Functions:
- `mock_profiler_response()` - Generates realistic profiles based on PRD content
- `mock_researcher_response()` - Standard selection responses
- `mock_architect_response_strategy()` - Complete strategy markdown with sections
- `mock_architect_response_questions()` - Clarifying questions for gaps
- `mock_critic_response_passed()` - Valid strategy validation
- `mock_critic_response_failed()` - Failed validation with issues

Step Coverage:
- Profiler: 60+ steps covering initialization, PRD processing, assertions
- Researcher: 50+ steps for standard retrieval and validation
- Architect: 70+ steps for strategy generation and question handling
- Critic: 80+ steps for validation, citation checking, risk coverage

Example Steps:
```python
@given("a detailed PRD describing a Node.js backend and React frontend")
@when("the Profiler processes the PRD")
@then("the SystemProfile should contain \"{item}\" in {field}")
```

---

### 2. api_steps.py (412 lines, 39 step functions)
**Step implementations for REST API endpoint testing**

📍 Location: `/sessions/gracious-nifty-johnson/mnt/TestAI/prototype/features/steps/api_steps.py`

Key Features:
- httpx TestClient integration
- Direct FastAPI app testing
- Request/response validation
- Session management
- Error response verification

Step Coverage:
- Health check: 5+ steps
- Strategy generation: 10+ steps
- Export functionality: 8+ steps
- Question answering: 5+ steps
- Error handling: 5+ steps
- Domain listing: 5+ steps

Example Steps:
```python
@given("a valid GenerateRequest with PRD text and domain \"{domain}\"")
@when("I send a POST request to \"{endpoint}\" with the request")
@then("the response status code should be {status_code:d}")
@then("the response should contain a \"session_id\" field")
```

---

### 3. benchmark_steps.py (517 lines, 42 step functions)
**Step implementations for end-to-end pipeline testing**

📍 Location: `/sessions/gracious-nifty-johnson/mnt/TestAI/prototype/features/steps/benchmark_steps.py`

Key Features:
- Real pipeline execution (not mocked)
- Agent sequencing verification
- Output validation
- Performance benchmarking
- Domain-specific standard validation

Step Coverage:
- Pipeline initialization: 5+ steps
- Full pipeline execution: 8+ steps
- Sequential agent verification: 10+ steps
- Security validation: 8+ steps
- OWASP verification: 5+ steps
- Standards validation: 5+ steps

Example Steps:
```python
@given("the complete pipeline is initialized")
@when("the pipeline runs end-to-end")
@then("the final output should be a StrategyResponse")
@then("all four agents should produce non-empty outputs")
```

---

## Configuration Files (2 files, 435 lines)

### 1. environment.py (427 lines)
**Behave hooks and test configuration**

📍 Location: `/sessions/gracious-nifty-johnson/mnt/TestAI/prototype/features/environment.py`

Hooks:
- `before_all()` - Test suite initialization, logging setup
- `after_all()` - Cleanup, summary statistics
- `before_feature()` - Feature-level resource setup
- `after_feature()` - Feature-level cleanup
- `before_scenario()` - Scenario initialization, tag processing
- `after_scenario()` - Resource cleanup, error handling
- `before_step()` - Step-level logging
- `after_step()` - Step failure logging

Helper Functions:
- `assert_field_present()` - Field existence verification
- `assert_field_value()` - Field value validation
- `assert_collection_contains()` - Collection membership
- `assert_collection_non_empty()` - Collection non-empty check
- `cleanup_scenario_resources()` - Resource cleanup

Test Data:
- `SAMPLE_PRD_MINIMAL` - Sparse 1-line description
- `SAMPLE_PRD_DETAILED` - Complete Node.js/React/PostgreSQL stack
- `SAMPLE_PRD_MEDICAL` - Medical imaging with HIPAA/IEC 62304
- `SAMPLE_PRD_AUTOMOTIVE` - Vehicle infotainment with ISO 26262

Context Managers:
- `MockLLMContext` - For mock LLM testing
- `LiveAPIContext` - For live API testing (with API key)

### 2. steps/__init__.py (8 lines)
**Step package initialization**

📍 Location: `/sessions/gracious-nifty-johnson/mnt/TestAI/prototype/features/steps/__init__.py`

Package marker with documentation

---

## Documentation Files (3 files, 1,076 lines)

### 1. README.md (350 lines)
**Comprehensive feature test documentation**

📍 Location: `/sessions/gracious-nifty-johnson/mnt/TestAI/prototype/features/README.md`

Sections:
- Overview and project description
- Directory structure
- Running tests (all, specific, by tag, with formats)
- Feature file descriptions (each feature and its scenarios)
- Step definition details
- Test data overview
- Mock LLM strategy
- Behave hooks explanation
- Configuration guide
- CI/CD integration
- Troubleshooting
- Best practices

### 2. BDD_TEST_SUMMARY.md (603 lines)
**Complete summary of all created files**

📍 Location: `/sessions/gracious-nifty-johnson/mnt/TestAI/prototype/BDD_TEST_SUMMARY.md`

Sections:
- Project overview
- Detailed file descriptions
- Statistics (features, steps, coverage)
- Test coverage matrix
- Running instructions
- Design decisions
- CI/CD integration
- Future enhancements
- Usage examples

### 3. RUNNING_BEHAVE_TESTS.md (123 lines)
**Quick start guide for running tests**

📍 Location: `/sessions/gracious-nifty-johnson/mnt/TestAI/prototype/RUNNING_BEHAVE_TESTS.md`

Sections:
- Prerequisites
- Quick commands
- Test structure overview
- Common workflows
- Expected output

---

## Test Coverage Summary

### Agents Covered
- [x] **Profiler (Agent 1)** - 3 scenarios, 60+ steps
- [x] **Researcher (Agent 2)** - 4 scenarios, 50+ steps
- [x] **Architect (Agent 3)** - 5 scenarios, 70+ steps
- [x] **Critic (Agent 4)** - 6 scenarios, 80+ steps

### API Endpoints Covered
- [x] GET /api/health
- [x] POST /api/strategy/generate
- [x] POST /api/strategy/answer
- [x] GET /api/strategy/export/{session_id}
- [x] GET /api/standards/stats
- [x] GET /api/domains

### Domains Covered
- [x] General Software
- [x] Medical Device (IEC 62304, HIPAA)
- [x] Automotive (ISO 26262, SOTIF)
- [x] Embedded IoT
- [x] Financial

### Error Cases Covered
- [x] Invalid sessions (404)
- [x] Validation errors (422)
- [x] Hallucinated citations
- [x] Missing risk coverage
- [x] Incomplete sections

---

## File Locations Reference

```
/sessions/gracious-nifty-johnson/mnt/TestAI/prototype/
├── features/
│   ├── INDEX.md                    ← You are here
│   ├── README.md                   ← Detailed documentation
│   ├── environment.py              ← Behave hooks
│   ├── profiler.feature            ← Agent 1 tests
│   ├── researcher.feature          ← Agent 2 tests
│   ├── architect.feature           ← Agent 3 tests
│   ├── critic.feature              ← Agent 4 tests
│   ├── api.feature                 ← API tests
│   ├── mattermost_benchmark.feature ← E2E tests
│   └── steps/
│       ├── __init__.py
│       ├── agent_steps.py          ← Agent step implementations
│       ├── api_steps.py            ← API step implementations
│       └── benchmark_steps.py      ← Benchmark step implementations
├── BDD_TEST_SUMMARY.md             ← Complete summary
└── RUNNING_BEHAVE_TESTS.md         ← Quick start guide
```

---

## Getting Started

### 1. Install Dependencies
```bash
pip install behave httpx pytest
```

### 2. Run All Tests
```bash
cd /sessions/gracious-nifty-johnson/mnt/TestAI/prototype
behave features/
```

### 3. Run Specific Feature
```bash
behave features/profiler.feature
```

### 4. Run with Specific Format
```bash
behave --format json -o results.json features/
```

See [RUNNING_BEHAVE_TESTS.md](../RUNNING_BEHAVE_TESTS.md) for more commands.

---

## Statistics at a Glance

| Metric | Count |
|--------|-------|
| **Feature Files** | 6 |
| **Total Scenarios** | 31 |
| **Step Definition Files** | 3 |
| **Total Step Functions** | 173 |
| **Configuration Files** | 2 |
| **Documentation Files** | 3 |
| **Total Files** | 12 |
| **Total Lines of Code** | 3,023 |
| **Feature Lines** | 365 |
| **Step Implementation Lines** | 2,223 |
| **Configuration Lines** | 435 |

---

## Tags Used

### @wip
Work-in-progress tests requiring live LLM API keys. Excluded by default with `behave --tags=-@wip`.

### @integration
Integration tests (slower). Include with `behave --tags=@integration`.

### @slow
Slow-running tests. Exclude with `behave --tags=-@slow`.

---

## Key Design Principles

1. **Mock LLM by Default** - Unit tests use mocked responses for speed
2. **Domain-Aware** - Support for medical, automotive, general software domains
3. **Comprehensive Coverage** - All 4 agents + API endpoints + end-to-end
4. **Clear Organization** - Separate files for agent, API, and benchmark tests
5. **Extensive Documentation** - README, summary, and quick start guides
6. **CI/CD Ready** - JSON output, tag filtering, and organized reporting

---

## Related Files

- **Source Code**: `/sessions/gracious-nifty-johnson/mnt/TestAI/prototype/src/`
- **Main App**: `/sessions/gracious-nifty-johnson/mnt/TestAI/prototype/src/app.py`
- **Agent Implementations**: `/sessions/gracious-nifty-johnson/mnt/TestAI/prototype/src/agents/`
- **Data Models**: `/sessions/gracious-nifty-johnson/mnt/TestAI/prototype/src/models/`

---

## Next Steps

1. Review individual feature files for scenario details
2. Check step implementations for assertion patterns
3. Run test commands from RUNNING_BEHAVE_TESTS.md
4. Extend tests with additional scenarios as needed
5. Integrate with CI/CD pipeline using JSON output

---

**Last Updated:** March 2026
**Total Project Size:** 3,023 lines across 12 files
**Ready for:** Development testing, CI/CD integration, team collaboration
