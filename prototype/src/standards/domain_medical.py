"""Domain-specific standards: Medical Devices / Healthcare IT."""

STANDARD_ID = "Medical Device Standards"

SECTIONS: dict[str, dict] = {
    "iec_62304:2015": {
        "title": "IEC 62304:2015 — Medical Device Software Lifecycle Processes",
        "sections": {
            "5.1": {
                "title": "Software Development Planning",
                "content": (
                    "The manufacturer shall establish a software development plan covering: "
                    "software development process, software development standards and methods, "
                    "software tools, traceability between system requirements and software items. "
                    "The plan must include verification and validation activities mapped to risk class."
                ),
                "keywords": ["development plan", "traceability", "verification", "validation", "medical"],
            },
            "5.5": {
                "title": "Software Integration and Integration Testing",
                "content": (
                    "Software integration testing shall verify that software items work correctly "
                    "together when integrated. Test cases must be derived from architectural design. "
                    "For Class B and C software, integration test results must be evaluated against "
                    "acceptance criteria and documented."
                ),
                "keywords": ["integration testing", "software items", "Class B", "Class C", "architecture"],
            },
            "5.7": {
                "title": "Software System Testing",
                "content": (
                    "System testing verifies that the integrated software system meets software "
                    "requirements. Tests must demonstrate all software requirements are met. "
                    "Anomalies must be evaluated. For Class C: complete requirements traceability mandatory."
                ),
                "keywords": ["system testing", "requirements", "traceability", "anomalies"],
            },
            "risk_classes": {
                "title": "Software Safety Classification",
                "content": (
                    "Class A: No injury or damage to health. Minimal lifecycle requirements. "
                    "Class B: Non-serious injury. Requires documented V&V, integration testing. "
                    "Class C: Death or serious injury possible. Full lifecycle requirements — "
                    "complete traceability matrix, unit testing, integration testing, system testing, "
                    "regression testing after changes, detailed problem resolution process."
                ),
                "keywords": ["Class A", "Class B", "Class C", "safety", "risk classification"],
            },
        },
    },
    "fda_csa:2025": {
        "title": "FDA Computer Software Assurance (CSA) Guidance — 2025",
        "content": (
            "CSA replaces the traditional CSV (Computer System Validation) approach. "
            "Risk-based approach: more assurance activities for higher-risk software. "
            "Emphasizes critical thinking over documentation volume. "
            "Allows unscripted testing (ad-hoc, exploratory) for lower-risk functions. "
            "Scripted testing still required for highest-risk software functions."
        ),
        "sections": {
            "risk_based": {
                "title": "Risk-Based Assurance",
                "content": (
                    "Assurance activities should be commensurate with risk. "
                    "High-risk: scripted testing with documented evidence. "
                    "Medium-risk: combination of scripted and unscripted. "
                    "Low-risk: unscripted testing, peer review, exploratory testing acceptable."
                ),
                "keywords": ["CSA", "risk-based", "assurance", "scripted", "unscripted", "FDA"],
            },
        },
    },
    "hipaa": {
        "title": "HIPAA — Health Insurance Portability and Accountability Act",
        "sections": {
            "security_rule": {
                "title": "HIPAA Security Rule — Technical Safeguards",
                "content": (
                    "Access control: unique user identification, emergency access, automatic logoff, "
                    "encryption. Audit controls: mechanisms to record and examine access to ePHI. "
                    "Integrity: protect ePHI from improper alteration or destruction. "
                    "Transmission security: encrypt ePHI in transit. "
                    "Testing must verify all technical safeguards are implemented and effective."
                ),
                "keywords": ["HIPAA", "ePHI", "access control", "audit", "encryption", "healthcare"],
            },
        },
    },
}
