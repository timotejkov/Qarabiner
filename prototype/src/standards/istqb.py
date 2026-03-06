"""
ISTQB Syllabi — Test design techniques, risk-based testing, lifecycle.

Covers Foundation, Advanced Test Manager, and Advanced Test Analyst concepts.
"""

STANDARD_ID = "ISTQB"

SECTIONS: dict[str, dict] = {
    "foundation": {
        "title": "ISTQB Certified Tester Foundation Level (CTFL) v4.0",
        "sections": {
            "1.1": {
                "title": "What is Testing?",
                "content": (
                    "Testing is a way to assess the quality of software and reduce the risk of software failure. "
                    "Testing involves activities such as planning, analysis, design, implementation, execution, "
                    "and completion. Testing is not only executing tests. It includes reviewing work products "
                    "such as requirements, user stories, designs, and code."
                ),
                "keywords": ["testing", "quality", "risk", "activities"],
            },
            "2.1": {
                "title": "Software Development Lifecycle and Testing",
                "content": (
                    "Testing does not exist in isolation. Test activities are related to software development "
                    "activities. Different development lifecycle models (V-model, iterative, agile) "
                    "require different testing approaches. For every development activity, there is a "
                    "corresponding test activity. Test levels: component testing, integration testing, "
                    "system testing, acceptance testing."
                ),
                "keywords": ["lifecycle", "V-model", "agile", "test levels", "component", "integration", "system", "acceptance"],
            },
            "2.2": {
                "title": "Test Levels",
                "content": (
                    "Component Testing: tests individual components in isolation. "
                    "Integration Testing: tests interfaces and interactions between components/systems. "
                    "System Testing: tests the complete integrated system against requirements. "
                    "Acceptance Testing: validates the system meets business requirements and is ready for deployment. "
                    "Each level has specific objectives, test basis, test objects, defects and failures, and approaches."
                ),
                "keywords": ["component", "integration", "system", "acceptance", "test levels"],
            },
            "2.3": {
                "title": "Test Types",
                "content": (
                    "Functional Testing: tests what the system does (features, functions). "
                    "Non-functional Testing: tests how well the system behaves (performance, usability, security). "
                    "Black-box Testing: based on specification without internal structure knowledge. "
                    "White-box Testing: based on internal structure (code). "
                    "Confirmation Testing: verifies that a fixed defect is truly resolved. "
                    "Regression Testing: verifies that changes haven't introduced new defects."
                ),
                "keywords": ["functional", "non-functional", "black-box", "white-box", "regression", "confirmation"],
            },
            "4.2": {
                "title": "Black-box Test Techniques",
                "content": (
                    "Equivalence Partitioning (EP): divides input data into partitions where all values "
                    "should be treated the same; one test per partition. "
                    "Boundary Value Analysis (BVA): tests at the boundaries of equivalence partitions "
                    "where defects are most likely. "
                    "Decision Table Testing: tests combinations of conditions and their resulting actions. "
                    "State Transition Testing: tests transitions between states triggered by events. "
                    "Use Case Testing: tests complete business scenarios."
                ),
                "keywords": ["equivalence", "boundary", "decision table", "state transition", "use case", "EP", "BVA"],
            },
            "4.3": {
                "title": "White-box Test Techniques",
                "content": (
                    "Statement Coverage: every executable statement exercised at least once. "
                    "Branch Coverage: every branch (decision outcome) exercised at least once. "
                    "100% branch coverage implies 100% statement coverage but not vice versa. "
                    "Higher coverage criteria (MC/DC, path coverage) exist for safety-critical systems."
                ),
                "keywords": ["statement coverage", "branch coverage", "MC/DC", "white-box"],
            },
            "5.1": {
                "title": "Risk-Based Testing and Test Prioritization",
                "content": (
                    "Product risk analysis identifies and assesses product risks to guide test effort allocation. "
                    "Risk level = likelihood x impact. Higher-risk items are tested first and more thoroughly. "
                    "Risk categories include: functional (incorrect calculations, missing features), "
                    "non-functional (poor performance, security vulnerabilities), and structural risks."
                ),
                "keywords": ["risk", "prioritization", "risk-based", "likelihood", "impact"],
            },
        },
    },
    "advanced_test_manager": {
        "title": "ISTQB Advanced Level Test Manager (CTAL-TM)",
        "sections": {
            "2.3": {
                "title": "Test Estimation",
                "content": (
                    "Estimation approaches: metrics-based (historical data, defect density) and "
                    "expert-based (Wideband Delphi, planning poker). "
                    "Factors affecting effort: product complexity, process maturity, tool support, "
                    "people skills, environmental factors, quality requirements."
                ),
                "keywords": ["estimation", "effort", "complexity", "metrics"],
            },
            "3.1": {
                "title": "Test Process Management",
                "content": (
                    "Managing the test process includes: establishing the test policy and strategy, "
                    "planning, monitoring and controlling, and implementing process improvements. "
                    "Test manager responsibilities: resource allocation, risk management, "
                    "stakeholder communication, and metrics reporting."
                ),
                "keywords": ["management", "process", "resource", "stakeholder"],
            },
            "4.1": {
                "title": "Defect Management",
                "content": (
                    "Defect lifecycle: detected → reported → analyzed → prioritized → assigned → "
                    "fixed → retested → closed. Defect metrics: defect density, defect detection "
                    "percentage, defect age, defect removal efficiency. "
                    "Root cause analysis identifies systemic issues."
                ),
                "keywords": ["defect", "bug", "lifecycle", "root cause", "metrics"],
            },
        },
    },
    "advanced_test_analyst": {
        "title": "ISTQB Advanced Level Test Analyst (CTAL-TA)",
        "sections": {
            "3.2": {
                "title": "Test Design Techniques — Application",
                "content": (
                    "Selecting appropriate test design techniques based on the test item: "
                    "For business logic: decision table testing, state transition testing. "
                    "For input validation: equivalence partitioning, boundary value analysis. "
                    "For workflows: use case testing, activity diagram-based testing. "
                    "For complex algorithms: classification tree method, pairwise testing. "
                    "Techniques should be combined based on risk level and test objectives."
                ),
                "keywords": ["techniques", "selection", "business logic", "input validation", "workflow"],
            },
            "4.1": {
                "title": "Non-functional Testing — Quality Characteristics",
                "content": (
                    "Non-functional testing verifies ISO 25010 quality characteristics: "
                    "Performance testing (load, stress, endurance, spike, scalability), "
                    "Usability testing (effectiveness, efficiency, satisfaction), "
                    "Reliability testing (maturity, availability, fault tolerance, recoverability), "
                    "Security testing (confidentiality, integrity, non-repudiation, accountability, authenticity), "
                    "Maintainability testing (code analysis, testability review), "
                    "Portability testing (installation, adaptation, migration)."
                ),
                "keywords": ["non-functional", "performance", "load", "stress", "usability", "reliability", "security"],
            },
        },
    },
}
