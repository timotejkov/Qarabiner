"""Domain-specific standards: Automotive."""

STANDARD_ID = "Automotive Standards"

SECTIONS: dict[str, dict] = {
    "iso_26262": {
        "title": "ISO 26262 — Functional Safety for Road Vehicles",
        "sections": {
            "asil": {
                "title": "Automotive Safety Integrity Levels (ASIL)",
                "content": (
                    "ASIL A: Lowest safety requirement. Statement coverage sufficient. "
                    "ASIL B: Branch coverage required. Semi-formal verification methods. "
                    "ASIL C: Branch coverage + MC/DC recommended. Formal verification encouraged. "
                    "ASIL D: Highest safety requirement. MC/DC coverage mandatory. "
                    "Formal verification methods required. Back-to-back testing between model and code. "
                    "ASIL decomposition allows splitting a high ASIL into lower ASIL requirements "
                    "across redundant elements."
                ),
                "keywords": ["ASIL", "safety", "coverage", "MC/DC", "formal verification", "decomposition"],
            },
            "part6_sw": {
                "title": "Part 6: Product Development at the Software Level",
                "content": (
                    "Software unit testing: verify software units against detailed design. "
                    "Software integration testing: verify interactions between software components. "
                    "Software testing in the target environment. "
                    "Methods: requirements-based testing, interface testing, fault injection testing, "
                    "resource usage testing, back-to-back comparison testing."
                ),
                "keywords": ["unit testing", "integration", "fault injection", "back-to-back", "target environment"],
            },
            "part8_safety": {
                "title": "Part 8: Supporting Processes",
                "content": (
                    "Configuration management, change management, verification, documentation, "
                    "qualification of software tools, qualification of software components. "
                    "Tool Confidence Level (TCL) determines qualification effort required. "
                    "All safety-relevant changes require impact analysis and re-testing."
                ),
                "keywords": ["configuration", "change management", "tool qualification", "TCL", "impact analysis"],
            },
        },
    },
    "aspice": {
        "title": "Automotive SPICE (ASPICE) v3.1",
        "sections": {
            "swt": {
                "title": "SWE.4 — Software Unit Verification",
                "content": (
                    "Verify software units against the software detailed design. "
                    "Define unit verification strategy, criteria, and test cases. "
                    "Perform static verification (code review, static analysis). "
                    "Perform dynamic verification (unit testing). "
                    "Ensure bidirectional traceability between test cases and detailed design."
                ),
                "keywords": ["ASPICE", "unit verification", "static analysis", "traceability"],
            },
            "swi": {
                "title": "SWE.5 — Software Integration and Integration Testing",
                "content": (
                    "Integrate software units into larger assemblies per integration strategy. "
                    "Verify integrated software against architectural design. "
                    "Regression testing after each integration step. "
                    "Traceability from integration tests to architectural design elements."
                ),
                "keywords": ["ASPICE", "integration", "regression", "architecture", "strategy"],
            },
            "sqt": {
                "title": "SWE.6 — Software Qualification Testing",
                "content": (
                    "Verify the integrated software against software requirements. "
                    "Tests executed in the target environment or a representative simulation. "
                    "Full requirements coverage through qualification test cases. "
                    "Bidirectional traceability: requirements ↔ test cases ↔ test results."
                ),
                "keywords": ["ASPICE", "qualification", "target environment", "requirements coverage"],
            },
        },
    },
}
