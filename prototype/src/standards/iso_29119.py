"""
ISO/IEC/IEEE 29119 — Software Testing Standard.

Curated key sections for prototype use. This is NOT the full standard text
(which is proprietary). These are summaries of publicly available concepts
and principles from the standard's scope and published abstracts.

In production, this would be replaced by a Vector DB with licensed content.
"""

STANDARD_ID = "ISO/IEC/IEEE 29119"

SECTIONS: dict[str, dict] = {
    "29119-1:2022": {
        "title": "Part 1: General Concepts",
        "sections": {
            "1": {
                "title": "Scope",
                "content": (
                    "Defines concepts and vocabulary for software testing. "
                    "Establishes the foundation for all other parts of ISO 29119. "
                    "Applicable to testing in all software development lifecycle models."
                ),
                "keywords": ["concepts", "vocabulary", "testing", "lifecycle"],
            },
            "4.1": {
                "title": "What is Testing?",
                "content": (
                    "Testing is the process consisting of all lifecycle activities, both static and dynamic, "
                    "concerned with planning, preparation, and evaluation of a component or system and related "
                    "work products to determine that they satisfy specified requirements, to demonstrate that "
                    "they are fit for purpose, and to detect defects."
                ),
                "keywords": ["definition", "testing", "static", "dynamic", "evaluation"],
            },
            "4.5": {
                "title": "Risk-Based Testing",
                "content": (
                    "Risk-based testing is an approach to testing where test activities, including test design, "
                    "are prioritized based on the level of risk. Risks are identified, analyzed, and used to "
                    "guide the test effort. Higher-risk areas receive more testing attention. "
                    "Product risk = likelihood of defect x impact of defect."
                ),
                "keywords": ["risk", "prioritization", "risk-based", "product risk"],
            },
        },
    },
    "29119-2:2021": {
        "title": "Part 2: Test Processes",
        "sections": {
            "5": {
                "title": "Organizational Test Process",
                "content": (
                    "Defines the organizational-level test process that establishes and maintains "
                    "test policies, test strategies, and organizational test specifications. "
                    "Includes test policy definition, organizational test strategy, and test process improvement."
                ),
                "keywords": ["organization", "policy", "strategy", "process"],
            },
            "6.2": {
                "title": "Test Planning",
                "content": (
                    "Test planning determines the scope, approach, resources, and schedule of testing activities. "
                    "The test plan identifies the items to be tested, features to be tested, testing tasks, "
                    "who will do each task, and any risks requiring contingency planning. "
                    "A test plan addresses: test objectives, test scope, test approach, entry criteria, "
                    "exit criteria, suspension and resumption criteria, deliverables, and resource needs."
                ),
                "keywords": ["planning", "scope", "approach", "resources", "schedule", "entry criteria", "exit criteria"],
            },
            "6.3": {
                "title": "Test Monitoring and Control",
                "content": (
                    "Test monitoring compares actual progress against the test plan. "
                    "Test control involves taking corrective actions when monitoring shows deviation. "
                    "Key metrics: test case execution rate, defect discovery rate, defect density, "
                    "test coverage, and schedule adherence."
                ),
                "keywords": ["monitoring", "control", "metrics", "coverage", "defect rate"],
            },
            "6.4": {
                "title": "Test Design and Implementation",
                "content": (
                    "Test design transforms test conditions into test cases and other testware. "
                    "Test implementation organizes and prioritizes test cases, creates test data, "
                    "sets up test environments, and prepares test harnesses."
                ),
                "keywords": ["design", "implementation", "test cases", "test data", "environment"],
            },
            "7": {
                "title": "Test Strategy",
                "content": (
                    "A test strategy defines the general approach to testing for a project. "
                    "It specifies the test levels (component, integration, system, acceptance), "
                    "the test types (functional, non-functional, structural, confirmation, regression), "
                    "the test design techniques to use, entry and exit criteria, and the degree of independence. "
                    "The strategy must be risk-based, using product risk analysis to prioritize testing effort."
                ),
                "keywords": ["strategy", "test levels", "test types", "techniques", "risk-based"],
            },
        },
    },
    "29119-3:2021": {
        "title": "Part 3: Test Documentation",
        "sections": {
            "8": {
                "title": "Test Plan Documentation",
                "content": (
                    "Defines the structure and content of test plan documents. "
                    "A test plan should contain: test plan identifier, introduction, test items, "
                    "features to be tested, features not to be tested, approach, item pass/fail criteria, "
                    "suspension/resumption criteria, test deliverables, environmental needs, responsibilities, "
                    "staffing and training needs, schedule, and risks and contingencies."
                ),
                "keywords": ["documentation", "test plan", "template", "deliverables"],
            },
            "9": {
                "title": "Test Status Report",
                "content": (
                    "Defines content for test status reports: summary of testing activities, "
                    "deviations from the test plan, metrics (tests run, passed, failed, blocked), "
                    "assessment of test item quality, and impediments."
                ),
                "keywords": ["status", "report", "metrics", "assessment"],
            },
        },
    },
    "29119-4:2021": {
        "title": "Part 4: Test Techniques",
        "sections": {
            "4.2": {
                "title": "Specification-based (Black-box) Techniques",
                "content": (
                    "Techniques that derive test cases from the specification: "
                    "Equivalence Partitioning, Boundary Value Analysis, Decision Table Testing, "
                    "State Transition Testing, Classification Tree Method, Pairwise Testing, "
                    "Use Case Testing. Each technique has defined coverage criteria."
                ),
                "keywords": ["black-box", "equivalence", "boundary", "decision table", "state transition"],
            },
            "4.3": {
                "title": "Structure-based (White-box) Techniques",
                "content": (
                    "Techniques that derive test cases from internal structure: "
                    "Statement Testing, Branch/Decision Testing, Condition Testing, "
                    "Modified Condition/Decision Coverage (MC/DC), Path Testing. "
                    "MC/DC is required for safety-critical systems (DO-178C DAL A, ISO 26262 ASIL D)."
                ),
                "keywords": ["white-box", "statement", "branch", "MC/DC", "path", "coverage"],
            },
            "4.4": {
                "title": "Experience-based Techniques",
                "content": (
                    "Techniques leveraging tester expertise: Error Guessing, "
                    "Exploratory Testing, Checklist-based Testing. "
                    "These complement systematic techniques and are particularly useful "
                    "when specifications are incomplete."
                ),
                "keywords": ["experience", "exploratory", "error guessing", "checklist"],
            },
        },
    },
}
