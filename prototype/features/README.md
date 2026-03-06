# BDD Feature Tests for AI QA Architect

This directory contains Behavior-Driven Development (BDD) tests for the AI QA Architect prototype using Behave and Gherkin syntax.

## Overview

The feature files define test scenarios across the 4-agent pipeline:

1. **Profiler Agent** (`profiler.feature`) - Extracts system profiles from PRDs
2. **Researcher Agent** (`researcher.feature`) - Retrieves applicable standards
3. **Architect Agent** (`architect.feature`) - Generates test strategies
4. **Critic Agent** (`critic.feature`) - Validates strategies
5. **REST API** (`api.feature`) - Tests FastAPI endpoints
6. **End-to-End** (`mattermost_benchmark.feature`) - Full pipeline benchmarks

## Directory Structure

```
features/
├── README.md                          # This file
├── environment.py                     # Behave hooks and configuration
├── profiler.feature                   # Agent 1 feature tests
├── researcher.feature                 # Agent 2 feature tests
├── architect.feature                  # Agent 3 feature tests
├── critic.feature                     # Agent 4 feature tests
├── api.feature                        # REST API endpoint tests
├── mattermost_benchmark.feature       # End-to-end pipeline tests
└── steps/
    ├── __init__.py
    ├── agent_steps.py                 # Steps for Agents 1-4 (mock LLM)
    ├── api_steps.py                   # Steps for API endpoints (httpx TestClient)
    └── benchmark_steps.py             # Steps for end-to-end pipeline tests
```

## Running the Tests

### Prerequisites

Install Behave and dependencies:

```bash
pip install behave httpx pytest
```

### Run All Features

```bash
cd /sessions/gracious-nifty-johnson/mnt/TestAI/prototype
behave features/
```

### Run Specific Feature

```bash
behave features/profiler.feature
behave features/api.feature
```

### Run with Tags

```bash
# Run only integration tests
behave --tags=@integration

# Run only tests marked as work-in-progress
behave --tags=@wip

# Run excluding slow tests
behave --tags=-@slow
```

### Run with Verbose Output

```bash
behave -v features/
```

### Run with JSON Output (for CI/CD)

```bash
behave --format json -o test_results.json features/
```

## Feature Files

### profiler.feature

Tests for the Profiler agent (Agent 1) that extracts structured system profiles from raw PRD text.

**Scenarios:**
- Extracts tech stack from detailed PRD
- Identifies security-sensitive data handling
- Handles minimal input gracefully

**Key Testing:**
- Validates extraction of backend/frontend stacks
- Checks risk identification
- Tests graceful degradation with sparse input

### researcher.feature

Tests for the Researcher agent (Agent 2) that retrieves relevant standards based on system profiles.

**Scenarios:**
- Returns core standards for general software (ISO 25010, OWASP, IEEE 29119)
- Includes medical domain standards (IEC 62304) for medical devices
- Includes automotive standards (ISO 26262) for automotive domain
- Retrieves standards for embedded IoT with hardware constraints

**Key Testing:**
- Domain-specific standard retrieval
- Standards library integration
- Standard section formatting for prompt injection

### architect.feature

Tests for the Architect agent (Agent 3) that generates test strategies or identifies information gaps.

**Scenarios:**
- Generates complete strategy with all required sections
- Returns clarifying questions for vague PRDs
- Incorporates answered questions into strategy
- Adapts strategy to different deployment environments
- Reflects critic feedback in regenerated strategy

**Key Testing:**
- Strategy markdown generation
- Question/gap detection
- Multi-pass refinement (questions → answers → strategy)
- Environment-specific customization

### critic.feature

Tests for the Critic agent (Agent 4) that validates generated strategies for quality and accuracy.

**Scenarios:**
- Passes valid strategy with correct citations
- Fails strategy with hallucinated citations
- Detects missing risk coverage
- Flags incomplete sections
- Validates citation accuracy metrics

**Key Testing:**
- Citation verification against retrieved standards
- Hallucination detection
- Risk coverage validation
- Structural completeness checking

### api.feature

Tests for the REST API endpoints using httpx TestClient.

**Scenarios:**
- GET /api/health returns healthy status
- POST /api/strategy/generate returns session ID
- GET /api/strategy/export/{session_id} returns markdown
- GET /api/strategy/export/{invalid_session} returns 404
- POST /api/strategy/answer updates with answers
- Invalid requests return 422 validation errors
- GET /api/standards/stats returns library info
- GET /api/domains lists supported domains

**Key Testing:**
- HTTP status codes
- Request/response validation
- Session management
- Error handling

### mattermost_benchmark.feature

End-to-end tests for the full pipeline using a realistic Mattermost PRD.

**Scenarios:**
- Full pipeline produces strategy from Mattermost PRD
- Strategy contains security testing section
- Strategy references OWASP standards
- Minimal PRD returns questions not strategy
- Pipeline executes all four agents in sequence
- Standards library properly integrated

**Key Testing:**
- Complete pipeline execution
- Agent sequencing (Profiler → Researcher → Architect → Critic)
- Domain-specific standard retrieval
- Real-world PRD processing

**Notes:**
- Marked with `@wip` tag for tests requiring live LLM API keys
- Uses mocks by default for fast unit-level testing
- Verify execution time and output quality

## Step Definitions

### agent_steps.py

Implements steps for testing the four agents with mock LLM responses.

**Key Features:**
- Mock LLM response builders for realistic outputs
- Domain-specific response generation (medical, automotive, general software)
- Minimal mock setup to avoid API calls
- Comprehensive profile/standard/strategy assertions

**Example Mock Data:**
- Detailed REST API profiles
- Medical device with healthcare standards
- Automotive with functional safety standards
- Minimal profiles with sparse input

### api_steps.py

Implements steps for testing REST API endpoints using httpx TestClient.

**Key Features:**
- Direct HTTP testing against FastAPI app
- Request/response validation
- Session management testing
- Error response verification

**Example Tests:**
- Health check validation
- Strategy generation workflow
- Export functionality
- Domain listing

### benchmark_steps.py

Implements steps for end-to-end pipeline testing.

**Key Features:**
- Full pipeline execution (all 4 agents)
- Sequential agent verification
- Output serialization testing
- Domain-specific standard validation

**Example Tests:**
- Mattermost PRD processing
- Security section validation
- OWASP standard referencing
- Minimal PRD handling

## Test Data

Sample PRDs are included in `environment.py`:

- **SAMPLE_PRD_MINIMAL** - Sparse 1-line description
- **SAMPLE_PRD_DETAILED** - Complete Node.js/React/PostgreSQL stack
- **SAMPLE_PRD_MEDICAL** - Medical imaging system with HIPAA/IEC 62304
- **SAMPLE_PRD_AUTOMOTIVE** - Vehicle infotainment with ISO 26262

## Mock LLM Strategy

The tests use mock LLM responses instead of real API calls for fast execution:

1. **Agent Steps** - Mock `_call_llm_json()` method with realistic responses
2. **API Steps** - TestClient calls real FastAPI which internally uses mocks
3. **Benchmark Steps** - Option to use real LLM via `@wip` tag and API key

```python
# Example mock setup in test steps
agent._call_llm_json = MagicMock(return_value=mock_response)
```

## Behave Hooks

The `environment.py` file provides:

- **before_all**: Test suite initialization, logging setup
- **after_all**: Cleanup, summary statistics
- **before_feature**: Feature-level resource setup
- **after_feature**: Feature-level cleanup
- **before_scenario**: Scenario-level context initialization
- **after_scenario**: Scenario resource cleanup
- **before_step**: Step-level logging (debug level)
- **after_step**: Step failure logging

## Configuration

Test behavior can be controlled via tags:

- `@wip` - Work-in-progress, requires API key for live LLM
- `@integration` - Integration tests (slower)
- `@slow` - Slow tests to be excluded with `-@slow`
- `@skip` - Tests to skip entirely

## Assertions and Helpers

Custom assertion helpers in `environment.py`:

- `assert_field_present(obj, field_name)` - Verify object has field
- `assert_field_value(obj, field, expected)` - Verify field value
- `assert_collection_contains(collection, item)` - Check membership
- `assert_collection_non_empty(collection)` - Verify non-empty

## CI/CD Integration

Run with JSON output for integration with CI/CD systems:

```bash
behave --format json -o results.json --format plain -o results.txt features/
```

Results can be parsed and displayed in build dashboards.

## Troubleshooting

### Test Failures

1. **Import errors**: Ensure project root is in Python path
2. **Mock issues**: Verify mock LLM is configured in context
3. **HTTP errors**: Check FastAPI app is properly initialized

### Debugging

Enable verbose output:

```bash
behave -v --format=plain --no-capture features/profiler.feature:3
```

Add logging in steps:

```python
logger = logging.getLogger("behave")
logger.info(f"Debug: {context.profile}")
```

## Best Practices

1. **Isolation**: Each scenario should be independent
2. **Cleanup**: Use `after_scenario` hook for resource cleanup
3. **Assertions**: Use domain-specific assertion helpers
4. **Mocking**: Keep mocks realistic but fast
5. **Documentation**: Write descriptive scenario names

## Future Enhancements

- [ ] Add test data fixtures in separate files
- [ ] Implement performance benchmarking steps
- [ ] Add database integration tests
- [ ] Support concurrent test execution
- [ ] Generate test coverage reports
- [ ] Add screenshot/video capture for failures

## References

- [Behave Documentation](https://behave.readthedocs.io/)
- [Gherkin Syntax](https://cucumber.io/docs/gherkin/)
- [httpx Documentation](https://www.python-httpx.org/)
- [FastAPI Testing](https://fastapi.tiangolo.com/advanced/testing-dependencies/)
