"""
ISTQB Syllabi — Test design techniques, risk-based testing, lifecycle.

Covers Foundation, Advanced Test Manager, and Advanced Test Analyst concepts.

This module provides comprehensive testing knowledge based on ISTQB certification
syllabi, including fundamental testing principles, test lifecycle, test design
techniques, test management, and tool support.

The module addresses:
- Testing fundamentals and role in quality assurance
- Test levels (component, integration, system, acceptance)
- Test types (functional, non-functional, structural, etc.)
- Test design techniques (black-box, white-box, experience-based)
- Test management and metrics
- Test tools classification and selection

References:
    - ISTQB Certified Tester Foundation Level Syllabus v4.0
    - ISTQB Advanced Level Test Manager Syllabus
    - ISTQB Advanced Level Test Analyst Syllabus
"""

STANDARD_ID = "ISTQB"

SECTIONS: dict[str, dict] = {
    "foundation": {
        "title": "ISTQB Certified Tester Foundation Level (CTFL) v4.0",
        "sections": {
            "1.1": {
                "part": "Part 1",
                "clause": "1.1",
                "title": "What is Testing?",
                "content": (
                    "Testing is an organized process to assess software quality and reduce the risk of software failure "
                    "in production. Testing encompasses far more than executing automated or manual test cases; it includes "
                    "activities such as planning, analysis, design, implementation, execution, and completion. Testing is a "
                    "collaborative effort involving developers, testers, analysts, and business stakeholders. Beyond execution, "
                    "testing includes review of work products such as requirements, user stories, designs, and code (static testing). "
                    "Testing is both constructive (identifying improvements) and destructive (seeking failures). Modern testing "
                    "emphasizes prevention through design review and early quality activities rather than detection-only approaches."
                ),
                "keywords": ["testing", "quality", "risk", "activities", "static testing", "dynamic testing", "planning"],
            },
            "1.2": {
                "part": "Part 1",
                "clause": "1.2",
                "title": "Why Testing is Necessary",
                "content": (
                    "Testing reduces software defects, increases confidence in quality, and manages risk. Testing cannot "
                    "prove absence of defects (it can only reveal presence). Software failures have potential for significant "
                    "financial, reputational, safety, and regulatory consequences. Testing serves multiple objectives: reducing "
                    "defect escape into production, providing confidence for release decisions, supporting continuous improvement "
                    "of development processes, and documenting system behavior through test coverage. Testing early in development "
                    "(shift-left) reduces defect remediation costs compared to detection in later phases. Context-driven testing "
                    "emphasizes that testing approaches must be tailored to project-specific factors including risk profile, "
                    "stakeholder priorities, and constraints."
                ),
                "keywords": ["risk", "defect", "quality", "confidence", "shift-left", "context-driven"],
            },
            "2.1": {
                "part": "Part 2",
                "clause": "2.1",
                "title": "Software Development Lifecycle and Testing",
                "content": (
                    "Testing does not exist in isolation but is integrated throughout the software development lifecycle. "
                    "Different development models (V-model, iterative, agile, DevOps) require corresponding adjustments to "
                    "testing approaches. The V-model emphasizes phase alignment: component design pairs with component testing, "
                    "system design with system testing, etc. Iterative and agile models test continuously within sprints/iterations "
                    "with feedback loops for rapid improvement. DevOps emphasizes continuous testing throughout delivery pipelines. "
                    "Regardless of model, testing activities must be planned, resourced, and integrated from project initiation. "
                    "Defects detected earlier in development are less costly to remediate than those discovered after release."
                ),
                "keywords": ["lifecycle", "V-model", "agile", "iterative", "DevOps", "continuous testing", "shift-left"],
            },
            "2.2": {
                "part": "Part 2",
                "clause": "2.2",
                "title": "Test Levels and Their Characteristics",
                "content": (
                    "Test levels organize testing activities into distinct phases corresponding to different scope and focus areas. "
                    "Component testing (or unit testing) verifies individual units in isolation using developer-written tests and stubs "
                    "for dependencies. Integration testing validates interfaces and interactions between components or systems, detecting "
                    "integration defects that don't manifest in isolated units. System testing exercises the complete integrated system "
                    "against requirements, validating end-to-end functionality, performance, and non-functional aspects. Acceptance testing "
                    "validates that the system meets business requirements and determines readiness for deployment. Each level has specific "
                    "entry/exit criteria, test objects, test basis documents, typical defects, and recommended techniques. Test levels may "
                    "overlap in agile environments where a single story spans multiple levels."
                ),
                "keywords": ["component", "integration", "system", "acceptance", "test levels", "unit testing", "UAT"],
            },
            "2.2.1": {
                "part": "Part 2",
                "clause": "2.2.1",
                "title": "Component Testing",
                "content": (
                    "Component testing (unit testing) verifies individual software units such as functions, methods, or classes "
                    "in isolation from other components. Entry criteria include unit specifications or design documents and availability "
                    "of component code. Test objects are typically small, discrete units designed for standalone verification. Developers "
                    "typically write and execute component tests, often using test-driven development (TDD) approaches writing tests before code. "
                    "Stubs and mocks replace dependencies on external components or systems. Common defects detected include incorrect logic, "
                    "boundary condition handling, error condition handling, and initialization issues. Exit criteria include achieving required "
                    "code coverage, defect resolution, and test completion. Component testing tools include xUnit frameworks (JUnit, NUnit, etc.), "
                    "mocking frameworks (Mockito, Moq), and code coverage tools (JaCoCo, Istanbul)."
                ),
                "keywords": ["unit testing", "component testing", "developer", "TDD", "mock", "stub", "code coverage"],
            },
            "2.2.2": {
                "part": "Part 2",
                "clause": "2.2.2",
                "title": "Integration Testing",
                "content": (
                    "Integration testing verifies communication, data flow, and interfaces between integrated components or systems. "
                    "Integration testing can occur at different granularities: between components within a system, between systems in an "
                    "ecosystem, or with external services. Entry criteria include completed component testing, integration test planning, "
                    "and test environment availability. Test objects include interfaces, integrated components, and data exchanges. Integration "
                    "testing typically employs bottom-up (test lower components first, building up) or top-down (test upper components first, "
                    "mocking lower) approaches. Stub and mock usage shifts from component testing; many dependencies are now real. Common defects "
                    "include interface mismatches, incorrect data transformations, missing error handling, and assumptions about component behavior. "
                    "Exit criteria include interface validation, data integrity verification, and system integration readiness confirmation."
                ),
                "keywords": ["integration testing", "interface", "component integration", "system integration", "data flow", "stubs", "API testing"],
            },
            "2.2.3": {
                "part": "Part 2",
                "clause": "2.2.3",
                "title": "System Testing",
                "content": (
                    "System testing validates the complete, integrated system against documented requirements and specifications. "
                    "The system is treated as a black box; internal structure is not considered. Entry criteria include system completion, "
                    "test environment readiness, and requirements traceability. Test objects include the entire system and system documentation. "
                    "System testing encompasses functional requirements (feature completeness and correctness) and non-functional requirements "
                    "(performance, security, usability, reliability, etc.). Testing addresses both normal operation and error conditions. Common "
                    "defects include missing features, incorrect functionality, poor performance, security vulnerabilities, and integration issues. "
                    "Exit criteria include requirements coverage, acceptance threshold achievement, and identified defect resolution. System testing "
                    "tools include test management platforms (TestRail, Zephyr), test automation frameworks, and performance testing tools."
                ),
                "keywords": ["system testing", "end-to-end", "functional requirements", "non-functional", "performance", "security testing"],
            },
            "2.2.4": {
                "part": "Part 2",
                "clause": "2.2.4",
                "title": "Acceptance Testing",
                "content": (
                    "Acceptance testing validates that the system meets business requirements and is acceptable for deployment to "
                    "production. Acceptance testing is often performed by business stakeholders, product owners, or designated acceptance "
                    "testers representing user interests. Entry criteria include system testing completion, acceptance test criteria definition, "
                    "and production environment readiness. Test objects include business scenarios, user stories, and acceptance criteria. "
                    "Acceptance testing encompasses User Acceptance Testing (UAT) validating against functional requirements, Operational Acceptance "
                    "Testing validating operational aspects (backup/recovery, administration), and Contract Acceptance Testing validating against "
                    "contract specifications. Common defects are typically few at this stage if upstream testing was effective; discovered defects "
                    "usually affect usability or business logic. Exit criteria include acceptance threshold achievement and go/no-go release decision. "
                    "Defect discovery at acceptance testing stage indicates insufficient testing in earlier levels."
                ),
                "keywords": ["acceptance testing", "UAT", "user acceptance", "business requirements", "go-live", "release decision"],
            },
            "2.3": {
                "part": "Part 2",
                "clause": "2.3",
                "title": "Test Types",
                "content": (
                    "Test types categorize testing based on what aspect of the system is being evaluated, independent of test level. "
                    "Functional testing verifies what the system does: features, functions, and business logic correctness. Non-functional testing "
                    "verifies how well the system behaves: performance, usability, security, reliability, maintainability, and portability. "
                    "Structural testing (white-box) verifies the internal structure and code paths. Confirmation testing verifies that previously "
                    "detected defects have been properly fixed. Regression testing verifies that changes haven't introduced new defects in "
                    "previously working functionality. Most test types apply across all test levels. Selection of test types depends on "
                    "test objectives and identified risks."
                ),
                "keywords": ["functional", "non-functional", "structural", "white-box", "regression", "confirmation", "test types"],
            },
            "2.3.1": {
                "part": "Part 2",
                "clause": "2.3.1",
                "title": "Functional Testing",
                "content": (
                    "Functional testing evaluates system features and functions against requirements specifications and user stories. "
                    "Functional testing is often black-box in nature (specifications-based without code knowledge). Testing covers normal "
                    "operations (typical user workflows), edge cases (boundary conditions), and error conditions (invalid inputs, exceptional states). "
                    "Functional defects manifest as missing features, incorrect calculations, wrong results, or incomplete workflows. Functional "
                    "testing typically uses black-box techniques such as equivalence partitioning and boundary value analysis. Functional test coverage "
                    "is typically measured as requirements coverage: percentage of requirements with corresponding test cases."
                ),
                "keywords": ["functional", "requirements", "features", "black-box", "workflows", "correctness"],
            },
            "2.3.2": {
                "part": "Part 2",
                "clause": "2.3.2",
                "title": "Non-Functional Testing",
                "content": (
                    "Non-functional testing evaluates system qualities and characteristics: performance, usability, security, reliability, "
                    "maintainability, and portability (ISO 25010 characteristics). Non-functional testing addresses requirements such as response "
                    "time thresholds, concurrent user support, data security, uptime percentages, and supportability. Non-functional defects "
                    "manifest as unacceptable response times, usability problems, security vulnerabilities, or system unavailability. Non-functional "
                    "testing often requires specialized tools (load testing, security scanning, accessibility checkers) and expertise. Non-functional "
                    "requirements must be explicitly defined as testable criteria during requirements analysis; absence of specification often results "
                    "in non-functional testing neglect."
                ),
                "keywords": ["non-functional", "performance", "load", "stress", "usability", "security", "reliability"],
            },
            "2.3.3": {
                "part": "Part 2",
                "clause": "2.3.3",
                "title": "Black-box vs. White-box Testing",
                "content": (
                    "Black-box testing (specification-based) evaluates behavior against specifications without internal structure knowledge. "
                    "Black-box testers don't require code access or understanding; they focus on inputs and outputs. Black-box testing is applicable "
                    "throughout all test levels and by testers without development expertise. White-box testing (structure-based) uses internal code "
                    "structure knowledge to design tests targeting specific code paths, branches, and conditions. White-box testing requires code access "
                    "and development expertise; it's primarily used in component and sometimes integration testing. Black-box testing is more effective "
                    "at finding functional defects; white-box testing is better at finding structural defects and coverage gaps. Most comprehensive "
                    "testing strategies combine both approaches."
                ),
                "keywords": ["black-box", "white-box", "specification-based", "structure-based", "code coverage"],
            },
            "2.3.4": {
                "part": "Part 2",
                "clause": "2.3.4",
                "title": "Confirmation and Regression Testing",
                "content": (
                    "Confirmation testing verifies that a previously detected defect has been properly resolved. Confirmation testing executes "
                    "the specific test case that revealed the original defect, verifying that the defect no longer reproduces. Additional test cases "
                    "may exercise related areas to ensure the fix is complete and robust. Effective confirmation testing requires clear defect "
                    "documentation including reproduction steps. Regression testing verifies that changes (features, bug fixes, enhancements) haven't "
                    "introduced new defects in previously working functionality. Regression testing is essential but resource-intensive; test "
                    "automation reduces regression testing cost and enables frequent execution. Regression test selection techniques include impact analysis "
                    "(testing areas affected by changes) and prioritization (risk-based selection of highest-impact tests)."
                ),
                "keywords": ["confirmation testing", "regression testing", "defect fix", "test automation", "impact analysis"],
            },
            "3.1": {
                "part": "Part 3",
                "clause": "3.1",
                "title": "Static Testing and Reviews",
                "content": (
                    "Static testing examines work products without executing code, including requirements, design specifications, "
                    "code, test cases, and documentation. Static testing can detect defects before execution, reducing detection cost. "
                    "Static techniques include informal reviews (unstructured review by colleagues), walkthroughs (author-led review), "
                    "technical reviews (peer review by experts), and inspections (formal, structured, metrics-based review). Code review "
                    "is a static testing technique examining source code for correctness, style, security issues, and maintainability. "
                    "Automated static analysis tools scan code for violations of coding standards, potential bugs, security vulnerabilities, "
                    "and code quality metrics. Effective static testing catches defects early when remediation cost is lowest."
                ),
                "keywords": ["static testing", "review", "code review", "inspection", "walthrough", "static analysis"],
            },
            "4.1": {
                "part": "Part 4",
                "clause": "4.1",
                "title": "Test Design Techniques Overview",
                "content": (
                    "Test design techniques provide systematic approaches for selecting test cases from infinite possible inputs. "
                    "Techniques are categorized as black-box (specification/requirement-based), white-box (structure-based), or experience-based. "
                    "Black-box techniques include equivalence partitioning, boundary value analysis, decision table testing, state transition testing, "
                    "and use case testing. White-box techniques include statement coverage, branch coverage, and condition coverage. Experience-based "
                    "techniques include exploratory testing, checklist-based testing, and error guessing. Technique selection depends on test objectives, "
                    "risk assessment, available time/resources, and tester expertise. Most comprehensive testing strategies employ multiple techniques "
                    "to maximize defect detection and requirement coverage."
                ),
                "keywords": ["test design", "techniques", "black-box", "white-box", "specification-based", "systematic"],
            },
            "4.2": {
                "part": "Part 4",
                "clause": "4.2",
                "title": "Black-box Test Design Techniques",
                "content": (
                    "Black-box techniques design tests based on specifications without code knowledge. These techniques are specification-based "
                    "and produce effective tests for requirements coverage. Equivalence Partitioning (EP) divides input/output domains into groups "
                    "(partitions) where all values should be treated identically by the system; one test case per partition provides broad coverage "
                    "efficiently. Boundary Value Analysis (BVA) targets the edges of partitions where defects frequently occur, testing at and "
                    "around boundary values. Decision Table Testing captures combinations of inputs and corresponding expected outputs, effectively "
                    "testing business logic with multiple conditions. State Transition Testing models system as state machine, testing transitions "
                    "between states triggered by events. Use Case Testing follows complete business scenarios from user perspective, testing workflows "
                    "and interactions. These techniques work well at all test levels and are particularly effective at system testing level."
                ),
                "keywords": ["equivalence", "boundary", "decision table", "state transition", "use case", "EP", "BVA"],
            },
            "4.2.1": {
                "part": "Part 4",
                "clause": "4.2.1",
                "title": "Equivalence Partitioning",
                "content": (
                    "Equivalence Partitioning divides input and output domains into groups where all values should be treated identically. "
                    "The principle is that if a test case with one value from a partition reveals a defect, then other values from that partition "
                    "would likely reveal the same defect. This reduces testing effort while maintaining comprehensive coverage. Partitions may be "
                    "based on input values (valid ranges vs. invalid ranges), output values, computational boundaries, or state conditions. "
                    "Deriving partitions requires understanding requirements and domain knowledge. Valid partitions contain acceptable values; invalid "
                    "partitions contain unacceptable values. Test case selection includes at least one test from each partition, with particular "
                    "attention to boundary values (see BVA). EP is particularly effective at reducing test cases when many combinations exist."
                ),
                "keywords": ["equivalence partitioning", "partitions", "valid", "invalid", "domain", "coverage"],
            },
            "4.2.2": {
                "part": "Part 4",
                "clause": "4.2.2",
                "title": "Boundary Value Analysis",
                "content": (
                    "Boundary Value Analysis identifies and tests values at the edges of equivalence partitions and at state transition "
                    "boundaries, where defects are disproportionately likely. BVA recognizes that programmers often make mistakes with boundary "
                    "conditions (off-by-one errors, <= vs. <, etc.). BVA tests values at, just inside, and just outside partition boundaries. "
                    "For a partition from 1 to 100, boundary values include 0 (just outside lower), 1 (at lower), 2 (just inside lower), 99 "
                    "(just inside upper), 100 (at upper), and 101 (just outside upper). BVA typically increases test cases compared to EP alone "
                    "but focuses effort on highest-risk areas. BVA is particularly effective for numeric ranges, dates, and state transitions. "
                    "Combined with EP, BVA provides powerful coverage of input domains."
                ),
                "keywords": ["boundary", "boundary value", "edges", "off-by-one", "transition", "limits"],
            },
            "4.2.3": {
                "part": "Part 4",
                "clause": "4.2.3",
                "title": "Decision Table Testing",
                "content": (
                    "Decision Table Testing systematically captures combinations of conditions and their resulting actions in a tabular format. "
                    "This technique is particularly effective for business logic where multiple conditions determine outcomes. Decision tables "
                    "organize test cases around condition combinations, ensuring comprehensive coverage of condition permutations. Conditions represent "
                    "input variables or predicates; actions represent outputs or behavior. Each column represents a test case (rule). Derivation "
                    "includes identifying all conditions, determining possible values (true/false for Boolean, or multiple values), listing all "
                    "actions, and defining rules covering all meaningful condition combinations. Simplified decision tables omit impossible or "
                    "redundant combinations. Decision table testing often reduces test cases compared to testing all possible combinations while "
                    "maintaining comprehensive coverage."
                ),
                "keywords": ["decision table", "conditions", "actions", "combinations", "rules", "business logic"],
            },
            "4.2.4": {
                "part": "Part 4",
                "clause": "4.2.4",
                "title": "State Transition Testing",
                "content": (
                    "State Transition Testing models system or software behavior as a state machine with distinct states and transitions "
                    "between them triggered by events. States represent system conditions; transitions represent event responses. Testing "
                    "verifies that transitions occur correctly in response to triggers and that the system enters the expected new state. "
                    "State transition diagrams visually represent valid transitions; the diagram guides test case design. Test cases follow "
                    "paths through the state diagram, covering states and transitions. Coverage criteria include all states visited at least "
                    "once, all transitions exercised at least once, and invalid transitions properly rejected. State transition testing is "
                    "effective for systems with stateful behavior such as workflows, protocols, or complex business processes with sequential "
                    "phases."
                ),
                "keywords": ["state transition", "state machine", "states", "events", "transitions", "workflows"],
            },
            "4.2.5": {
                "part": "Part 4",
                "clause": "4.2.5",
                "title": "Use Case Testing",
                "content": (
                    "Use Case Testing derives test cases from documented use cases representing complete business scenarios from user "
                    "perspective. Use cases describe actor interactions with the system, including preconditions, main flow, alternative flows, "
                    "and postconditions. Each use case becomes a test scenario; test cases cover main flows and alternative/exceptional flows. "
                    "Use case testing ensures that complete workflows function correctly end-to-end. This technique is particularly valuable for "
                    "system and acceptance testing where end-to-end validation is critical. Use case testing provides business relevance and "
                    "stakeholder alignment; test cases directly correspond to documented business scenarios."
                ),
                "keywords": ["use case", "scenario", "business flow", "actor", "workflow", "end-to-end"],
            },
            "4.3": {
                "part": "Part 4",
                "clause": "4.3",
                "title": "White-box Test Design Techniques",
                "content": (
                    "White-box (structure-based) test design uses knowledge of internal code structure to design tests targeting specific "
                    "code paths, branches, and conditions. White-box testing requires code access and development expertise. Code coverage "
                    "metrics quantify testing thoroughness: statement coverage, branch coverage, condition coverage, and path coverage. Statement "
                    "Coverage measures percentage of executable statements executed by tests; branch coverage measures percentage of decision "
                    "outcomes (true/false branches) executed. Condition coverage measures individual condition values within complex expressions. "
                    "Path coverage measures percentage of execution paths through code; this grows exponentially with decisions and becomes "
                    "impractical for large code bases. 100% statement coverage is a minimum reasonable target; 100% branch coverage is often "
                    "more achievable and meaningful. Coverage measurement tools instrumentalize code to track execution."
                ),
                "keywords": ["white-box", "coverage", "statement", "branch", "condition", "path", "internal structure"],
            },
            "4.3.1": {
                "part": "Part 4",
                "clause": "4.3.1",
                "title": "Statement Coverage",
                "definition": (
                    "Statement Coverage measures the percentage of executable statements exercised at least once during testing. "
                    "This is the most basic coverage metric. Achieving 100% statement coverage ensures every line is executed, but "
                    "doesn't verify correctness or comprehensive branch testing. Statement coverage alone may miss defects in untaken "
                    "branches. Coverage tools highlight uncovered code, guiding test development. Uncovered code indicates either dead code "
                    "(unreachable) or inadequate test coverage."
                ),
                "content": (
                    "Statement Coverage exercises every executable statement at least once. This is the most fundamental coverage metric "
                    "and minimum reasonable testing target. Achieving 100% statement coverage ensures all code is exercised but may miss "
                    "branch-specific defects. For example, code executing if-branch but not else-branch achieves statement coverage while missing "
                    "potential else-branch defects. Coverage measurement tools identify uncovered statements (dark red or highlighted in reports), "
                    "guiding test development. Uncovered code suggests either dead code that should be removed or testing gaps that need addressing."
                ),
                "keywords": ["statement coverage", "lines of code", "executable statements", "coverage measurement"],
            },
            "4.3.2": {
                "part": "Part 4",
                "clause": "4.3.2",
                "title": "Branch Coverage",
                "content": (
                    "Branch Coverage (decision coverage) measures the percentage of decision branches (true and false outcomes) exercised. "
                    "Branch coverage is a stronger metric than statement coverage; 100% branch coverage implies 100% statement coverage. Branch "
                    "coverage requires multiple test cases for decisions: one exercising the true branch, another exercising the false branch. "
                    "Complex conditions with AND/OR operators may require additional tests covering different condition combinations (condition coverage). "
                    "Branch coverage effectiveness depends on test data quality; high branch coverage with poor test data (testing for execution "
                    "without validating correct behavior) is less effective than low coverage with good test data."
                ),
                "keywords": ["branch coverage", "decision coverage", "coverage", "condition", "true", "false"],
            },
            "4.3.3": {
                "part": "Part 4",
                "clause": "4.3.3",
                "title": "Condition and Path Coverage",
                "content": (
                    "Condition Coverage (multiple condition coverage, MC/DC) measures individual condition values within complex boolean "
                    "expressions. For expressions with AND/OR operators, condition coverage ensures each condition evaluates true and false "
                    "in meaningful combinations. Modified Condition/Decision Coverage (MC/DC) additionally requires that each condition affects "
                    "the overall decision outcome independently. Path Coverage measures execution paths through code; this grows exponentially "
                    "with decision count and becomes impractical for realistic code bases. For example, code with 10 independent decisions has "
                    "1024 possible paths; path coverage is rarely achieved completely. MC/DC is often required for safety-critical systems "
                    "(aviation, medical) where thorough condition testing is justified. Practical testing often targets branch coverage as a "
                    "balance between coverage completeness and effort."
                ),
                "keywords": ["condition coverage", "MC/DC", "path coverage", "safety-critical", "boolean expressions"],
            },
            "5.1": {
                "part": "Part 5",
                "clause": "5.1",
                "title": "Test Management and Quality Metrics",
                "content": (
                    "Test management encompasses planning, resourcing, scheduling, monitoring, and control of test activities. "
                    "Test planning defines test strategy, scope, entry/exit criteria, resource allocation, and scheduling. Test organization "
                    "establishes roles (test manager, test lead, test analyst, test automation engineer) and responsibilities. Risk-based testing "
                    "prioritizes testing effort based on identified risks: high-risk areas receive more testing. Test monitoring tracks progress "
                    "against plans through metrics (tests planned vs. executed, defect detection rate, test execution progress). Test control "
                    "responds to monitoring data, adjusting activities to address variances. Defect management tracks reported defects through "
                    "lifecycle: reported → analyzed → prioritized → assigned → fixed → retested → closed. Test metrics provide objective measures "
                    "of testing effectiveness, progress, and quality."
                ),
                "keywords": ["test management", "planning", "risk-based", "monitoring", "metrics", "defect management"],
            },
            "5.1.1": {
                "part": "Part 5",
                "clause": "5.1.1",
                "title": "Test Planning and Strategy",
                "content": (
                    "Test planning establishes the overall testing approach, objectives, scope, strategy, schedule, and resource "
                    "allocation. Test planning occurs at project level (overall test strategy) and release/iteration level (test plans). "
                    "Test strategy defines which test types will be applied, test levels and scope, test coverage targets, test design "
                    "techniques to be employed, and risk-based prioritization. Entry criteria specify conditions that must be met before "
                    "testing can commence (test environment readiness, test data availability, requirements completion). Exit criteria "
                    "specify conditions determining when testing is sufficiently complete (coverage targets achieved, acceptable defect "
                    "levels, go/no-go decisions). Test planning must account for constraints (time, budget, resources, tooling) and "
                    "dependencies on development activities."
                ),
                "keywords": ["test planning", "test strategy", "entry criteria", "exit criteria", "scope", "scheduling"],
            },
            "5.1.2": {
                "part": "Part 5",
                "clause": "5.1.2",
                "title": "Risk-Based Testing and Test Prioritization",
                "content": (
                    "Risk-based testing prioritizes testing effort based on identified product risks (likelihood and impact of failures). "
                    "Product risk analysis identifies potential failure modes, estimates likelihood and impact, and prioritizes for testing. "
                    "High-risk areas (critical functionality, complex logic, high impact failures) receive more intensive testing. Risk-based "
                    "testing ensures effort focuses on most important areas, especially when resources are constrained. Risk level is often "
                    "calculated as likelihood × impact. Risk assessment should consider functional risks (incorrect calculations, missing features), "
                    "non-functional risks (poor performance, security vulnerabilities), integration risks (interface failures, data corruption), "
                    "and infrastructure risks (availability, reliability). Risk-based test prioritization determines test execution order, focusing "
                    "on high-risk tests first."
                ),
                "keywords": ["risk-based", "risk analysis", "likelihood", "impact", "prioritization", "critical", "high-risk"],
            },
            "5.1.3": {
                "part": "Part 5",
                "clause": "5.1.3",
                "title": "Test Monitoring and Metrics",
                "content": (
                    "Test monitoring tracks test execution progress and quality metrics against planned targets. Key metrics include test "
                    "cases planned/executed/passed/failed percentages, defect detection rates, defect density (defects per line of code), "
                    "defect age (time from detection to closure), test coverage achieved, and risk coverage. Metrics provide early warning "
                    "of problems (low test pass rate, high defect escape) enabling corrective action. Metrics support release readiness "
                    "decisions: if test pass rate is too low or defect escape rate is high, system may not be ready for release. Common "
                    "pitfalls include metric manipulation (emphasizing metrics rather than quality) or missing context (failing tests might "
                    "indicate insufficient testing or poor test design, not necessarily poor product quality)."
                ),
                "keywords": ["monitoring", "metrics", "test progress", "defect rate", "coverage", "quality gates"],
            },
            "5.1.4": {
                "part": "Part 5",
                "clause": "5.1.4",
                "title": "Configuration Management and Test Traceability",
                "content": (
                    "Configuration management tracks test artifacts, builds, test environments, and test data versions throughout "
                    "testing lifecycle. Configuration management ensures reproducibility: given a specific build version, test environment "
                    "configuration, and test data, test execution should be reproducible. Version control repositories maintain historical "
                    "versions of test cases, test data, and test environments. Build management tracks which code version is being tested. "
                    "Test environments must be properly versioned and documented (OS version, database version, third-party dependencies). "
                    "Test traceability links requirements to test cases (requirements traceability matrix/RTM) enabling requirements coverage "
                    "verification. Test cases link to test results and discovered defects enabling traceability from requirements through "
                    "testing to quality assurance."
                ),
                "keywords": ["configuration management", "version control", "traceability", "RTM", "build management"],
            },
            "6.1": {
                "part": "Part 6",
                "clause": "6.1",
                "title": "Test Tool Support and Classification",
                "content": (
                    "Test tools support various testing activities throughout the development lifecycle. Tools can be categorized by "
                    "function: test management (planning, case management, execution tracking), test design (test case generation, "
                    "decision table tools), test automation (automated test execution), performance testing (load, stress, profiling), "
                    "security testing (vulnerability scanning, penetration testing), code analysis (static code analysis, code coverage), "
                    "and environment management (configuration, build, deployment). Tool selection depends on testing needs, integration "
                    "with development environment, licensing costs, and team expertise. Overreliance on tools without effective testing "
                    "processes is ineffective; tools support process, not replace good testing practices. Tool evaluation should consider "
                    "learning curve, maintenance requirements, and long-term support."
                ),
                "keywords": ["test tools", "test management", "automation", "performance", "security", "static analysis"],
            },
            "6.1.1": {
                "part": "Part 6",
                "clause": "6.1.1",
                "title": "Test Management Tools",
                "content": (
                    "Test management tools provide test case repositories, test execution tracking, results reporting, and traceability "
                    "to requirements. These tools organize test cases, track execution progress, record results, and generate metrics reports. "
                    "Features include test case organization (hierarchical folders), status tracking (planned, in progress, passed, failed), "
                    "execution assignment to testers, and defect linkage. Benefits include centralized test asset management, progress visibility, "
                    "and historical record of testing. Some tools integrate with requirements management and issue tracking, providing end-to-end "
                    "traceability. Test management tools support manual testing; they don't automate test execution."
                ),
                "keywords": ["test management", "test case", "execution", "tracking", "reporting", "traceability"],
            },
            "6.1.2": {
                "part": "Part 6",
                "clause": "6.1.2",
                "title": "Test Automation Tools",
                "content": (
                    "Test automation tools execute tests automatically, reducing execution time and enabling frequent testing. Automation "
                    "tools record or script interactions (UI clicks, API calls, database queries) and verify results against expectations. "
                    "Benefits include repeatability (same test can be run identically each time), execution speed (automation is faster than "
                    "manual), and regression testing support (previously passing tests can be repeatedly validated). Risks include high initial "
                    "investment (scripting time, maintenance), false confidence (automated tests don't catch unforeseen issues), and maintenance "
                    "burden (tests break when system changes). Effective automation focuses on stable, frequently-executed tests; automation "
                    "of rarely-executed exploratory testing is inefficient. Common tools include Selenium (web UI), Cypress (web), Appium (mobile), "
                    "Postman (API), and TestNG/JUnit (unit testing)."
                ),
                "keywords": ["test automation", "regression", "scripts", "execution", "repeatability", "maintenance"],
            },
            "6.1.3": {
                "part": "Part 6",
                "clause": "6.1.3",
                "title": "Performance and Security Testing Tools",
                "content": (
                    "Performance testing tools generate load on systems to measure response times, throughput, and resource utilization "
                    "under various load profiles. Load testing applies expected load; stress testing exceeds expected load to find breaking "
                    "points. Tools include JMeter, LoadRunner, and Gatling. Results include performance graphs, bottleneck identification, and "
                    "capacity recommendations. Security testing tools identify vulnerabilities: static analysis scans code for security issues; "
                    "dynamic analysis runs the application testing for runtime vulnerabilities; penetration testing simulates attacks. Tools "
                    "include SonarQube (code quality), OWASP ZAP (web vulnerabilities), Nessus (vulnerability scanning), and Burp Suite (web "
                    "security testing). Effective security testing combines automated scanning (broad coverage, consistency) with manual testing "
                    "(creative attacks, business logic vulnerabilities)."
                ),
                "keywords": ["performance testing", "load testing", "security testing", "vulnerability scanning", "penetration testing"],
            },
        },
    },
    "advanced_test_manager": {
        "title": "ISTQB Advanced Level Test Manager (CTAL-TM) v4.0",
        "sections": {
            "1.1": {
                "part": "Part 1",
                "clause": "1.1",
                "title": "Role and Responsibilities of Test Manager",
                "content": (
                    "A test manager is responsible for test team leadership, process improvement, quality assurance metrics, risk "
                    "management, and stakeholder communication. Test manager responsibilities include test strategy development, test "
                    "planning, resource allocation, test execution oversight, metrics interpretation, defect escalation, and release "
                    "readiness assessment. Test managers bridge development and business stakeholders, translating quality requirements "
                    "into testing activities and communicating testing status to decision-makers. Test managers must possess testing expertise, "
                    "leadership skills, and business acumen. In agile environments, test managers often coordinate across distributed team "
                    "members; in traditional environments, test managers may directly oversee larger test teams."
                ),
                "keywords": ["test manager", "leadership", "metrics", "risk management", "stakeholder", "planning"],
            },
            "2.1": {
                "part": "Part 2",
                "clause": "2.1",
                "title": "Test Strategy and Policy",
                "content": (
                    "Test strategy defines the overall approach to testing across the organization. Test strategy addresses test methodology "
                    "(V-model, agile, DevOps), risk-based prioritization, test levels and types to be applied, tool strategy, training strategy, "
                    "and continuous improvement approach. Test policy establishes testing standards, entry/exit criteria templates, and "
                    "organizational expectations. Test strategy should align with business objectives and development processes. Strategy "
                    "documentation provides consistency across projects and enables onboarding of new testers. Regular strategy review ensures "
                    "continuing relevance as organizational processes evolve."
                ),
                "keywords": ["strategy", "policy", "methodology", "standards", "organizational", "continuous improvement"],
            },
            "2.2": {
                "part": "Part 2",
                "clause": "2.2",
                "title": "Test Planning and Estimation",
                "content": (
                    "Test planning translates test strategy into specific plans for projects or releases. Test plans specify scope (what will "
                    "be tested), schedule (timeline), resource allocation (team members and skills needed), entry/exit criteria, test design "
                    "techniques, and risk-based prioritization. Test estimation calculates effort needed for test activities; estimation methods "
                    "include metrics-based (using historical data on similar projects), expert-based (eliciting estimates from experienced "
                    "testers), and parametric (using algorithms based on scope factors). Estimation should account for rework (test script "
                    "maintenance, environment setup retries). Test planning must coordinate with development schedule ensuring tests are ready "
                    "when code is ready for testing."
                ),
                "keywords": ["planning", "estimation", "effort", "scope", "schedule", "resource allocation"],
            },
            "2.3": {
                "part": "Part 2",
                "clause": "2.3",
                "title": "Test Estimation Methods",
                "content": (
                    "Test estimation approaches vary in sophistication and applicability. Metrics-based estimation uses historical data from "
                    "similar projects: if past projects required 40 hours of testing per 100 lines of code, and the current project has 5000 "
                    "lines, estimation is 2000 hours. Defect density estimation assumes defect rate based on historical data and allocates "
                    "testing effort to achieve target defect detection. Expert-based approaches (Wideband Delphi, planning poker) elicit estimates "
                    "from experienced team members. Factors affecting estimation include product complexity (algorithm difficulty, data dependencies), "
                    "tool support availability, team experience level, quality requirements, and environmental factors (tools, infrastructure). "
                    "Estimation should explicitly address risks (estimation includes buffer for unknowns) and include assumptions documentation."
                ),
                "keywords": ["estimation", "effort", "complexity", "metrics", "expert judgment", "planning poker"],
            },
            "3.1": {
                "part": "Part 3",
                "clause": "3.1",
                "title": "Test Process Management",
                "content": (
                    "Test process management encompasses planning, monitoring and controlling, and improvement. Planning establishes what will "
                    "be done, by whom, and when. Monitoring tracks actual progress against plan through metrics (test progress, defect rates, "
                    "resource utilization). Control takes corrective action when metrics indicate variances (tests behind schedule, defect "
                    "levels unacceptable). Process improvement addresses root causes of problems and implements improvements. Test managers "
                    "establish metrics dashboards providing visibility to stakeholders, identifying issues early. Regular test status meetings "
                    "with development and business stakeholders maintain alignment on testing progress and risks."
                ),
                "keywords": ["process management", "monitoring", "control", "planning", "metrics", "improvement"],
            },
            "3.2": {
                "part": "Part 3",
                "clause": "3.2",
                "title": "Defect Management and Root Cause Analysis",
                "content": (
                    "Defect management tracks reported defects through complete lifecycle: detected → reported → analyzed → prioritized → "
                    "assigned → fixed → retested → closed. Defect reports should include reproduction steps, environment details, severity "
                    "(impact on users), and priority (urgency of remediation). Severity is objective (defect impact); priority is subjective "
                    "(remediation urgency). Test managers ensure timely defect resolution and escalate blockers. Root cause analysis investigates "
                    "why defects weren't prevented in development; findings should drive process improvements. Defect metrics (detection rate, "
                    "escape rate, density, age) provide quality visibility."
                ),
                "keywords": ["defect management", "lifecycle", "severity", "priority", "root cause", "metrics"],
            },
            "3.3": {
                "part": "Part 3",
                "clause": "3.3",
                "title": "Test Team Organization and Roles",
                "content": (
                    "Test team composition depends on project size, complexity, and methodology. Roles include test manager (leadership, "
                    "planning, metrics), test lead (day-to-day coordination), test analyst (test case design), test automation engineer "
                    "(automation implementation), and test administrator (environment, data management). In agile teams, roles may be shared "
                    "or distributed. Test manager must ensure team has appropriate skills (automation, domain knowledge, testing expertise), "
                    "training, tools, and clear responsibilities. Effective team communication (stand-ups, retrospectives, knowledge sharing) "
                    "supports quality and morale."
                ),
                "keywords": ["team", "roles", "responsibilities", "test manager", "test lead", "skills"],
            },
            "4.1": {
                "part": "Part 4",
                "clause": "4.1",
                "title": "Defect Lifecycle and Metrics",
                "content": (
                    "Defect lifecycle encompasses detection, reporting, analysis, prioritization, assignment, resolution, verification, and "
                    "closure. Defect reporting includes reproduction steps (clear steps to recreate), environment details (OS, database version), "
                    "expected vs. actual behavior, and attachments (screenshots, logs). Analysis determines root cause and fix approach. "
                    "Prioritization considers severity (impact) and priority (schedule urgency). Defect metrics track quality trends: defect "
                    "detection rate (defects found per test execution hour), defect escape rate (defects found in production vs. testing), "
                    "defect density (defects per 1000 lines of code), defect age (time from detection to closure). Metrics enable quality "
                    "assessment and trend analysis guiding testing focus."
                ),
                "keywords": ["defect", "lifecycle", "severity", "priority", "metrics", "escape rate"],
            },
            "4.2": {
                "part": "Part 4",
                "clause": "4.2",
                "title": "Quality Gates and Release Decisions",
                "content": (
                    "Quality gates are defined criteria determining whether a software release can proceed. Quality gates typically include "
                    "test coverage thresholds (percentage of requirements tested), defect thresholds (critical defects must be zero, major "
                    "defects below acceptable level), code quality metrics (code coverage, static analysis violations), and performance criteria "
                    "(response time, scalability). Release readiness assessment synthesizes testing metrics, risk assessment, and business "
                    "requirements. Decisions are go (release approved), go with conditions (release approved with workarounds or known "
                    "limitations documented), or no-go (release blocked pending further testing/fixes). Release decision documentation should "
                    "justify the decision and acknowledge remaining risks."
                ),
                "keywords": ["quality gates", "release decision", "go-live", "criteria", "thresholds", "risk"],
            },
        },
    },
    "advanced_test_analyst": {
        "title": "ISTQB Advanced Level Test Analyst (CTAL-TA) v4.0",
        "sections": {
            "1.1": {
                "part": "Part 1",
                "clause": "1.1",
                "title": "Role of Test Analyst",
                "content": (
                    "Test analysts design test cases and develop test specifications, translating requirements into comprehensive test "
                    "coverage. Test analysts require strong domain knowledge, testing expertise, and analytical skills. Test analysts "
                    "collaborate with business analysts to clarify requirements, with developers to understand implementation, and with "
                    "test managers to prioritize testing. Test analysts must think like users (black-box perspective) and like developers "
                    "(understanding implementation). Test analysts select appropriate design techniques, create test cases, and sometimes "
                    "execute or automate tests. In agile environments, test analysts often work within development teams; in traditional "
                    "environments, test analysts may be a separate testing organization."
                ),
                "keywords": ["test analyst", "design", "requirements", "specifications", "test cases", "collaboration"],
            },
            "2.1": {
                "part": "Part 2",
                "clause": "2.1",
                "title": "Requirement Analysis and Testability Review",
                "content": (
                    "Test analysts analyze requirements to understand scope and extractable test cases. Requirement analysis identifies "
                    "ambiguities, inconsistencies, and missing specifications preventing clear testing. Good requirements are testable "
                    "(observable, repeatable), unambiguous, and complete. Test analysts conduct testability reviews: are requirements stated "
                    "precisely enough to determine if they're met? Are acceptance criteria clear? Testability issues should be raised with "
                    "business analysts for clarification. Requirements organization (requirements hierarchy, relationships) aids test design. "
                    "Traceability matrices link requirements to test cases ensuring comprehensive coverage. Requirements not adequately specified "
                    "cannot be thoroughly tested; early requirement quality work pays dividends."
                ),
                "keywords": ["requirements", "analysis", "testability", "traceability", "acceptance criteria"],
            },
            "3.1": {
                "part": "Part 3",
                "clause": "3.1",
                "title": "Test Case Design and Execution",
                "content": (
                    "Test case design creates specific test cases from requirements and test design techniques. A well-designed test case "
                    "includes test objective (what is being tested), preconditions (system state before test), input (data or actions), "
                    "expected result (what should happen), and postconditions (system state after test). Test cases should be independent "
                    "(can be executed in any order), atomic (test one thing), and clearly written (someone else can execute without ambiguity). "
                    "Test case organization (by feature, by test level, by risk) aids management. Test case execution involves following "
                    "steps precisely, recording results (passed/failed), capturing evidence (screenshots, logs), and reporting issues. "
                    "Test execution documentation supports traceability and change management."
                ),
                "keywords": ["test case", "design", "execution", "preconditions", "expected results", "postconditions"],
            },
            "3.2": {
                "part": "Part 3",
                "clause": "3.2",
                "title": "Test Design Techniques Application",
                "content": (
                    "Test analysts select appropriate test design techniques based on test item characteristics and risk level. Functional "
                    "requirements with business logic respond well to decision table testing or state transition testing. Numeric input "
                    "validation benefits from equivalence partitioning and boundary value analysis. Complex workflows align with use case "
                    "testing. Data-driven features may benefit from pairwise testing or classification tree method. Selection should balance "
                    "technique rigor (thoroughness) with effort. Most effective testing uses multiple techniques on the same item, providing "
                    "different test perspectives. Technique application should be documented in test specifications allowing technique "
                    "selection justification."
                ),
                "keywords": ["techniques", "selection", "business logic", "input validation", "workflows", "pairwise"],
            },
            "4.1": {
                "part": "Part 4",
                "clause": "4.1",
                "title": "Non-functional Testing and Quality Characteristics",
                "content": (
                    "Non-functional testing addresses ISO 25010 quality characteristics (performance, usability, security, reliability, "
                    "etc.). Performance testing measures response times, throughput, and resource utilization under various load conditions. "
                    "Usability testing evaluates user interface design, learnability, and accessibility. Reliability testing validates "
                    "system stability and recovery capabilities. Security testing verifies confidentiality, integrity, and access controls. "
                    "Maintainability testing evaluates code quality and testability. Portability testing validates platform independence "
                    "and installation procedures. Each quality characteristic requires specialized testing approaches and often specialized "
                    "tools. Non-functional testing is often neglected if not explicitly planned and resourced."
                ),
                "keywords": ["non-functional", "performance", "load", "stress", "usability", "security", "reliability"],
            },
            "4.2": {
                "part": "Part 4",
                "clause": "4.2",
                "title": "Performance Testing Approaches",
                "content": (
                    "Performance testing measures system behavior under various load conditions. Load testing applies expected production "
                    "load, measuring response times and throughput. Stress testing exceeds expected load, determining breaking points and "
                    "degradation patterns. Endurance (soak) testing applies moderate load for extended periods, detecting memory leaks and "
                    "resource exhaustion. Spike testing applies sudden load increases, testing system reaction. Performance test design "
                    "requires understanding production usage patterns (user distribution, typical transactions). Results identify bottlenecks "
                    "(components limiting performance) and support capacity planning. Performance testing requires production-like environments "
                    "and realistic test data. Performance metrics include response time (latency), throughput, resource utilization (CPU, "
                    "memory, disk, network), and scalability (performance degradation with increased load)."
                ),
                "keywords": ["performance", "load", "stress", "endurance", "spike", "scalability", "bottleneck"],
            },
            "4.3": {
                "part": "Part 4",
                "clause": "4.3",
                "title": "Security Testing Approaches",
                "content": (
                    "Security testing verifies that systems protect information and enforce access controls. Threat modeling identifies "
                    "potential attack vectors (SQL injection, cross-site scripting, etc.) guiding test design. Static security analysis "
                    "scans code for known vulnerable patterns. Dynamic security testing (penetration testing) attempts actual attacks against "
                    "running systems. Security testing addresses authentication (correct identity verification), authorization (access controls "
                    "enforced), confidentiality (encryption and access control), and integrity (data cannot be modified without authorization). "
                    "OWASP provides comprehensive security testing guidance. Security testing should combine automated scanning (broad, "
                    "consistent coverage) with manual testing (creative attacks, business logic vulnerabilities). Security defects have high "
                    "severity; security testing requires sustained effort."
                ),
                "keywords": ["security", "threat", "penetration", "vulnerability", "encryption", "access control"],
            },
            "4.4": {
                "part": "Part 4",
                "clause": "4.4",
                "title": "Usability Testing Approaches",
                "content": (
                    "Usability testing evaluates how effectively and efficiently users can accomplish tasks, and user satisfaction. Usability "
                    "encompasses learnability (how quickly users learn), operability (ease of operation), accessibility (usable by people with "
                    "disabilities), and aesthetics (visual appeal). Usability testing methodologies include user testing (observing users "
                    "performing tasks), surveys (collecting subjective feedback), and accessibility evaluation (WCAG compliance). Usability "
                    "defects manifest as confusion, excessive steps, poor error recovery, and user frustration. Usability testing requires "
                    "representative users; testing with developers biases results toward developer mental models rather than typical user "
                    "understanding."
                ),
                "keywords": ["usability", "learnability", "accessibility", "user testing", "WCAG", "satisfaction"],
            },
        },
    },
}
