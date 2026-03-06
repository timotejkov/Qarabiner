# Quick Start: Running Behave Tests

## Prerequisites

```bash
pip install behave httpx pytest
```

## Running Tests

### All Tests
```bash
cd /sessions/gracious-nifty-johnson/mnt/TestAI/prototype
behave features/
```

### Specific Feature
```bash
behave features/profiler.feature
behave features/architect.feature
behave features/api.feature
```

### Specific Scenario
```bash
# Run scenario at line 10 of profiler.feature
behave features/profiler.feature:10
```

### With Verbose Output
```bash
behave -v features/
behave -v features/profiler.feature
```

### By Tags
```bash
# Run integration tests only
behave --tags=@integration

# Exclude work-in-progress tests
behave --tags=-@wip

# Exclude slow tests
behave --tags=-@slow

# Multiple conditions
behave --tags=@integration --tags=-@slow
```

### With Specific Format
```bash
# Plain text (default)
behave features/

# JSON (for CI/CD)
behave --format json -o results.json features/

# Pretty format
behave --format pretty features/

# HTML (if html formatter installed)
behave --format html -o report.html features/
```

## Test Structure

### Features Directory
```
features/
├── profiler.feature              # Agent 1: PRD → Profile
├── researcher.feature            # Agent 2: Profile → Standards
├── architect.feature             # Agent 3: Standards → Strategy/Questions
├── critic.feature                # Agent 4: Validation
├── api.feature                   # REST API endpoints
├── mattermost_benchmark.feature  # End-to-end tests
├── environment.py                # Behave hooks
├── steps/
│   ├── agent_steps.py           # Agent test steps
│   ├── api_steps.py             # API test steps
│   └── benchmark_steps.py       # Benchmark test steps
└── README.md                     # Detailed documentation
```

## Common Workflows

### Development: Run One Feature
```bash
behave features/architect.feature -v
```

### Testing: Run All Excluding WIP
```bash
behave features/ --tags=-@wip
```

### CI/CD: Generate JSON Report
```bash
behave features/ --format json -o test_results.json --format plain
```

### Debugging: Run with No Capture
```bash
behave --no-capture features/profiler.feature:1
```

### Performance: Check Slow Tests
```bash
behave --tags=@slow features/ -v
```

## Expected Output

### Successful Run
```
Feature: Profiler Agent (Agent 1)
  Background: Passing
    Given the Profiler agent is initialized ... OK in 0.001s
    And a mock LLM is configured to return structured responses ... OK in 0.001s

  Scenario: Extracts tech stack from detailed PRD
    Given a detailed PRD describing a Node.js backend and React frontend with PostgreSQL ... OK
    And the domain is "general_software" ... OK
    And the safety level is