"""
ISO/IEC/IEEE 29119 — Software Testing Standard.

Comprehensive reference material for software testing based on ISO/IEC/IEEE 29119 concepts.
This module provides summaries of publicly available principles and guidance from the standard.
These are summaries and practical guidance, NOT verbatim copyrighted text.

In production, this would be replaced by a Vector DB with licensed content.
"""

STANDARD_ID = "ISO/IEC/IEEE 29119"

SECTIONS: dict[str, dict] = {
    "29119-1:2022": {
        "title": "Part 1: General Concepts and Vocabulary",
        "part": 1,
        "sections": {
            "1": {
                "title": "Scope and Application",
                "part": 1,
                "clause": 1,
                "content": (
                    "Part 1 establishes fundamental concepts and vocabulary for software testing, "
                    "providing a common language across the testing discipline. It defines what constitutes "
                    "testing, its objectives, and its scope across the entire software development lifecycle. "
                    "The concepts apply to testing in all development models (waterfall, agile, iterative, etc.), "
                    "all types of organizations (small to large), and all software domains (embedded, enterprise, safety-critical). "
                    "This foundation enables effective communication between stakeholders and ensures consistent interpretation "
                    "of testing concepts and practices across projects and organizations."
                ),
                "keywords": ["concepts", "vocabulary", "testing", "lifecycle", "scope", "terminology", "definitions"],
            },
            "4.1": {
                "title": "Definition of Software Testing",
                "part": 1,
                "clause": "4.1",
                "content": (
                    "Testing is a process encompassing all lifecycle activities, both static and dynamic, concerned with "
                    "planning, preparation, and evaluation of a component or system and related work products. Its purposes are: "
                    "(1) to determine that specified requirements are satisfied, (2) to demonstrate that the software is fit for purpose, "
                    "and (3) to detect defects that could impact quality. Static testing includes reviews and analysis; dynamic testing "
                    "involves executing the software. Testing must be planned, structured, and controlled to maximize effectiveness. "
                    "The earlier defects are found, the lower their cost of remediation, emphasizing the importance of testing throughout "
                    "the development lifecycle rather than only at the end."
                ),
                "keywords": ["definition", "testing", "static", "dynamic", "evaluation", "planning", "defect detection", "quality"],
            },
            "4.2": {
                "title": "Test Objectives and Goals",
                "part": 1,
                "clause": "4.2",
                "content": (
                    "Testing has multiple, sometimes competing objectives: to verify that requirements are met (verification), "
                    "to validate that the software meets user needs (validation), to ensure fitness for purpose, and to detect defects. "
                    "Test objectives drive test strategy and guide the allocation of testing resources. Primary testing goals include: "
                    "building confidence in software quality, identifying failures and defects before release, supporting decision-making "
                    "on software readiness, and preventing defects through early quality activities. Different stakeholders may have different "
                    "priorities (developers focus on correctness, customers focus on fitness for purpose), so test objectives must be explicitly "
                    "defined and agreed upon before testing begins."
                ),
                "keywords": ["objectives", "goals", "verification", "validation", "fitness for purpose", "quality", "defect detection"],
            },
            "4.3": {
                "title": "Test Levels",
                "part": 1,
                "clause": "4.3",
                "content": (
                    "Testing is organized into distinct levels, each with different scope, focus, and objectives. "
                    "Unit/component testing focuses on individual software modules or functions, verifying logic and correctness at the smallest granularity. "
                    "Integration testing verifies that separately tested components work correctly together, identifying issues in component interactions and interfaces. "
                    "System testing validates the complete, integrated system against specified requirements, testing end-to-end functionality and non-functional characteristics. "
                    "Acceptance testing is performed by users or customer representatives to verify the system meets their needs and acceptance criteria. "
                    "Each level uses different test data, environments, and focuses on different failure modes. Test planning must specify which levels are needed "
                    "and what the exit criteria are for each level. Higher levels test from user perspective; lower levels test from developer perspective."
                ),
                "keywords": ["test levels", "unit testing", "integration testing", "system testing", "acceptance testing", "component", "scope"],
            },
            "4.3.1": {
                "title": "Unit Testing",
                "part": 1,
                "clause": "4.3.1",
                "content": (
                    "Unit testing (component testing) verifies individual software units or components in isolation. "
                    "A unit is the smallest testable part of an application (a function, method, class, or module). "
                    "Unit tests are typically written and executed by developers as part of development, often using automated frameworks (JUnit, pytest, xUnit, etc.). "
                    "Unit testing focuses on logic correctness, edge cases, and error handling within a single component. "
                    "Stubs and mocks are used to isolate units from external dependencies. Unit testing is most cost-effective when performed early and continuously, "
                    "as fixing defects at this level costs orders of magnitude less than fixing them in production. Test coverage at unit level should be high (typically 70-90%), "
                    "especially for critical paths and error handling. Unit tests serve as executable documentation of component behavior and enable refactoring with confidence."
                ),
                "keywords": ["unit testing", "component testing", "module", "function", "isolated", "stub", "mock", "automation", "developer testing"],
            },
            "4.3.2": {
                "title": "Integration Testing",
                "part": 1,
                "clause": "4.3.2",
                "content": (
                    "Integration testing verifies that separately tested components or systems work correctly together. "
                    "The focus is on interfaces, data flow between components, and interaction correctness rather than internal logic. "
                    "Integration testing strategies include bottom-up (testing lower-level components first), top-down (testing upper layers first), and big-bang "
                    "(integrating everything at once, less preferred). Sandwich/hybrid approaches combine elements of both. "
                    "Integration testing often reveals issues that unit tests miss: incorrect interface assumptions, data format mismatches, sequencing problems, "
                    "and timing issues. Test environments must simulate realistic interactions. Both automated and manual approaches may be used, depending on "
                    "component dependencies and system architecture. Integration testing is critical for reducing system-level defects and ensuring components "
                    "work as a cohesive whole before system testing begins."
                ),
                "keywords": ["integration testing", "interfaces", "data flow", "component interaction", "bottom-up", "top-down", "sandwich", "coupling"],
            },
            "4.3.3": {
                "title": "System Testing",
                "part": 1,
                "clause": "4.3.3",
                "content": (
                    "System testing validates the complete, fully integrated system against specified requirements. "
                    "It tests the system as a black box, verifying end-to-end functionality, non-functional requirements (performance, security, usability), "
                    "and system behavior under realistic conditions. System testing includes functional testing (does it do what it should?) and non-functional testing "
                    "(performance, load, stress, security, usability, reliability). System testing often occurs in an environment close to production, using realistic data volumes and scenarios. "
                    "This level typically involves QA professionals and may include customer involvement. System testing is where many integration issues surface, as well as "
                    "issues with system design, architecture, and external interface assumptions. Exit criteria for system testing typically require: all critical and high-priority "
                    "defects fixed, acceptable performance and reliability metrics achieved, and stakeholder agreement that system quality is sufficient."
                ),
                "keywords": ["system testing", "end-to-end", "functional", "non-functional", "requirements", "black-box", "production-like", "performance"],
            },
            "4.3.4": {
                "title": "Acceptance Testing",
                "part": 1,
                "clause": "4.3.4",
                "content": (
                    "Acceptance testing is performed by users, customers, or customer representatives to determine whether the system "
                    "meets their needs, requirements, and acceptance criteria. It may be conducted by the customer, internal stakeholders, or a dedicated UAT team. "
                    "Acceptance testing validates business processes and workflows, confirming the system delivers the intended business value. "
                    "It often uses data and scenarios provided by the business, testing the system in ways that mirror actual use. "
                    "Types of acceptance testing include: user acceptance testing (UAT) by business users, operational acceptance testing by operations/support teams, "
                    "and contractual/regulatory acceptance testing. Acceptance testing is the final gate before production release; successful acceptance indicates "
                    "the customer is satisfied with quality and the system is ready for deployment. Issues found at this level often require significant remediation, "
                    "so coordinating with earlier test levels to prevent such findings is important. Clear acceptance criteria defined upfront enable objective pass/fail decisions."
                ),
                "keywords": ["acceptance testing", "UAT", "user acceptance", "business needs", "customer", "fitness for purpose", "business processes"],
            },
            "4.4": {
                "title": "Test Types",
                "part": 1,
                "clause": "4.4",
                "content": (
                    "Test types classify testing based on what aspect of the system is being evaluated. "
                    "Functional testing verifies that the software performs its intended functions correctly, testing requirements and features. "
                    "Non-functional testing evaluates characteristics like performance, security, usability, reliability, and maintainability. "
                    "Structural testing (white-box) examines internal code structure and logic; conformance testing checks compliance with standards; "
                    "confirmation (retesting) verifies that fixes work; regression testing ensures changes didn't break existing functionality. "
                    "Different test types use different techniques, environments, and skill sets. A comprehensive test strategy specifies which test types are needed. "
                    "Functional testing is typically the foundation; non-functional testing becomes critical for systems with specific performance or reliability requirements. "
                    "Confirmation and regression testing are essential whenever changes occur, preventing regressions and ensuring fix quality."
                ),
                "keywords": ["test types", "functional", "non-functional", "structural", "confirmation", "regression", "performance", "security"],
            },
            "4.4.1": {
                "title": "Functional Testing",
                "part": 1,
                "clause": "4.4.1",
                "content": (
                    "Functional testing verifies that software functions work as intended, validating requirements and features. "
                    "It tests what the system does: user interactions, business logic, data processing, and feature completeness. "
                    "Functional testing is typically black-box; testers don't need to know internal implementation. Test cases are derived from requirements, "
                    "use cases, and business rules. Functional testing includes: positive testing (system behaves correctly with valid input), negative testing "
                    "(system handles invalid input gracefully), and boundary testing (system behaves correctly at limits). "
                    "Functional test coverage aims to exercise all major requirements and features at least once. "
                    "Automation of functional tests is often valuable for regression testing. Functional testing is often the largest portion of testing effort "
                    "and is the foundation for other test types. Without adequate functional testing, non-functional testing results may be meaningless."
                ),
                "keywords": ["functional testing", "features", "requirements", "business logic", "positive", "negative", "boundary", "use cases"],
            },
            "4.4.2": {
                "title": "Non-Functional Testing",
                "part": 1,
                "clause": "4.4.2",
                "content": (
                    "Non-functional testing evaluates system characteristics beyond functionality: performance, security, usability, reliability, maintainability, and portability. "
                    "Performance testing measures response time, throughput, and resource utilization under various load conditions. "
                    "Load testing determines system behavior under normal and peak loads; stress testing identifies the breaking point. "
                    "Security testing verifies that the system protects against unauthorized access, data breaches, and other security threats. "
                    "Usability testing assesses user-friendliness and intuitiveness; accessibility testing ensures compliance with standards (WCAG). "
                    "Reliability testing (including soak testing) verifies system stability over extended periods. "
                    "Non-functional testing often requires specialized tools and expertise. Non-functional requirements must be explicitly defined in the test plan with measurable criteria (e.g., 'response time < 2 seconds'). "
                    "Non-functional testing typically occurs after functional testing has established a baseline of functionality."
                ),
                "keywords": ["non-functional", "performance", "security", "usability", "reliability", "load", "stress", "accessibility", "portability"],
            },
            "4.4.3": {
                "title": "Structural and Compliance Testing",
                "part": 1,
                "clause": "4.4.3",
                "content": (
                    "Structural (white-box) testing examines internal code structure, logic, and control flow to ensure all paths are exercised. "
                    "This includes statement testing (every statement executed at least once), branch testing (all decision outcomes tested), "
                    "condition testing (all conditions evaluated), and path testing (critical control flow paths exercised). "
                    "Structural testing is often automated using code coverage tools and is typically performed by developers or QA engineers with code access. "
                    "Conformance testing verifies that software complies with standards, regulations, and specifications (e.g., ISO 26262 for automotive, DO-178C for avionics). "
                    "Compliance testing may also verify adherence to corporate standards and coding guidelines. "
                    "Structural testing complements specification-based testing; together they provide comprehensive coverage. "
                    "For safety-critical systems, structural coverage requirements may be mandated by regulations (e.g., MC/DC for DAL A in DO-178C)."
                ),
                "keywords": ["structural testing", "white-box", "code coverage", "statement", "branch", "condition", "path", "compliance", "standards"],
            },
            "4.4.4": {
                "title": "Confirmation and Regression Testing",
                "part": 1,
                "clause": "4.4.4",
                "content": (
                    "Confirmation (retesting) testing verifies that a previously failing test now passes after a fix is applied. "
                    "It specifically targets the component or feature that was fixed, typically using the same test case that failed. "
                    "Regression testing verifies that changes (fixes, enhancements, refactoring) don't adversely affect previously working functionality. "
                    "Regression tests include a subset of existing test cases, often automated for efficiency. "
                    "Both confirmation and regression testing are essential when code changes occur; without them, fixes can introduce new defects. "
                    "Regression test selection strategies include: retest all (simple but expensive), retest modified code plus impacted areas (moderate), "
                    "or risk-based selection (most efficient but requires risk analysis). Automation is particularly valuable for regression testing "
                    "due to the repeated nature and need for frequent execution. Version control and traceability between requirements, code, and tests "
                    "enable more efficient regression test selection."
                ),
                "keywords": ["confirmation testing", "regression testing", "retesting", "defect fix", "change impact", "retest", "selection strategy"],
            },
            "4.5": {
                "title": "Risk-Based Testing Approach",
                "part": 1,
                "clause": "4.5",
                "content": (
                    "Risk-based testing is a strategic approach where test activities are prioritized based on risk level. "
                    "Instead of testing everything equally, testing effort is focused on areas with higher product risk. "
                    "Product risk is a function of likelihood (probability that a defect exists) and impact (consequence if a defect exists). "
                    "Risk-based testing involves: (1) identifying risks in requirements, architecture, and design, (2) analyzing and prioritizing risks, "
                    "(3) allocating test effort proportionally to risk, and (4) monitoring for emerging risks throughout testing. "
                    "High-risk areas receive more testing, more diverse test techniques, and higher coverage expectations. "
                    "Low-risk areas may receive minimal testing or be tested using less expensive techniques. "
                    "Risk assessment should involve stakeholders (developers, architects, product managers) who understand the system and domain. "
                    "Risk-based testing enables better resource allocation, more effective defect detection, and better prioritization of testing activities."
                ),
                "keywords": ["risk-based testing", "product risk", "likelihood", "impact", "prioritization", "resource allocation", "test focus"],
            },
            "4.6": {
                "title": "Test Independence and Levels of Independence",
                "part": 1,
                "clause": "4.6",
                "content": (
                    "Test independence refers to the degree to which testing is separated from development. "
                    "Independence ranges from no independence (developers test their own code) to complete independence (separate test organization). "
                    "Benefits of independence include: fresh perspective, ability to identify unintended functionality, reduced bias, and credibility with stakeholders. "
                    "Levels of independence: (1) developer testing (low independence, cost-effective for unit testing), (2) independent testers within team, "
                    "(3) independent test group within project, (4) independent test function reporting separately, and (5) external/third-party testing (highest independence). "
                    "System and acceptance testing should have significant independence; unit testing can be performed by developers. "
                    "Some organizations use a hybrid approach: developers do unit/integration testing, independent testers do system/acceptance testing. "
                    "The appropriate level depends on risk level, criticality, and organizational culture. Complete independence can delay feedback but increases objectivity."
                ),
                "keywords": ["test independence", "independence levels", "developer testing", "independent testers", "perspective", "credibility"],
            },
            "4.7": {
                "title": "Static and Dynamic Testing",
                "part": 1,
                "clause": "4.7",
                "content": (
                    "Static testing evaluates software work products without execution: reviewing code, documents, and designs. "
                    "Static testing includes formal reviews, code inspections, walkthroughs, and automated static analysis using tools. "
                    "Benefits: finds defects early (before execution), identifies logical and structural issues, and can find issues dynamic testing might miss. "
                    "Static testing is cost-effective for finding defects compared to dynamic testing. "
                    "Dynamic testing executes the software and observes behavior: unit tests, system tests, integration tests all qualify as dynamic testing. "
                    "Dynamic testing finds failures (observable deviations from expected behavior) but may not find defects if code paths aren't executed. "
                    "Both static and dynamic testing are necessary; they are complementary. Static testing early in development is highly cost-effective. "
                    "A balanced approach uses static testing for requirements, architecture, design, and code reviews, combined with dynamic testing for execution-based verification."
                ),
                "keywords": ["static testing", "dynamic testing", "review", "inspection", "code analysis", "execution", "complementary"],
            },
            "4.8": {
                "title": "Test Basis and Traceability",
                "part": 1,
                "clause": "4.8",
                "content": (
                    "The test basis is the source material from which test cases are derived: requirements documents, design specifications, use cases, "
                    "user stories, acceptance criteria, risk analysis, and standards/regulations. "
                    "A clear, well-defined test basis is essential for meaningful testing. Ambiguous or incomplete test basis leads to inadequate test coverage. "
                    "Requirements traceability links requirements to test cases, ensuring every requirement is tested. "
                    "Traceability also works backward: every test case should trace to a requirement (or design, risk, etc. for derived test cases). "
                    "Traceability enables impact analysis when requirements change: which tests are affected, what retesting is needed? "
                    "Tools like requirement management systems, test management tools, or spreadsheets maintain traceability matrices. "
                    "Bidirectional traceability (requirements to tests, tests to requirements) enables verification that all requirements are tested and no unnecessary tests exist. "
                    "Traceability supports quality metrics: test coverage (% of requirements tested), requirements coverage (% of tests with traceability)."
                ),
                "keywords": ["test basis", "requirements", "traceability", "coverage", "specifications", "user stories", "impact analysis"],
            },
            "4.9": {
                "title": "Test Environment and Test Data",
                "part": 1,
                "clause": "4.9",
                "content": (
                    "The test environment is the hardware, software, and configuration needed to execute tests. "
                    "Test environments should approximate production to detect environment-dependent issues. "
                    "However, test environments often differ from production (smaller scale, different data volumes, simplified configurations). "
                    "Environment setup includes: operating systems, databases, third-party software, networking, security configurations, and monitoring tools. "
                    "Test data consists of inputs used during testing, derived from the test basis or representative of real data. "
                    "Test data should cover normal cases, boundary cases, error cases, and exception scenarios. "
                    "Data preparation may be complex: creating, loading, resetting, masking, and archiving test data. "
                    "Data privacy and security must be protected; production data typically cannot be used in test environments due to compliance requirements. "
                    "Test data management is increasingly important as systems become more data-driven. Automating test data generation and management improves efficiency."
                ),
                "keywords": ["test environment", "test data", "production-like", "data privacy", "data management", "configuration", "setup"],
            },
            "4.10": {
                "title": "V-Model and Test-Development Relationship",
                "part": 1,
                "clause": "4.10",
                "content": (
                    "The V-model describes the relationship between development activities and corresponding test activities at each level. "
                    "On the left side of the V: requirements definition, high-level design, detailed design, implementation. "
                    "On the right side of the V: acceptance testing (verifies requirements), system testing (verifies design), integration testing (verifies component interactions), "
                    "and unit testing (verifies code). Each development level has a corresponding test level. "
                    "Test planning should start when requirements are created, not after development is complete. "
                    "Test design should start during design phases, using design documents to inform test cases. "
                    "This parallel development and testing reduces defect detection costs and enables early quality assessment. "
                    "The V-model applies to waterfall and traditional development models. Agile models compress the V into shorter cycles, testing continuously throughout development. "
                    "Regardless of development model, the principle holds: test each development artifact with the same level of care it's developed."
                ),
                "keywords": ["V-model", "test levels", "development phases", "parallel", "early testing", "requirements", "design", "implementation"],
            },
        },
    },
    "29119-2:2021": {
        "title": "Part 2: Test Processes",
        "part": 2,
        "sections": {
            "5": {
                "title": "Organizational Test Process",
                "part": 2,
                "clause": 5,
                "content": (
                    "The organizational test process establishes and maintains test policies, strategies, and infrastructure at the organization level. "
                    "This process includes: defining test policies that set organizational expectations, developing test strategies that guide testing approaches, "
                    "establishing test environments and infrastructure, managing test resources and competencies, and continuous improvement of testing practices. "
                    "Organizational test policies establish: testing is mandatory, independence levels, entry/exit criteria standards, "
                    "and organizational test metrics and goals. Test strategy defines how different systems will be tested, handling common patterns and risks. "
                    "Organizational processes enable consistency across projects, facilitate knowledge sharing, and optimize resource utilization. "
                    "This process is typically owned by quality or test management but involves stakeholders across the organization. "
                    "Effective organizational testing improves predictability, reduces schedule surprises, and increases product quality."
                ),
                "keywords": ["organization", "policy", "strategy", "infrastructure", "improvement", "consistency", "process"],
            },
            "5.1": {
                "title": "Test Policy Definition",
                "part": 2,
                "clause": "5.1",
                "content": (
                    "A test policy is a high-level document that establishes organizational expectations and principles for testing. "
                    "Test policies address: scope of testing, who is responsible for testing, minimum testing standards, "
                    "independence requirements, test roles and competencies, and testing as part of quality assurance. "
                    "Policies establish non-negotiable requirements (e.g., all safety-critical code must be reviewed) while allowing flexibility in implementation. "
                    "Policies should be endorsed by senior management to ensure organizational commitment. "
                    "Test policies align testing with organizational quality and business goals. "
                    "Policies are typically high-level and stable; strategies and procedures provide more detailed guidance. "
                    "Policy violations should be escalated; exceptions must be approved by management with documented risk acceptance. "
                    "Policies are periodically reviewed and updated to reflect organizational changes, lessons learned, and evolving standards."
                ),
                "keywords": ["policy", "organizational", "expectations", "standards", "governance", "responsibility", "requirements"],
            },
            "5.2": {
                "title": "Test Strategy Development",
                "part": 2,
                "clause": "5.2",
                "content": (
                    "Test strategy at the organizational level defines the general approach to testing for the organization, "
                    "addressing: test levels (which are needed?), test types (what aspects to test?), test techniques (how to design tests?), "
                    "entry/exit criteria (when to start/stop testing?), independence levels, and test metrics. "
                    "Strategy is derived from organizational policies, risk assessment, product portfolio, and resource constraints. "
                    "Strategy should be risk-based: higher-risk systems receive more intensive testing. "
                    "A good strategy balances comprehensiveness with practicality; it guides testing decisions without micromanaging details. "
                    "Organizational strategy may allow for tactical flexibility: different projects may adjust the strategy to fit their context "
                    "while maintaining alignment with organizational principles. "
                    "Strategy documents should be accessible to all stakeholders and reviewed periodically. "
                    "Strategy effectiveness is monitored through metrics: defect detection rates, schedule adherence, and post-release defect rates."
                ),
                "keywords": ["strategy", "test levels", "test types", "techniques", "risk-based", "entry criteria", "exit criteria", "metrics"],
            },
            "6": {
                "title": "Dynamic Test Process (Test Execution Lifecycle)",
                "part": 2,
                "clause": 6,
                "content": (
                    "The dynamic test process describes the activities involved in planning, designing, executing, and reporting on testing. "
                    "This process includes: Test Planning (define scope, approach, resources), Test Analysis & Design (identify test conditions, create test cases), "
                    "Test Implementation (prepare test environment, test data, test execution setup), Test Execution (run tests, observe results), "
                    "Test Incident Reporting (document and track defects), and Test Completion (finalize deliverables, lessons learned). "
                    "These activities are typically conducted in sequence but may overlap and iterate, especially in agile environments. "
                    "The process should be tailored to project context: agile projects compress cycles, waterfall projects may have distinct phases. "
                    "Each activity has defined inputs (what's needed to start), activities (what's done), and outputs (what's produced). "
                    "Process effectiveness is measured through metrics and lessons learned. "
                    "The dynamic test process must be documented, communicated, and consistently followed across the organization."
                ),
                "keywords": ["test process", "planning", "design", "implementation", "execution", "reporting", "lifecycle", "activities"],
            },
            "6.2": {
                "title": "Test Planning",
                "part": 2,
                "clause": "6.2",
                "content": (
                    "Test planning determines the scope, approach, resources, and schedule for testing. "
                    "Inputs to test planning include: project scope and requirements, risk analysis, organizational test strategy, available resources, "
                    "schedule constraints, and budget. "
                    "Test planning activities include: defining test objectives, determining test scope (what's in and out), selecting test approach and techniques, "
                    "identifying test levels and types, determining resource needs (people, tools, environment), developing schedule and timeline, "
                    "identifying risks and contingencies, and defining entry and exit criteria. "
                    "Test plan outputs include: test plan document, resource plan, schedule, risk register, and test approach documentation. "
                    "A good test plan is realistic, achievable, and communicated to all stakeholders. Entry criteria define when testing can begin; exit criteria define when testing is complete. "
                    "Test plans should address: test items, features to test, features not to test, test approach, suspension/resumption criteria, deliverables, environmental needs, "
                    "roles and responsibilities, schedule, and risks/contingencies. Test plans are living documents, updated as project circumstances change."
                ),
                "keywords": ["planning", "scope", "approach", "resources", "schedule", "entry criteria", "exit criteria", "test plan", "risk"],
            },
            "6.2.1": {
                "title": "Test Planning - Inputs and Analysis",
                "part": 2,
                "clause": "6.2.1",
                "content": (
                    "Inputs to test planning provide the foundation for test decisions and resource allocation. "
                    "Key inputs include: project requirements and scope (what must be tested?), risk assessment and risk register (what's risky?), "
                    "organizational test strategy and policies (how do we test?), schedule and budget constraints (resources and timeline?), "
                    "project stakeholders and their interests (who cares? what do they care about?), development approach and lifecycle model (waterfall, agile, iterative?), "
                    "and lessons learned from previous projects (what worked?). "
                    "Test planning analysis involves: assessing testing complexity based on requirements volatility, technical complexity, and domain criticality; "
                    "evaluating resource availability and competencies; and identifying constraints and dependencies. "
                    "Risk-based analysis prioritizes testing: high-risk areas get more testing, low-risk areas get less. "
                    "Early involvement of test stakeholders in planning ensures buy-in and realistic assessments. "
                    "Planning documents should be reviewed and approved by relevant stakeholders before testing begins."
                ),
                "keywords": ["planning inputs", "analysis", "requirements", "risk", "constraints", "resources", "stakeholders", "assessment"],
            },
            "6.2.2": {
                "title": "Test Planning - Scope and Approach Definition",
                "part": 2,
                "clause": "6.2.2",
                "content": (
                    "Test scope defines what will and will not be tested, setting clear boundaries and expectations. "
                    "In scope might include: all critical and high-priority features, all user-facing functionality, key business workflows, "
                    "and integration points with other systems. Out of scope might include: cosmetic UI issues, internal diagnostic tools, "
                    "features under design review, and third-party components that are maintained separately. "
                    "Test approach specifies how testing will be conducted: selected test types (functional, performance, security?), test levels (which levels?), "
                    "test techniques (black-box, white-box, experience-based?), degree of automation, independence levels, and tools. "
                    "Approach should be risk-driven: high-risk areas get more comprehensive approach, low-risk areas get streamlined approach. "
                    "Approach decisions balance thoroughness against practical constraints (time, budget, people). "
                    "Documenting scope and approach ensures shared understanding and enables objective determination of when testing is complete. "
                    "Scope and approach should be traceable to organizational strategy and justified by risk/requirement analysis."
                ),
                "keywords": ["scope", "approach", "in scope", "out of scope", "test types", "test levels", "risk-driven", "boundaries"],
            },
            "6.2.3": {
                "title": "Test Planning - Criteria Definition",
                "part": 2,
                "clause": "6.2.3",
                "content": (
                    "Entry criteria define the preconditions that must be met before testing can begin. "
                    "Examples include: requirements are finalized and approved, test environment is prepared and validated, "
                    "necessary test data is available, test cases are reviewed and approved, and required tools are installed and working. "
                    "Without entry criteria, testing may start prematurely with incomplete or unstable artifacts, wasting effort. "
                    "Exit criteria define the conditions that must be satisfied for testing to be considered complete. "
                    "Examples include: all planned test cases executed, all critical defects resolved, achieved coverage targets, "
                    "performance/reliability requirements met, and sign-off obtained from stakeholders. "
                    "Exit criteria should be measurable and realistic. Vague criteria like 'sufficient testing' or 'no more defects found' are problematic. "
                    "Suspension criteria specify conditions under which testing should pause (e.g., too many blocking defects). "
                    "Resumption criteria specify when testing should resume. Clear criteria enable objective decisions about testing status and completion. "
                    "Criteria should be agreed upon by stakeholders before testing begins."
                ),
                "keywords": ["entry criteria", "exit criteria", "suspension", "resumption", "preconditions", "completion", "measurable", "conditions"],
            },
            "6.3": {
                "title": "Test Design and Specification",
                "part": 2,
                "clause": "6.3",
                "content": (
                    "Test design and specification transform test conditions (derived from requirements and risk analysis) into detailed test cases and scenarios. "
                    "Inputs include: requirements, use cases, acceptance criteria, risk register, and organizational test techniques guidance. "
                    "Test design activities include: identifying test conditions (what needs to be tested?), identifying test cases for each condition, "
                    "determining test data requirements, and prioritizing test cases by risk and importance. "
                    "Test cases specify: test inputs, expected results, test steps, preconditions, and postconditions. "
                    "Well-designed test cases are independent, repeatable, and unambiguous. "
                    "Design activities should use structured techniques: equivalence partitioning, boundary value analysis, decision tables, state transition, etc. "
                    "Test case design should target high-risk areas and requirements with techniques appropriate to the artifact (requirements suggest black-box techniques, code suggests white-box). "
                    "Design should be reviewed for completeness (all requirements covered?), appropriateness (right techniques used?), and quality (clear, testable?). "
                    "Test design occurs in parallel with or immediately after requirements/design phase."
                ),
                "keywords": ["test design", "test specification", "test conditions", "test cases", "scenarios", "inputs", "expected results", "techniques"],
            },
            "6.3.1": {
                "title": "Test Design - Test Condition and Case Identification",
                "part": 2,
                "clause": "6.3.1",
                "content": (
                    "A test condition is an attribute or aspect of the system that can be evaluated by a test. "
                    "Test conditions are derived from requirements, design, risks, and use cases. Examples: 'user can log in with valid credentials', "
                    "'system rejects invalid password', 'system handles timeout gracefully', 'performance is < 2 seconds'. "
                    "For each test condition, one or more test cases are designed. "
                    "A test case is a concrete specification of inputs, execution steps, and expected results. "
                    "Test case design uses techniques appropriate to the artifact: specifications suggest black-box techniques (equivalence partitioning, boundary values), "
                    "design/code suggest white-box techniques (statement/branch coverage, path testing). "
                    "Test cases should be minimal (just enough to test the condition) and independent (can run in any order). "
                    "Test cases should be traceable: which requirement or risk does each test case address? "
                    "Well-designed test cases enable efficient test execution and clear reporting on coverage. "
                    "Test cases are typically organized into test suites by feature, test type, or test level."
                ),
                "keywords": ["test condition", "test case", "identification", "requirement", "derivation", "specification", "execution steps"],
            },
            "6.3.2": {
                "title": "Test Design - Data Identification and Prioritization",
                "part": 2,
                "clause": "6.3.2",
                "content": (
                    "Test data identification determines what data is needed for each test case. "
                    "Test data should cover: normal cases (typical valid input), boundary cases (limits of valid range), error cases (invalid input), "
                    "and exception cases (unexpected conditions). "
                    "Data identification considers: data sources (real data, synthetic, masked production data?), data preparation needs (how to create/load?), "
                    "data reset between tests (ensure test isolation), and data cleanup after testing. "
                    "Sensitive data (personally identifiable information, financial data) must be handled securely and may need masking or anonymization. "
                    "Test case prioritization determines the order and emphasis of testing. "
                    "Prioritization factors include: risk level (test high-risk areas first), requirement criticality (test critical features first), "
                    "dependency order (test prerequisites before dependents), and schedule constraints (test efficiently). "
                    "Risk-based prioritization focuses effort on areas most likely to contain serious defects. "
                    "Prioritization enables efficient resource use: if time/budget is cut, highest-priority tests still get executed."
                ),
                "keywords": ["test data", "identification", "boundary", "error cases", "sensitive data", "prioritization", "risk-based", "order"],
            },
            "6.4": {
                "title": "Test Implementation and Environment Setup",
                "part": 2,
                "clause": "6.4",
                "content": (
                    "Test implementation prepares the test environment and testware (test cases, test data, test scripts, test harnesses) for execution. "
                    "Implementation activities include: setting up test environments (hardware, software, configuration), preparing test data, "
                    "creating test scripts or test execution tools, establishing test data management, implementing test infrastructure (monitoring, logging), "
                    "and validating test readiness. "
                    "Test environment setup involves installing operating systems, databases, third-party software, network configuration, security settings, "
                    "and monitoring/logging tools. Environments should approximate production to detect environment-dependent issues. "
                    "Test data preparation may be complex: creating initial data, defining data reset procedures between tests, "
                    "preparing error scenarios, and ensuring data privacy/security compliance. "
                    "Automation of test implementation (test scripts, data generation) is valuable for regression testing and repeated execution. "
                    "Test environment validation verifies the environment is ready before testing begins. "
                    "Implementation is complete when test cases are executable, test data is prepared, environment is validated, and testing can begin."
                ),
                "keywords": ["implementation", "environment setup", "test data", "infrastructure", "configuration", "validation", "readiness"],
            },
            "6.4.1": {
                "title": "Test Environment Setup - Infrastructure and Configuration",
                "part": 2,
                "clause": "6.4.1",
                "content": (
                    "Test environment infrastructure includes all hardware and software needed to execute tests. "
                    "Infrastructure components: test servers/machines, operating systems, databases, message queues, caching layers, "
                    "third-party integrations, network configuration, security appliances, and monitoring tools. "
                    "Environment configuration includes: firewall rules, user accounts and permissions, authentication/authorization setup, "
                    "SSL certificates, logging levels, performance monitoring setup, and backup/recovery procedures. "
                    "Test environments should be consistent and repeatable; configuration drift (untracked changes) can lead to environment-specific issues. "
                    "Infrastructure-as-code approaches (automated provisioning scripts) improve consistency and efficiency. "
                    "Multiple test environments may exist: development (for developers), integration (for integration testing), staging (close to production), and performance (optimized for load testing). "
                    "Environment differences may be necessary, but should be documented and justified. "
                    "Environment validation verifies all components are installed correctly, networked properly, and function as expected. "
                    "Environment maintenance ensures stability; issues should be quickly resolved to minimize testing delays."
                ),
                "keywords": ["environment", "infrastructure", "configuration", "consistent", "provisioning", "staging", "validation", "maintenance"],
            },
            "6.4.2": {
                "title": "Test Environment Setup - Data Preparation and Management",
                "part": 2,
                "clause": "6.4.2",
                "content": (
                    "Test data preparation creates and manages data needed for testing. "
                    "Test data activities: defining data requirements (what data is needed?), creating initial data sets, loading data into test environment, "
                    "resetting data between tests, archiving data after testing, and managing data lifecycle. "
                    "Test data should be representative of production but may be smaller or simplified. "
                    "Data may come from: real production data (must be masked/anonymized), synthetic generated data (realistic but not real), "
                    "or copies of production data from specific periods (point-in-time snapshots). "
                    "Data reset procedures ensure test isolation: each test starts with known, consistent data state. "
                    "Data reset may be automatic (via database snapshots or scripts) or manual (slower, error-prone). "
                    "Sensitive data (personal information, financial data, credentials) must be handled securely: encryption, masked display, restricted access, "
                    "compliance with regulations (GDPR, HIPAA, PCI DSS). "
                    "Test data management tools automate creation, loading, masking, and reset, improving efficiency and reducing manual effort. "
                    "Data quality is important: garbage data can lead to invalid test results."
                ),
                "keywords": ["test data", "preparation", "management", "synthetic", "reset", "masking", "sensitive", "compliance", "quality"],
            },
            "6.5": {
                "title": "Test Execution",
                "part": 2,
                "clause": "6.5",
                "content": (
                    "Test execution is the process of running test cases, observing results, recording outcomes, and logging issues. "
                    "Execution activities: verifying entry criteria are met, executing test cases in planned order, recording test results "
                    "(pass, fail, blocked, not run), collecting execution metrics, investigating failures, and logging incidents/defects. "
                    "Execution may be manual (tester follows test steps) or automated (test script runs automatically). "
                    "Automated execution is more efficient for regression testing and repetitive tests. Manual execution is better for exploratory testing "
                    "and tests requiring judgment. Most projects use a hybrid approach. "
                    "During execution, test cases may be blocked (cannot proceed due to prerequisite failure), skipped (not applicable), "
                    "or deferred (execution issues, retested later). "
                    "Execution monitoring tracks: number of tests run, passed, failed, blocked; defect discovery rate; and schedule adherence. "
                    "When tests fail, root cause analysis determines: Is the defect in the system (needs fixing) or in the test (needs correcting)? "
                    "Execution is complete when all planned tests are executed and results documented."
                ),
                "keywords": ["execution", "running tests", "manual", "automated", "recording results", "pass", "fail", "blocked", "defects"],
            },
            "6.5.1": {
                "title": "Test Execution - Execution Activities and Progress Tracking",
                "part": 2,
                "clause": "6.5.1",
                "content": (
                    "Test execution activities are performed in a structured, controlled manner to ensure test repeatability and result credibility. "
                    "Before execution starts: verify entry criteria (ready to test?), confirm test environment is stable, ensure test data is prepared, "
                    "review test cases for clarity. During execution: follow test steps precisely, record observations, note any deviations (environment issues, unclear steps). "
                    "Record results immediately: pass (system behaves as expected), fail (system does not meet expected behavior), "
                    "blocked (cannot proceed due to external issue), or skip (test not applicable). "
                    "For failures, record: test case, step that failed, expected vs actual result, severity, reproducibility. "
                    "Progress tracking monitors execution rate: are we on schedule? At current rate, will we complete on time? "
                    "Metrics tracked: tests planned vs executed, pass rate, fail rate, defect discovery rate. "
                    "If execution is falling behind schedule, prioritize remaining high-priority tests or request additional resources. "
                    "If defect discovery is still high late in execution, system quality may be inadequate; may need schedule extension or release delay. "
                    "Execution monitoring enables early identification of quality/schedule issues."
                ),
                "keywords": ["execution activities", "progress tracking", "entry criteria", "recording", "results", "metrics", "monitoring", "schedule"],
            },
            "6.5.2": {
                "title": "Test Execution - Failure Analysis and Root Cause Determination",
                "part": 2,
                "clause": "6.5.2",
                "content": (
                    "When a test fails, immediate analysis determines whether the failure indicates a system defect or a test issue. "
                    "Analysis activities: reproduce the failure independently (is it repeatable?), compare actual vs expected results precisely, "
                    "review test steps for correctness (is the test valid?), check test data (is data as expected?), and verify environment state (is environment stable?). "
                    "Root cause determination: Is the system behavior wrong (product defect) or is the test wrong (test defect)? "
                    "Common test issues: incorrect expected results, wrong test data, test environment issues, test step ambiguity. "
                    "If the test is valid and environment is correct, but behavior doesn't match expectations, a product defect has been found. "
                    "Defect documentation should include: test case executed, failure description, steps to reproduce, expected vs actual, system state, "
                    "severity assessment, and supporting evidence (logs, screenshots, data). "
                    "Severity determines priority: critical defects (blocking functionality) should be fixed immediately, "
                    "high-priority defects should be fixed before release, medium/low can be deferred. "
                    "Reproducibility affects confidence: consistently reproducible defects are taken seriously; intermittent issues are harder to diagnose. "
                    "Root cause analysis is essential for fixing defects correctly and preventing recurrence."
                ),
                "keywords": ["failure analysis", "root cause", "reproduce", "defect", "severity", "priority", "product defect", "test defect"],
            },
            "6.6": {
                "title": "Test Incident Reporting and Defect Tracking",
                "part": 2,
                "clause": "6.6",
                "content": (
                    "Test incident reporting documents issues found during testing: defects, failures, environment problems, and test execution issues. "
                    "A test incident (or defect report) is a documented report of a failure or deviation from expected behavior. "
                    "Incident reporting activities: record incident information (what failed?), describe failure (how to reproduce?), "
                    "assess severity/priority, assign to responsible party, and track status to resolution. "
                    "Incident records should include: unique ID, date/time, tester name, test case, description, expected vs actual, "
                    "steps to reproduce, severity (critical/high/medium/low), status (open/assigned/fixed/resolved/closed), "
                    "assigned to, fix verification method, and resolution notes. "
                    "Severity assessment considers: impact (how much functionality is affected?), workaround (can user work around it?), "
                    "frequency (how often does it occur?), and risk (what's the business impact?). "
                    "High-severity defects are prioritized for immediate fixing; low-severity may be deferred or accepted as-is. "
                    "Tracking monitors incidents: how many open? How many fixed? How long from report to resolution? "
                    "Metrics: incident discovery rate, incident resolution rate, time-to-fix, and reopened incidents (fixed but re-broken). "
                    "Incident trending identifies systemic issues: if many incidents in one area, root cause is likely architectural."
                ),
                "keywords": ["incident reporting", "defect tracking", "bug report", "severity", "priority", "status", "resolution", "metrics"],
            },
            "6.7": {
                "title": "Test Completion and Reporting",
                "part": 2,
                "clause": "6.7",
                "content": (
                    "Test completion marks the end of planned testing and includes finalization of test deliverables and lessons learned. "
                    "Completion activities: verify exit criteria are met (planned tests executed, quality targets met?), "
                    "finalize test logs and reports, document known issues and limitations, archive test work products, "
                    "and conduct lessons-learned review. "
                    "Test completion should not be confused with bug-free status; completion means planned testing activities are finished, "
                    "regardless of defects found. If exit criteria require 'no critical defects', completion is delayed until criteria are met. "
                    "Test deliverables completed: test plan, test design specification, test cases, test logs, test summary report, "
                    "incident log, and lessons learned. "
                    "Test summary report synthesizes testing results: scope of testing, pass/fail rates, defect summary, "
                    "quality assessment (is the system ready for release?), risks/limitations, and recommendations. "
                    "Lessons learned capture: what went well? What could improve? What issues were encountered? "
                    "Archiving preserves test work products for future reference, regression testing, and audit/compliance. "
                    "Completion marks the formal end of a test phase; maintenance testing or post-release support may continue."
                ),
                "keywords": ["completion", "reporting", "exit criteria", "deliverables", "summary report", "lessons learned", "archive"],
            },
        },
    },
    "29119-3:2021": {
        "title": "Part 3: Test Documentation",
        "part": 3,
        "sections": {
            "8": {
                "title": "Test Plan Documentation",
                "part": 3,
                "clause": 8,
                "content": (
                    "A test plan is a comprehensive document defining the scope, approach, resources, and schedule of testing. "
                    "Test plans provide a roadmap for test execution and a baseline for measuring progress and quality. "
                    "Test plans should be created early in the project, ideally when requirements are finalized, and updated as project circumstances change. "
                    "A complete test plan addresses: test objectives, scope (what is and isn't tested), approach and strategy, test levels and types, "
                    "entry and exit criteria, suspension/resumption criteria, test deliverables, resource requirements, schedule and timeline, "
                    "risks and contingencies, and roles and responsibilities. "
                    "Test plan content should be appropriately detailed: too sparse and it's unclear what will be tested, "
                    "too detailed and it becomes a document that's difficult to maintain. "
                    "Test plans should be reviewed and approved by stakeholders before test execution begins. "
                    "A well-structured test plan enables coordinated test execution, provides a baseline for tracking progress, "
                    "and documents test decisions and rationale for future reference."
                ),
                "keywords": ["test plan", "documentation", "scope", "approach", "resources", "schedule", "strategy", "comprehensive"],
            },
            "8.1": {
                "title": "Test Plan - Structure and Content",
                "part": 3,
                "clause": "8.1",
                "content": (
                    "Test plan structure typically includes: introduction (project context, references), test items (what's tested?), "
                    "features to be tested and features not to be tested, test approach (how will testing be done?), "
                    "test levels (unit/integration/system/acceptance?), test types (functional/non-functional/structural?), "
                    "entry and exit criteria (when to start/stop?), suspension and resumption criteria, test deliverables (what documents?), "
                    "environmental needs (hardware, software, data, tools), staffing and resource needs, schedule and timeline, "
                    "roles and responsibilities (who does what?), and risks and contingencies. "
                    "Content should be clear, organized, and accessible. Graphics (diagrams, charts) improve understanding. "
                    "Test plan should be concise enough to be read and understood by all stakeholders, yet complete enough to guide execution. "
                    "Common mistakes: test plans that are too vague (unclear what will be tested), too detailed (become obsolete quickly), "
                    "or divorced from reality (unrealistic timelines/resources). "
                    "Test plans are living documents; they should be updated when significant changes occur (scope changes, resource changes, schedule slippage). "
                    "Version control and change tracking ensure everyone uses the current plan."
                ),
                "keywords": ["test plan structure", "content", "introduction", "scope", "deliverables", "schedule", "roles", "living document"],
            },
            "8.2": {
                "title": "Test Design Specification",
                "part": 3,
                "clause": "8.2",
                "content": (
                    "A test design specification documents the test conditions, test cases, and test data derived from requirements or design. "
                    "It transforms high-level test objectives into concrete test specifications that can be executed. "
                    "Test design specification includes: test conditions (what needs testing?), test cases with inputs and expected results, "
                    "test data specifications, and test case organization (by feature, by test type, by test level). "
                    "For each requirement or risk item, the design spec shows: which test conditions address it? Which test cases test each condition? "
                    "Traceability from requirements to test cases is documented, enabling verification that all requirements are tested. "
                    "Test design specs typically contain: test condition ID, description, related requirement, test cases for the condition, "
                    "test data description, and expected coverage. "
                    "Test cases in the design spec include: test case ID, name, precondition, steps, inputs, expected result, postcondition. "
                    "Test design specs are reviewed for: completeness (all requirements covered?), correctness (test cases valid?), "
                    "clarity (can testers understand and execute?), and appropriateness (techniques match artifact?). "
                    "Design specs form the basis for test execution; unclear specs lead to unclear test results."
                ),
                "keywords": ["test design specification", "test conditions", "test cases", "traceability", "inputs", "expected results", "coverage"],
            },
            "8.3": {
                "title": "Test Case Specification",
                "part": 3,
                "clause": "8.3",
                "content": (
                    "A test case specification documents a single test case in detail, including inputs, steps, and expected results. "
                    "Test cases are the concrete executable specifications for testing. "
                    "Test case specification includes: unique test case ID, descriptive name, preconditions (what must be true to start?), "
                    "test inputs (what data/actions?), test steps (what actions in what order?), expected results (what should happen?), "
                    "and postcondition (what's the state after?). "
                    "Well-written test cases are: independent (can run alone, don't depend on other tests), repeatable (same result each time), "
                    "traceable (linked to requirement or condition), clear (unambiguous), and minimal (just enough to test the condition). "
                    "Test case levels should be appropriate: high-level test cases for system/acceptance testing (broader scope), "
                    "detailed test cases for unit testing (specific logic). "
                    "Test cases should avoid implementation details (don't test 'how', test 'what'). "
                    "Test cases should be organized logically: by feature, by test type, or by priority. "
                    "Test cases evolve as understanding improves; they should be reviewed, updated, and maintained. "
                    "Test case repositories or management tools enable organization, versioning, and traceability."
                ),
                "keywords": ["test case", "specification", "precondition", "steps", "inputs", "expected results", "independent", "repeatable"],
            },
            "8.4": {
                "title": "Test Procedure Specification",
                "part": 3,
                "clause": "8.4",
                "content": (
                    "A test procedure specification documents how to execute a group of test cases, including sequencing, data preparation, "
                    "and execution steps. Test procedures are typically used for manual execution or for complex execution scenarios. "
                    "Test procedure includes: test procedure ID, name, test cases to be executed (in order), preconditions "
                    "(environment state, data), execution steps (how to run the test cases), expected results summary, and postcondition. "
                    "Test procedures are useful when: test cases must run in a specific sequence (one depends on another's result), "
                    "significant setup is required before testing, or multiple test cases share common execution environment/data. "
                    "Test procedures for automated testing: typically represented as test scripts in a test automation framework. "
                    "Test procedures for manual testing: documented steps that a tester follows, often with supporting information (screenshots, references). "
                    "Test procedures should be clear enough that a tester unfamiliar with the system can follow them. "
                    "Procedure documentation should include: purpose (what's being tested?), preconditions, detailed steps with expected observations at each step, "
                    "how to handle different outcomes (pass vs fail scenarios). "
                    "Procedures are executed and results recorded; unmet expected results indicate test failures."
                ),
                "keywords": ["test procedure", "specification", "sequencing", "execution", "manual", "automated", "steps", "environment"],
            },
            "8.5": {
                "title": "Test Log",
                "part": 3,
                "clause": "8.5",
                "content": (
                    "A test log is a record of test execution, documenting test cases executed, results, and issues encountered. "
                    "Test logs provide evidence of test execution and support quality assessment. "
                    "Test log includes: test case ID, execution date/time, tester name, result (pass/fail/blocked/skip), "
                    "notes/observations, and incidents/defects if any. "
                    "Test logs may be: detailed (every step of every test recorded) or summary (just test case result and incidents). "
                    "Level of detail depends on project needs: critical systems may require detailed logs, less critical may use summary logs. "
                    "Electronic test logs (in test management tools) enable automated tracking and metrics generation. "
                    "Test log metrics: number of tests executed, pass rate, fail rate, defect discovery rate, test execution timeline. "
                    "Logs provide traceability: which tests were run? When? By whom? What were the results? "
                    "Logs support root cause analysis of failures: reviewing logs of related test executions may reveal patterns. "
                    "Logs are archived for compliance, audit, and future reference. "
                    "High-quality logs reduce time to resolve execution issues and support post-release defect analysis."
                ),
                "keywords": ["test log", "record", "execution", "results", "evidence", "traceability", "metrics", "documentation"],
            },
            "8.6": {
                "title": "Test Incident Report",
                "part": 3,
                "clause": "8.6",
                "content": (
                    "A test incident report documents an issue discovered during testing: a failure, defect, or problem. "
                    "Incident reports enable communication about issues and tracking toward resolution. "
                    "Incident report includes: incident ID, date/time reported, tester/reporter name, severity/priority, "
                    "description of issue, steps to reproduce, expected vs actual result, system/environment state, "
                    "assigned to (who will fix?), status (open/assigned/in progress/fixed/resolved/closed), "
                    "root cause (if analyzed), resolution, and verification method. "
                    "Severity levels: critical (system unusable), high (major functionality broken), medium (feature doesn't work), "
                    "low (cosmetic, usability issue). Severity drives priority and fix timeline. "
                    "Incident descriptions should be objective, specific, and reproducible. Vague descriptions like 'doesn't work' "
                    "waste time on clarification. Reproducible steps enable developers to see the issue and fix it. "
                    "Incident tracking enables metrics: how many open? How many fixed? Time-to-fix? "
                    "Incident reports are reviewed regularly to assess quality, identify systemic issues, and prioritize fixes. "
                    "Incident status must be updated to keep stakeholders informed of progress. "
                    "Well-managed incident tracking dramatically improves communication and timely issue resolution."
                ),
                "keywords": ["incident report", "defect report", "bug report", "severity", "priority", "reproduction", "tracking", "resolution"],
            },
            "8.7": {
                "title": "Test Summary Report",
                "part": 3,
                "clause": "8.7",
                "content": (
                    "A test summary report synthesizes testing results, providing an overview of testing scope, execution, findings, "
                    "and quality assessment. Summary reports are key communication tools for stakeholders. "
                    "Test summary report includes: executive summary (what was tested? what were the results?), "
                    "test scope and approach, test execution summary (planned vs actual), metrics (pass rate, defect rate, coverage), "
                    "quality assessment (is the system ready?), risks and limitations (what wasn't tested? why?), "
                    "incident summary (critical, high, medium, low severity counts), and recommendations. "
                    "Summary reports should be clear and accessible to non-technical stakeholders: metrics shown graphically (charts, graphs), "
                    "conclusions stated clearly, and recommendations explicit. "
                    "Quality assessment is the critical section: Is the system ready for release? What are the risks? "
                    "Assessment considers: defect discovery rate (still finding many defects?), defect severity distribution "
                    "(are remaining defects low-severity?), requirements coverage (are all critical requirements tested?), "
                    "and schedule/budget (was testing complete as planned?). "
                    "Summary reports are created at test phase completion and provided to decision-makers (product managers, executives). "
                    "Reports document test decisions and rationale, supporting accountability and future decision-making."
                ),
                "keywords": ["test summary report", "executive summary", "metrics", "quality assessment", "risk", "recommendations", "findings"],
            },
            "8.8": {
                "title": "Test Completion Report",
                "part": 3,
                "clause": "8.8",
                "content": (
                    "A test completion report documents the conclusion of testing and provides final assessment of system quality. "
                    "Completion report includes: summary of testing activities, coverage achieved (requirements, code, risks), "
                    "defect summary (total found, by severity, by status), quality metrics and trends, known issues and limitations, "
                    "recommendations for production release or further testing, and lessons learned. "
                    "The report should answer: What was tested? What defects were found? Are critical/major defects resolved? "
                    "What's the quality level compared to entry/exit criteria? Is the system safe to release? "
                    "Completion reports should identify: any remaining risks, workarounds for known issues, "
                    "recommended post-release monitoring or support priorities. "
                    "Lessons learned section captures: what testing approaches worked well? What should be improved? "
                    "What unexpected issues were encountered? What could help future projects? "
                    "Completion report is formal sign-off that testing is complete, supporting release decisions. "
                    "Reports are archived for regulatory compliance, audit trail, and organizational learning. "
                    "High-quality completion reports reduce post-release surprises and support continuous improvement."
                ),
                "keywords": ["completion report", "final assessment", "coverage", "quality metrics", "risks", "lessons learned", "sign-off"],
            },
        },
    },
    "29119-4:2021": {
        "title": "Part 4: Test Techniques",
        "part": 4,
        "sections": {
            "4.1": {
                "title": "Overview of Test Techniques",
                "part": 4,
                "clause": "4.1",
                "content": (
                    "Test techniques are structured approaches to test design, enabling systematic test case derivation with measurable coverage. "
                    "Techniques ensure test cases cover important aspects of the system and complement each other's strengths and weaknesses. "
                    "Three categories of techniques: specification-based (derive tests from requirements/specs), structure-based (derive tests from code structure), "
                    "and experience-based (derive tests from tester expertise). "
                    "Specification-based techniques are applicable before code is written (useful for early testing). "
                    "Structure-based techniques require access to code (useful for comprehensive testing of implemented logic). "
                    "Experience-based techniques leverage tester knowledge and intuition (useful when specs are incomplete). "
                    "Effective test design often combines techniques: use specification-based for requirements coverage, structure-based for code coverage, "
                    "and experience-based to find edge cases. Different systems may emphasize different techniques: safety-critical systems may require "
                    "structure-based (MC/DC) coverage, business systems may emphasize specification-based techniques. "
                    "Technique selection should be driven by risk assessment and project context."
                ),
                "keywords": ["test techniques", "specification-based", "structure-based", "experience-based", "coverage", "systematic"],
            },
            "4.2": {
                "title": "Specification-Based (Black-Box) Techniques",
                "part": 4,
                "clause": "4.2",
                "content": (
                    "Specification-based techniques derive test cases from specifications, requirements, use cases, and acceptance criteria, "
                    "without access to or knowledge of internal implementation. Also called black-box or functional techniques. "
                    "Specification-based techniques can be applied early in development (when only specs exist) and are suitable for any test level. "
                    "Key techniques: Equivalence Partitioning (partition inputs into groups with similar behavior), "
                    "Boundary Value Analysis (test boundaries between partitions), Decision Table Testing (test all combinations of conditions), "
                    "State Transition Testing (test state changes), Use Case Testing (test user workflows), "
                    "Classification Tree Method (structured partitioning), and Pairwise Testing (test important combinations). "
                    "Advantages: applicable early, test from user perspective, don't require code knowledge, find defects in requirements interpretation. "
                    "Disadvantages: may miss internal logic errors, may not achieve high code coverage, may miss obvious error cases. "
                    "Specification-based techniques are practical for most projects and provide good cost-benefit. "
                    "Coverage metrics: requirement coverage (% of requirements tested), use case coverage (% of use cases tested). "
                    "Specification-based techniques are typically the foundation for functional testing."
                ),
                "keywords": ["black-box", "functional", "specification-based", "equivalence partitioning", "boundary value", "decision table"],
            },
            "4.2.1": {
                "title": "Equivalence Partitioning",
                "part": 4,
                "clause": "4.2.1",
                "content": (
                    "Equivalence Partitioning divides input domain into groups (partitions) where all members are expected to behave equivalently. "
                    "The idea: test one representative from each partition (sufficient to uncover defects in partition boundaries). "
                    "Example: password field requires 6-20 characters. Partitions: too short (0-5 chars), valid (6-20 chars), too long (21+ chars). "
                    "Test one password from each partition; defects in boundaries (6, 20) would be caught by separate boundary tests. "
                    "Partitions are based on: input value ranges, discrete values, logical groups from requirements, output ranges. "
                    "Both valid and invalid partitions should be identified and tested. "
                    "Partitioning becomes challenging with complex combinations of inputs; decision tables or pairwise testing may be more appropriate. "
                    "Coverage metric: Equivalence Partitioning coverage = number of partitions tested / total partitions. "
                    "Equivalence Partitioning is simple, effective, and reduces test case count while maintaining reasonable coverage. "
                    "Common mistakes: partitioning that doesn't match actual behavior (input 7 behaves differently than 8 even though same partition), "
                    "or missing important partitions (valid/empty/null might be separate partitions)."
                ),
                "keywords": ["equivalence partitioning", "partitions", "domain", "representative", "boundaries", "valid", "invalid"],
            },
            "4.2.2": {
                "title": "Boundary Value Analysis",
                "part": 4,
                "clause": "4.2.2",
                "content": (
                    "Boundary Value Analysis focuses testing on the boundaries of input partitions, where defects often occur. "
                    "Boundaries are transition points between partitions where behavior changes. "
                    "Example: valid age range 18-65. Boundary values: 17 (just below), 18 (just at), 65 (just at), 66 (just above). "
                    "Testing: 17 should be rejected, 18 should be accepted, 65 should be accepted, 66 should be rejected. "
                    "Defects often occur at boundaries: off-by-one errors, <= vs < mistakes, etc. "
                    "Boundary value analysis can be applied to: input value boundaries, output ranges, time boundaries, loop counts, array indices. "
                    "Boundary testing is more thorough than just testing representative values from partitions. "
                    "Coverage metric: Boundary value coverage = number of boundaries tested / total boundaries. "
                    "Boundary value analysis is practical and cost-effective: relatively few additional test cases (boundaries + representatives). "
                    "For complex systems, boundaries may be numerous; risk-based prioritization focuses on high-risk boundaries. "
                    "Boundary analysis requires understanding domain constraints and expected behavior at limits. "
                    "Common mistakes: testing 18 and 65 but not 17 and 66 (both sides of boundary), or misidentifying boundaries."
                ),
                "keywords": ["boundary value analysis", "boundaries", "limits", "off-by-one", "transition", "edge cases", "coverage"],
            },
            "4.2.3": {
                "title": "Decision Table Testing",
                "part": 4,
                "clause": "4.2.3",
                "content": (
                    "Decision Table Testing (also called cause-effect analysis) systematically tests combinations of conditions and resulting actions. "
                    "Useful when a feature is governed by multiple conditions and the combination matters. "
                    "Example: Bank transfer requires: amount > 0, account has sufficient balance, receiving account exists. "
                    "Decision table lists all combinations: (amount, balance, account) and expected outcome for each combination. "
                    "Benefits: ensures all important combinations are tested, systematically discovers missing logic, documents expected behavior. "
                    "Decision table creates test case for each combination (row), ensuring all combinations tested. "
                    "Tables can be simplified: if not all combinations are possible or important, test only valid/important combinations. "
                    "Coverage metric: Decision table coverage = number of combinations tested / total possible combinations. "
                    "Decision tables scale with number of conditions; with 5 boolean conditions, 2^5 = 32 combinations, many may be tested. "
                    "Risk-based prioritization can reduce combinations: test high-risk combinations thoroughly, low-risk can be sampled. "
                    "Decision tables are valuable for business logic testing where multiple conditions determine outcomes. "
                    "Decision tables must accurately represent requirements; incorrect tables lead to incorrect test cases."
                ),
                "keywords": ["decision table", "cause-effect", "conditions", "combinations", "actions", "logic", "coverage", "outcomes"],
            },
            "4.2.4": {
                "title": "State Transition Testing",
                "part": 4,
                "clause": "4.2.4",
                "content": (
                    "State Transition Testing tests systems that transition between different states in response to events or conditions. "
                    "Applicable to systems with stateful behavior: order processing (created -> paid -> shipped -> delivered), login (logged out -> logged in), "
                    "user account (active -> suspended -> closed). "
                    "State diagrams show: states, transitions (events/actions that cause state changes), and guards (conditions enabling transitions). "
                    "Test cases exercise: valid transitions (allowed state changes), invalid transitions (rejected state changes), "
                    "state-dependent behavior (same action has different effect in different states). "
                    "Coverage metrics: state coverage (all states visited?), transition coverage (all transitions tested?), "
                    "all-pairs coverage (all state pair combinations tested?). "
                    "State transition testing is systematic: identify all states, all transitions, and design tests to exercise each. "
                    "Benefits: ensures state machine behaves correctly, catches missing transitions, detects invalid state combinations. "
                    "Common mistakes: testing only happy path (valid transitions), missing boundary conditions between states, "
                    "or incorrect state diagrams that don't match actual behavior. "
                    "State transition testing is valuable for process-oriented systems, workflow systems, and protocol testing. "
                    "Tools can generate state machines from code or requirements, supporting systematic transition testing."
                ),
                "keywords": ["state transition", "states", "transitions", "state machine", "events", "guards", "workflow", "coverage"],
            },
            "4.2.5": {
                "title": "Use Case Testing",
                "part": 4,
                "clause": "4.2.5",
                "content": (
                    "Use Case Testing derives test cases from use cases that describe user interactions with the system. "
                    "Use cases document: main success scenario (happy path), alternate flows (variations, branching), and exception flows (error cases). "
                    "Each use case becomes a source for multiple test cases: one for main success, one for each alternate/exception. "
                    "Test cases follow use case steps: precondition (initial state?), steps and interactions, postcondition (final state). "
                    "Benefits: tests from user perspective, ensures important user workflows function, uses business language stakeholders understand. "
                    "Use case testing can begin early (from requirements) before detailed design is complete. "
                    "Coverage metric: Use case coverage = use cases with at least one test / total use cases. "
                    "Use case testing is practical for user-facing systems where workflows are well-defined. "
                    "Common mistakes: testing only main success scenario, missing alternate/exception flows, or testing features not relevant to use cases. "
                    "Use case testing is often combined with other techniques: equivalence partitioning for input validation within use cases, "
                    "boundary testing for quantity limits, decision tables for complex conditional logic within use cases. "
                    "Well-written use cases enable comprehensive, user-focused testing. Use cases also serve as documentation for features."
                ),
                "keywords": ["use case testing", "user workflows", "main success", "alternate flows", "exception", "interactions", "scenario"],
            },
            "4.2.6": {
                "title": "Classification Tree and Pairwise Testing",
                "part": 4,
                "clause": "4.2.6",
                "content": (
                    "Classification Tree Method (CTM) structures the input domain hierarchically, identifying relevant classes and sub-classes. "
                    "The tree shows: parameter/class at root, child values representing partitions/classifications. "
                    "Example: Payment method tree: Credit Card (Visa, MasterCard, Amex), Debit Card, Cash, Check. "
                    "Classification trees enable systematic, hierarchical partitioning and visual representation of test space. "
                    "Pairwise Testing (All-Pairs testing) reduces test case count by testing all pairs of parameter values, "
                    "rather than all combinations. With 5 parameters with 5 values each, all combinations = 3125 tests; pairwise ≈ 40 tests. "
                    "Pairwise assumes that defects involve interaction of at most 2 parameters (reasonable for many systems). "
                    "Tools generate pairwise test cases automatically, ensuring coverage efficiency. "
                    "Benefits: reduced test case count (more practical), still covers important interactions, scalable to many parameters. "
                    "Disadvantages: may miss three-way or higher-order interactions (assumed low-risk), less intuitive than other techniques. "
                    "Pairwise testing is valuable when many parameters/conditions exist and comprehensive all-combinations testing is impractical. "
                    "Pairwise testing is often used for configuration testing (many options), feature interaction testing, and combinatorial scenarios."
                ),
                "keywords": ["classification tree", "pairwise testing", "all-pairs", "combinations", "parameters", "efficient", "interactions"],
            },
            "4.3": {
                "title": "Structure-Based (White-Box) Techniques",
                "part": 4,
                "clause": "4.3",
                "content": (
                    "Structure-based techniques derive test cases from internal code structure, logic, and control flow. "
                    "Also called white-box, glass-box, or code-based techniques. Require access to source code. "
                    "Structure-based techniques can identify code paths and logic that specifications don't reveal. "
                    "Key techniques: Statement Testing (execute every statement), Branch/Decision Testing (exercise all branches), "
                    "Condition Testing (exercise all conditions), Modified Condition/Decision Coverage (MC/DC), Path Testing (exercise control flow paths). "
                    "Advantages: thorough coverage of implemented logic, finds unintended code, detects dead code, useful for safety-critical systems. "
                    "Disadvantages: requires code access and technical expertise, expensive, applied after code written, may miss specification defects. "
                    "Coverage metrics: statement coverage (% of statements executed), branch coverage (% of branches taken), "
                    "condition coverage (% of conditions true/false). "
                    "Structure-based techniques complement specification-based: both are needed for comprehensive testing. "
                    "Safety-critical or high-risk systems may require high structure-based coverage (e.g., MC/DC required for DO-178C DAL A). "
                    "Code coverage tools automate coverage measurement, essential for large codebases. "
                    "Structure-based testing is often performed by developers or code-focused QA engineers."
                ),
                "keywords": ["white-box", "structure-based", "code", "coverage", "statement", "branch", "condition", "control flow"],
            },
            "4.3.1": {
                "title": "Statement Testing and Coverage",
                "part": 4,
                "clause": "4.3.1",
                "content": (
                    "Statement Testing (also called line coverage) verifies that every statement in the code is executed at least once. "
                    "Statement coverage = (number of statements executed / total statements) × 100%. "
                    "100% statement coverage means all lines of code have been exercised. However, this doesn't mean all logic is tested. "
                    "Example: if (x > 0) y = 2/x; without branches exercised, division error if x=0 might not be caught. "
                    "Statement testing is foundational: if 70% statement coverage, 30% of code isn't being tested at all. "
                    "Low statement coverage indicates significant untested code; high statement coverage doesn't guarantee high quality. "
                    "Statement coverage is easier to achieve than branch coverage but less thorough. "
                    "Tools measure statement coverage automatically, highlighting unexecuted lines. "
                    "Common reasons for low coverage: error handling code (rarely executed), defensive checks (don't expect to be triggered), "
                    "dead code (unreachable), or features not tested. "
                    "Target statement coverage depends on criticality: non-critical code might target 70%, critical code targets 90%+. "
                    "Statement coverage alone is insufficient for safety-critical systems; branch/condition coverage required. "
                    "Statement testing is foundational but should be combined with branch and condition testing for thorough coverage."
                ),
                "keywords": ["statement testing", "line coverage", "execution", "statements", "unexecuted code", "metrics", "100%"],
            },
            "4.3.2": {
                "title": "Branch and Decision Testing",
                "part": 4,
                "clause": "4.3.2",
                "content": (
                    "Branch Testing (also called decision testing) verifies that all branches of conditional logic are exercised. "
                    "Branch coverage = (number of decision outcomes tested / total possible outcomes) × 100%. "
                    "Examples: if-else statements have two branches (true, false); switch statements have multiple branches. "
                    "100% branch coverage requires: testing conditions when true AND when false. "
                    "Example: if (x > 0) means test x > 0 (true branch) and x ≤ 0 (false branch). "
                    "Branch coverage is more thorough than statement coverage: ensures conditional logic works in both directions. "
                    "However, branch coverage can miss issues with compound conditions: if (a && b), all branches may be true but "
                    "a=true & b=false, a=false & b=true combinations not tested. "
                    "Branch testing is practical and widely used. Most code coverage tools measure branch coverage. "
                    "Targets: non-critical code 80%, critical code 90%+. "
                    "Branch coverage should be accompanied by boundary and equivalence partitioning: focusing branch testing on important conditions. "
                    "Branch testing is often the minimum requirement for code-based testing before system testing. "
                    "Combination of branch testing + specification-based techniques provides good cost-benefit coverage."
                ),
                "keywords": ["branch testing", "decision testing", "outcomes", "conditional", "if-else", "switch", "branches", "coverage"],
            },
            "4.3.3": {
                "title": "Condition Testing and MC/DC Coverage",
                "part": 4,
                "clause": "4.3.3",
                "content": (
                    "Condition Testing focuses on the evaluation of individual conditions within logical expressions. "
                    "Conditions are boolean expressions that evaluate to true/false: x > 5, a != null, isActive && (count > 0). "
                    "Condition coverage requires each condition evaluated true and false. "
                    "Modified Condition/Decision Coverage (MC/DC) is a rigorous form of condition testing that ensures: "
                    "each condition independently affects the decision outcome (no redundant conditions). "
                    "MC/DC requires: exercising all combinations of condition values where each condition independently changes the outcome. "
                    "Example: (a && b) requires tests where a changes outcome (independent of b) and b changes outcome (independent of a). "
                    "MC/DC is more thorough than branch coverage: branch coverage of if (true || false) is 100% with single test; "
                    "MC/DC requires tests showing both conditions independently affect outcome. "
                    "MC/DC is mandated for safety-critical systems: DO-178C DAL A (aviation), IEC 62138 (functional safety), ISO 26262 (automotive). "
                    "MC/DC requires more test cases than branch testing but provides assurance of logical correctness. "
                    "Tools can assist: static analyzers identify independent conditions, coverage tools measure MC/DC coverage. "
                    "MC/DC testing is complex and may require expert testers or developers. "
                    "MC/DC is appropriate for high-risk, safety-critical logic; less critical code may use simpler branch testing."
                ),
                "keywords": ["condition testing", "MC/DC", "modified condition decision coverage", "compound conditions", "independent", "safety-critical"],
            },
            "4.3.4": {
                "title": "Path Testing",
                "part": 4,
                "clause": "4.3.4",
                "content": (
                    "Path Testing (also called basis path testing) focuses on executing important control flow paths through the code. "
                    "A path is a sequence of statements/branches from entry to exit of a function or module. "
                    "With multiple branches, the number of paths grows exponentially: n branches can create 2^n paths. "
                    "Full path coverage (all paths) is often impractical; basis path testing identifies a minimal set of important paths. "
                    "Basis path testing uses cyclomatic complexity: measures the number of independent paths through code. "
                    "Cyclomatic complexity = number of decision points + 1. Function with 3 if-statements and 1 loop: complexity ≈ 5. "
                    "Basis paths are sufficient to exercise all code and decision points without testing all exponential combinations. "
                    "Benefits: focuses on significant paths, manageable test case count, covers important control flow logic. "
                    "Disadvantages: may miss some logic combinations, requires code analysis, more complex than branch testing. "
                    "Path testing is valuable for complex control flow: functions with multiple nested conditions or loops. "
                    "Tools can calculate cyclomatic complexity and identify basis paths. "
                    "Path testing can be combined with other techniques: basis paths focus on control flow, condition testing on logic. "
                    "Path testing is often used in code review and focused testing of complex algorithms."
                ),
                "keywords": ["path testing", "basis path", "cyclomatic complexity", "control flow", "routes", "important paths", "logic"],
            },
            "4.4": {
                "title": "Experience-Based Techniques",
                "part": 4,
                "clause": "4.4",
                "content": (
                    "Experience-based techniques leverage tester knowledge, intuition, and skill to identify important test cases. "
                    "Also called exploratory, heuristic-based, or ad-hoc techniques. Based on tester expertise and system knowledge. "
                    "Key techniques: Error Guessing (anticipate likely errors), Exploratory Testing (systematic exploration with immediate test design), "
                    "Checklist-Based Testing (follow domain knowledge checklists). "
                    "Advantages: finds defects that systematic techniques miss, adaptable to incomplete specifications, captures domain knowledge, "
                    "can test quickly with minimal preparation. "
                    "Disadvantages: dependent on tester skill, less repeatable, hard to measure coverage, may miss important areas, "
                    "difficult to justify test selection to non-technical stakeholders. "
                    "Experience-based techniques are valuable complements to systematic techniques: systematic ensures comprehensiveness, "
                    "experience-based finds edge cases and defects in unexpected areas. "
                    "Effective testing uses combination: systematic techniques for planning/coverage, experience-based for finding unexpected issues. "
                    "Experience-based techniques are particularly valuable when specifications are incomplete or ambiguous. "
                    "Documenting experience-based tests improves repeatability and enables knowledge transfer. "
                    "Experience-based techniques require skilled, knowledgeable testers and should not be primary reliance for critical systems."
                ),
                "keywords": ["experience-based", "exploratory", "error guessing", "checklist", "domain knowledge", "intuition", "ad-hoc"],
            },
            "4.4.1": {
                "title": "Error Guessing and Exploratory Testing",
                "part": 4,
                "clause": "4.4.1",
                "content": (
                    "Error Guessing uses tester knowledge and intuition to anticipate likely errors and design tests for them. "
                    "Based on: previous project experience (where defects have been found?), domain knowledge (what could go wrong?), "
                    "type of system (embedded systems have different risks than business systems), and common failure modes. "
                    "Common errors: off-by-one in loops, uninitialized variables, null pointer dereferences, incorrect operator (= vs ==), "
                    "concurrency issues, resource leaks, exception handling errors. "
                    "Error guessing is informal but valuable: experienced testers intuitively identify risky areas. "
                    "Weakness: unstructured, dependent on individual skill, hard to measure coverage. "
                    "Exploratory Testing combines test design and execution: design tests while testing, react to observations, follow hunches. "
                    "Exploratory testing is structured exploration with immediate feedback: tester understands behavior, continuously refines understanding, "
                    "identifies new test areas as understanding improves. "
                    "Exploratory testing is valuable for: rapidly testing new features, complex systems, incomplete specifications, "
                    "understanding unexpected behavior. "
                    "Exploratory testing works best with skilled testers who understand system behavior and can make quick analysis decisions. "
                    "Time-boxed exploratory testing: allocate 1-2 hours for focused exploration of a feature area. "
                    "Session-based exploratory testing documents: mission (what to test), findings (what was tested, defects found), time spent. "
                    "Exploratory testing is effective complement to scripted testing, especially for understanding complex behavior."
                ),
                "keywords": ["error guessing", "exploratory testing", "intuition", "experience", "unstructured", "hypothesis", "immediate", "feedback"],
            },
            "4.4.2": {
                "title": "Checklist-Based Testing",
                "part": 4,
                "clause": "4.4.2",
                "content": (
                    "Checklist-Based Testing uses domain knowledge captured in structured checklists to guide testing. "
                    "Checklists document commonly important test conditions and areas for a type of system or feature. "
                    "Benefits: efficient (no need to design from scratch), captures best practices and lessons learned, "
                    "ensures important areas aren't missed, useful for less experienced testers, enables consistent testing across projects. "
                    "Checklists are created from: lessons learned from previous projects, industry best practices, domain expertise, "
                    "standards and regulations (if applicable). "
                    "Examples: security testing checklist (SQL injection? XSS? CSRF?), usability checklist (navigation clear? Labels visible? "
                    "Performance adequate?), performance testing checklist (load testing done? Stress testing? Recovery testing?). "
                    "Checklists should be regularly updated: add newly discovered important test conditions, remove obsolete items. "
                    "Checklists are most effective when created by domain experts and refined based on usage and feedback. "
                    "Weakness: checklists can become stale, may not cover novel/emerging risks, may be applied mechanically without understanding. "
                    "Effective use: review checklist items, assess applicability to current system, adapt as needed, document items tested. "
                    "Checklist-based testing is valuable for: teams with mixed experience levels, ensuring quality standards, consistent approach. "
                    "Checklist-based testing often combines with exploratory: use checklist to ensure coverage, add exploratory to find unexpected issues."
                ),
                "keywords": ["checklist-based testing", "domain knowledge", "best practices", "experience", "guidance", "consistency", "structured"],
            },
        },
    },
    "29119-5:2016": {
        "title": "Part 5: Keyword-Driven Testing",
        "part": 5,
        "sections": {
            "1": {
                "title": "Keyword-Driven Testing Framework",
                "part": 5,
                "clause": 1,
                "content": (
                    "Keyword-Driven Testing (KDT), also called table-driven testing, is an approach to test automation that separates test logic "
                    "from test data and automation scripts. Test cases are expressed using keyword commands and data, interpreted by an automation framework. "
                    "A keyword is a reusable action or operation: 'OpenBrowser', 'EnterText', 'ClickButton', 'VerifyText'. "
                    "Test cases are organized in a table: keyword in one column, test data/arguments in other columns. "
                    "Framework interprets keywords and executes corresponding automation code. This separation enables: non-programmers to write test cases, "
                    "easy modification of tests (change keywords/data, not automation code), reusable keywords across many tests, "
                    "maintenance of automation code separate from test logic. "
                    "Benefits: scalable automation, reduced automation code maintenance, enables collaboration between testers and developers, "
                    "faster test case creation and modification. "
                    "Disadvantages: requires framework development effort, keywords must be well-designed, steep learning curve for new framework users. "
                    "KDT is valuable for projects with high test case volume, frequent test modifications, or teams with mixed technical skills. "
                    "KDT is often used with tools like Cucumber (BDD), Robot Framework, or custom frameworks. "
                    "Effective KDT requires: well-designed keywords, comprehensive keyword library, good documentation, and skilled framework developers."
                ),
                "keywords": ["keyword-driven testing", "table-driven", "automation framework", "keywords", "BDD", "reusable", "separation"],
            },
            "2": {
                "title": "Keyword Design and Implementation",
                "part": 5,
                "clause": 2,
                "content": (
                    "Keyword design is critical to effective KDT. Keywords should be: atomic (single, well-defined action), reusable across tests, "
                    "clear and descriptive (test case understandable without seeing automation code), and independent (don't depend on other keywords). "
                    "Keyword library should include: UI interaction (Click, Type, Verify), navigation (GoToPage, NavigateTo), "
                    "data handling (LoadData, ValidateData), wait conditions (WaitForElement), assertions/verification (AssertEqual, VerifyVisible). "
                    "Keywords should have consistent naming and parameter conventions. "
                    "Keyword implementation requires: mapping keyword to automation code, handling parameters/arguments, error handling and reporting. "
                    "A well-designed keyword library is foundational: poor keywords lead to complex, hard-to-maintain test cases. "
                    "As keyword library grows, documentation and version control become important. "
                    "Keyword maintenance: add new keywords as new actions/patterns emerge, remove/deprecate unused keywords, refactor keywords "
                    "as underlying technology changes. "
                    "Effective keyword design enables: non-technical testers to write automated tests, rapid test creation and modification, "
                    "reusable test assets across projects. "
                    "Common challenges: keyword scope creep (keywords become too complex), inconsistent design (similar actions with different keywords), "
                    "inadequate documentation (testers unclear what keywords do)."
                ),
                "keywords": ["keyword design", "keyword library", "atomic", "reusable", "parameters", "implementation", "documentation"],
            },
            "3": {
                "title": "Behavior-Driven Development (BDD) and Gherkin Syntax",
                "part": 5,
                "clause": 3,
                "content": (
                    "Behavior-Driven Development (BDD) extends TDD with business-readable test specifications. BDD tests are written in natural language "
                    "using Gherkin syntax, enabling non-technical stakeholders to understand and contribute to test cases. "
                    "Gherkin keywords: 'Feature' (describes functionality), 'Scenario' (test case), 'Given' (precondition), 'When' (action), "
                    "'Then' (expected result). "
                    "Example: Feature: User Login, Scenario: Login with valid credentials, Given: user is on login page, When: user enters credentials, "
                    "Then: user is logged in. "
                    "Gherkin syntax bridges communication gap between business, testers, and developers. Business can review test scenarios, "
                    "developers implement step definitions, testers automate steps. "
                    "BDD frameworks (Cucumber, Behave, SpecFlow) map Gherkin text to automation code. Step definitions translate Given/When/Then "
                    "to automation actions. "
                    "Benefits: readable test cases, executable specifications, shared understanding between business/dev/QA, documentation of behavior. "
                    "Disadvantages: requires discipline in scenario writing (should be clear, focused, implementable), step definition maintenance. "
                    "Effective BDD requires: clear, business-focused scenario writing; reusable step definitions; good communication between stakeholders. "
                    "BDD is particularly valuable for business-logic-heavy systems where clear specification of behavior is important. "
                    "BDD works well with agile development where requirements are continuously refined."
                ),
                "keywords": ["BDD", "behavior-driven", "Gherkin", "Given-When-Then", "scenario", "executable specifications", "Cucumber"],
            },
        },
    },
}
