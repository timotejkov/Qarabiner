"""Domain-specific standards: Automotive."""

STANDARD_ID = "Automotive Standards"

SECTIONS: dict[str, dict] = {
    "iso_26262": {
        "title": "ISO 26262 — Functional Safety for Road Vehicles",
        "content": (
            "ISO 26262 establishes functional safety requirements for electrical/electronic systems in road vehicles. "
            "The standard applies to systems where failure could result in hazardous situations affecting vehicle occupants or road users. "
            "ISO 26262 uses Automotive Safety Integrity Level (ASIL) assignments based on risk analysis to determine appropriate verification and validation rigor. "
            "The standard is organized in parts addressing different aspects: Part 1 (Vocabulary), Part 2 (Management of Functional Safety), Part 3 (Concept Phase), "
            "Part 4 (Product Development at System Level), Part 5 (Product Development at Hardware Level), Part 6 (Product Development at Software Level), "
            "Part 7 (Production, Operation, Service, Decommissioning), Part 8 (Supporting Processes), and Part 9 (Automotive SPICE and Functional Safety Assessment). "
            "ISO 26262 compliance requires systematic hazard analysis, comprehensive verification and validation, documentation of design decisions, and continuous "
            "monitoring for safety-related issues throughout the vehicle lifecycle."
        ),
        "sections": {
            "asil_determination": {
                "title": "ASIL Determination and Classification",
                "part": "Part 3: Concept Phase",
                "clause": "3.5 (with Part 2)",
                "content": (
                    "ASIL assignment is based on risk analysis combining three factors: severity (potential harm level), exposure (likelihood of hazardous situation), "
                    "and controllability (ability to mitigate harm after hazardous situation). Severity ranges from S0 (no injury) to S3 (fatal injury). Exposure ranges "
                    "from E0 (improbable in vehicle lifetime) to E4 (high probability of occurrence). Controllability ranges from C0 (easily controlled) to C3 (uncontrollable). "
                    "The combination determines ASIL: QM (non-safety-relevant), ASIL A (lowest), ASIL B, ASIL C, or ASIL D (highest). For example, S3 + E4 + C3 results in "
                    "ASIL D. ASIL decomposition allows splitting ASIL D into multiple ASIL A or B requirements distributed across redundant elements, reducing verification burden "
                    "if independence and appropriate monitoring can be demonstrated. Functional safety requirement specifications must clearly state the assigned ASIL. Re-assessment "
                    "may be necessary if system design changes or if new hazards are identified during development."
                ),
                "keywords": ["ASIL", "risk analysis", "severity", "exposure", "controllability", "ASIL A", "ASIL B", "ASIL C", "ASIL D", "decomposition"],
            },
            "software_unit_testing": {
                "title": "Software Unit Testing Requirements by ASIL",
                "part": "Part 6: Product Development at Software Level",
                "clause": "6.5, Table 6.3",
                "content": (
                    "Software unit testing verifies that individual software units (functions, modules) conform to detailed design specifications. ASIL A requires basic "
                    "unit testing with statement coverage sufficient to demonstrate design conformance. ASIL B requires branch coverage ensuring all code paths are tested. "
                    "ASIL C requires branch coverage plus emphasis on testing error handling and boundary conditions. ASIL D requires Modified Condition Decision Coverage (MC/DC) "
                    "where each condition is tested to affect the outcome independently, ensuring comprehensive control flow verification. Unit testing requires test cases "
                    "derived from detailed design specifications, with clear expected outputs documented. Test harnesses may be needed to isolate units for testing. Stubs and "
                    "mocks simulate dependencies. Test results must demonstrate that all requirements are met and coverage metrics are achieved. Dynamic analysis tools measure "
                    "coverage. Static analysis complements unit testing by detecting defects without execution. For ASIL C and D, requirements traceability ensures every "
                    "detailed design element is tested."
                ),
                "keywords": ["unit testing", "statement coverage", "branch coverage", "MC/DC", "ASIL A", "ASIL B", "ASIL C", "ASIL D", "test harness", "traceability"],
            },
            "software_integration_testing": {
                "title": "Software Integration and System Testing",
                "part": "Part 6: Product Development at Software Level",
                "clause": "6.6, 6.7",
                "content": (
                    "Software integration testing verifies that software units work correctly together and that interfaces function as designed. Integration proceeds "
                    "incrementally from simpler to more complex assemblies according to an integration strategy. Interface testing validates data flow, signal timing, "
                    "and error handling across interfaces. For ASIL D, interface testing is particularly critical because failures can propagate through system. System "
                    "testing verifies the complete software system against software requirements. Testing must encompass functional behavior, error handling, and performance "
                    "characteristics. Regression testing verifies that changes do not introduce defects in previously validated functionality. For ASIL D, regression testing "
                    "is mandatory after any modification. Testing should occur in the target environment or a representative simulation. Requirements-based testing ensures "
                    "every requirement is tested. Fault injection testing deliberately introduces failures to verify error handling. Resource usage testing verifies correct "
                    "behavior under various memory and processing load conditions. Back-to-back testing compares behavior between model (design) and code implementations."
                ),
                "keywords": ["integration testing", "system testing", "interfaces", "regression testing", "requirements-based", "fault injection", "back-to-back", "ASIL"],
            },
            "asil_specific_methods": {
                "title": "ASIL-Specific Verification Methods and Techniques",
                "part": "Part 6: Software Development",
                "clause": "6.5-6.7, Tables 6.3, 6.4, 6.5",
                "content": (
                    "ISO 26262 defines tables of recommended and mandatory techniques for verification at each ASIL. ASIL A allows informal design review and basic unit testing. "
                    "ASIL B requires design review, unit testing with branch coverage, integration testing, and static analysis. ASIL C requires all ASIL B techniques plus "
                    "architectural design review, increased test coverage emphasis, and formal specification review. ASIL D mandates MC/DC coverage, formal verification methods, "
                    "model-based design practices, and higher-level design reviews. Static analysis techniques include data flow analysis, control flow analysis, and coding rule "
                    "checking. Formal methods include theorem proving, model checking, and abstract interpretation that provide mathematical proof of correctness. Semi-formal "
                    "methods such as structured review and design by contract provide intermediate verification strength. The selection of techniques should be justified based on "
                    "risk and system complexity. Multiple techniques applied to the same element increase confidence. Tool confidence level (TCL) determines if tools used for "
                    "verification require qualification."
                ),
                "keywords": ["verification methods", "design review", "static analysis", "formal methods", "MC/DC", "model checking", "tool confidence", "ASIL-specific"],
            },
            "fault_injection": {
                "title": "Fault Injection Testing for ASIL D",
                "part": "Part 6: Product Development at Software Level",
                "clause": "6.5-6.7, Method Table Recommendations",
                "content": (
                    "Fault injection testing deliberately introduces failures to verify that error detection and handling mechanisms function correctly. Software-implemented "
                    "fault injection (SWIFI) modifies variables or registers to simulate hardware faults or data corruption. Hardware-based fault injection uses specialized equipment "
                    "to induce physical faults. Systematic fault injection campaigns inject faults in different program locations and scenarios to evaluate system robustness. "
                    "Single fault injection tests response to individual failures. Multiple fault injection tests response to simultaneous failures. Fault injection testing is "
                    "particularly important for ASIL D systems and for safety mechanisms that rely on error detection and correction. Results demonstrate that critical faults are "
                    "detected and appropriate responses occur (e.g., safe state transition). Metrics such as fault detection percentage, false alarm rate, and failure mode coverage "
                    "quantify effectiveness. Fault injection must be sufficiently comprehensive to provide reasonable confidence in system robustness without exhaustively testing "
                    "all possible fault combinations."
                ),
                "keywords": ["fault injection", "SWIFI", "error detection", "failure modes", "ASIL D", "robustness", "metrics", "coverage"],
            },
            "configuration_management": {
                "title": "Configuration Management and Change Control",
                "part": "Part 8: Supporting Processes",
                "clause": "8.4",
                "content": (
                    "Configuration management controls all work products including requirements, design documents, source code, test cases, and test results. Each item must "
                    "have unique identification including version number, date, and responsible person. Baselines represent approved collections of configuration items representing "
                    "complete system state at specific points. Changes to baselines must follow formal change control procedures. Change requests are analyzed for impact on safety, "
                    "cost, and schedule. Change impact analysis assesses how modifications affect other system components and required verification activities. For ASIL C and D, "
                    "change impact analysis is mandatory and documented. Approved changes are implemented and re-verified. Regression testing verifies that changes do not break "
                    "existing functionality. Traceability links between configuration items must be maintained and updated as configurations change. Version control systems maintain "
                    "history of all changes including who made them and why. Audit procedures verify that configuration management procedures are followed."
                ),
                "keywords": ["configuration management", "version control", "baselines", "change control", "impact analysis", "traceability", "regression testing", "audit"],
            },
            "tool_qualification": {
                "title": "Software Tool Qualification and Confidence Levels",
                "part": "Part 8: Supporting Processes",
                "clause": "8.4",
                "content": (
                    "Software development tools such as compilers, code generators, static analyzers, and test execution environments must be qualified if they could introduce "
                    "failures that would not be detected by other means. Tool Confidence Level (TCL) reflects the confidence that a tool will not introduce failures. TCL1 is "
                    "the highest confidence (no qualification needed). TCL2 requires tool validation that outputs are correct. TCL3 requires qualifying the tool through verification "
                    "and testing. Most development tools require TCL2 or TCL3 qualification. Qualification evidence includes tool documentation, version information, description of "
                    "tool scope and limitations, and validation testing demonstrating correct operation. Tools generating safety-relevant artifacts (code generators, static analyzers) "
                    "typically require TCL3 qualification. Qualification effort scales with ASIL—higher ASIL requires more rigorous tool qualification. Third-party tools used in "
                    "development must come from qualified vendors or be independently qualified."
                ),
                "keywords": ["tool qualification", "TCL", "tool confidence", "code generators", "static analyzers", "validation", "vendor qualification", "ASIL"],
            },
        },
    },
    "aspice": {
        "title": "Automotive SPICE (ASPICE) v3.1 — Process Assessment Model",
        "content": (
            "Automotive SPICE is a process assessment and improvement model specifically designed for automotive software development. The model is based on ISO/IEC 33000 series "
            "process assessment standards and incorporates automotive industry best practices. ASPICE defines capability levels 0-5 for process maturity and provides detailed "
            "process descriptions for automotive software development, system engineering, and supporting processes. ASPICE assessments evaluate organizational processes against the "
            "model to identify strengths and improvement opportunities. ASPICE capability levels have gained widespread recognition in the automotive industry as a quality indicator. "
            "Many OEMs require suppliers to achieve specific ASPICE capability levels (often level 2 or 3) as contractual requirements. The model emphasizes traceability, verification "
            "rigor, and process discipline."
        ),
        "sections": {
            "capability_levels": {
                "title": "Capability Levels and Maturity Assessment",
                "part": "ASPICE v3.1, Process Attributes",
                "clause": "Assessment Framework",
                "content": (
                    "Capability Level 0 (Incomplete): Process not implemented or does not achieve defined purpose. Level 1 (Performed): Process is executed and achieves its purpose "
                    "but without formal procedures. Level 2 (Managed): Process is planned and executed according to documented procedures. Work products are managed and verified. "
                    "Level 3 (Established): Process is defined based on a standard and adapted to organizational needs. Defined processes are proactively managed. Level 4 (Predictable): "
                    "Process is quantitatively controlled using metrics. Quantitative targets for performance are established and monitored. Level 5 (Optimizing): Processes are "
                    "continuously improved based on quantitative feedback and innovation. Moving from level 2 to 3 typically requires establishing formal process definitions and training. "
                    "Moving to level 4 requires implementing quantitative measurement and control. Achieving higher capability levels demonstrates process maturity and reduces variability. "
                    "Organizations typically pursue ASPICE improvements to meet customer requirements, improve product quality, and enhance predictability. Assessment frequency "
                    "typically ranges from annually to every two years to track improvement progress."
                ),
                "keywords": ["capability level", "maturity", "process assessment", "ASPICE", "level 0-5", "improvement", "quantitative", "metrics"],
            },
            "swe1_swt": {
                "title": "SWE.1 — Software Unit Implementation and SWE.4 — Software Unit Verification",
                "part": "ASPICE Software Engineering Processes",
                "clause": "SWE.1, SWE.4",
                "content": (
                    "SWE.1 focuses on transforming detailed design into source code. At level 1, source code is written. At level 2, coding standards are defined and code is "
                    "produced according to standards. At level 3, formal design-to-code traceability is established. At level 4, code metrics guide improvement. SWE.4 covers software "
                    "unit verification confirming units meet design specifications. At level 1, basic testing occurs. At level 2, unit test cases are derived from detailed design, "
                    "tests are planned and executed, and results are documented. At level 3, unit verification strategy is defined, static analysis is performed (code review, "
                    "static analysis tools), dynamic testing validates behavior, coverage metrics are measured, and traceability is bidirectional. At level 4, code complexity and "
                    "defect metrics guide test strategy. ASPICE emphasizes that SWE.4 includes both static and dynamic verification—code review and static analysis complement "
                    "unit testing. Traceability ensures every design requirement has corresponding test evidence."
                ),
                "keywords": ["SWE.1", "SWE.4", "unit implementation", "unit verification", "code review", "static analysis", "traceability", "testing strategy"],
            },
            "swe2_3_integration": {
                "title": "SWE.2 — Software Construction and SWE.5 — Software Integration",
                "part": "ASPICE Software Engineering Processes",
                "clause": "SWE.2, SWE.5",
                "content": (
                    "SWE.2 addresses assembly of software units into software components. At level 1, units are combined. At level 2, integration strategy is planned, units are "
                    "combined according to plan, integration tests verify interactions. At level 3, integration procedures are formally defined, regression testing is systematically "
                    "performed, and traceability between tests and design is maintained. SWE.5 (Integration and Integration Testing) addresses combining software components into larger "
                    "assemblies. At level 2, integration testing is planned and executed with results documented. At level 3, integration strategy is detailed and documented, "
                    "regression testing is comprehensive, architectural design traceability is established, and integration anomalies are tracked. At level 4, integration metrics "
                    "guide testing strategy. Integration testing typically progresses in phases from integration of component-level groups toward system integration. Each integration "
                    "step introduces new potential failure modes that testing must address. ASPICE emphasizes the importance of regression testing to detect unintended side effects "
                    "of integration changes."
                ),
                "keywords": ["SWE.2", "SWE.5", "integration", "integration testing", "regression testing", "strategy", "traceability", "architecture"],
            },
            "swe6_qualification": {
                "title": "SWE.6 — Software Qualification Testing",
                "part": "ASPICE Software Engineering Processes",
                "clause": "SWE.6",
                "content": (
                    "SWE.6 addresses software qualification testing verifying the integrated software against software requirements. At level 1, testing is performed informally. "
                    "At level 2, test cases are derived from requirements, qualification testing is executed according to plan, and results are documented with traceability to "
                    "requirements. At level 3, qualification test strategy is documented considering both functional and non-functional requirements, test environment is representative "
                    "of actual use, coverage is comprehensive and documented, and bidirectional traceability exists (requirements to test cases to results). At level 4, test execution "
                    "data and defect metrics guide continuing test activities. ASPICE emphasizes full requirements coverage—every requirement must have at least one corresponding test "
                    "case and documented test result. Test environment should simulate actual target hardware and operating conditions. Non-functional requirements such as performance, "
                    "resource usage, and reliability must be tested. Anomalies discovered must be tracked, analyzed, and resolved."
                ),
                "keywords": ["SWE.6", "qualification testing", "requirements coverage", "test strategy", "traceability", "test environment", "non-functional", "anomalies"],
            },
            "sys_requirements": {
                "title": "SYS.1 — System Requirements Analysis and SYS.3 — System Architectural Design",
                "part": "ASPICE System Engineering Processes",
                "clause": "SYS.1, SYS.3",
                "content": (
                    "SYS.1 addresses system requirements analysis. At level 2, system requirements are collected and documented. At level 3, requirements are analyzed for completeness, "
                    "consistency, and feasibility; acceptance criteria are defined; traceability is established. At level 4, requirements volatility and quality metrics guide analysis. "
                    "System requirements form the basis for all subsequent design and verification activities. SYS.3 addresses system architectural design decomposing system requirements "
                    "into subsystems and defining interfaces. At level 2, system architecture is designed. At level 3, design is documented with rationale, design reviews are conducted, "
                    "traceability is established from system requirements to architectural elements, and design trade-offs are documented. At level 4, architectural metrics guide design "
                    "decisions. System architecture must address all functional and safety requirements. Interfaces between subsystems must be clearly defined. Allocation of requirements "
                    "to subsystems enables verification at appropriate levels."
                ),
                "keywords": ["SYS.1", "SYS.3", "system requirements", "architectural design", "allocation", "interfaces", "traceability", "design review"],
            },
            "process_discipline": {
                "title": "Process Management and Supporting Processes",
                "part": "ASPICE Management and Supporting Processes",
                "clause": "MAN.3, SUP.1, SUP.4, SUP.5, SUP.9",
                "content": (
                    "MAN.3 (Project Management) addresses planning and execution of projects. At level 2, project is planned with scope, schedule, and resources. Work is monitored and "
                    "controlled against plan. At level 3, process and metrics are defined, project procedures follow organizational standards. SUP.1 (Configuration Management) addresses "
                    "version control and configuration control. At level 2, baseline configuration is established and changes are tracked. At level 3, configuration control formally "
                    "manages changes with impact analysis. SUP.4 (Quality Assurance) addresses verification and validation. At level 2, QA activities are planned and performed, findings "
                    "are reported. At level 3, QA criteria are defined based on standards and risk. SUP.5 (Verification) addresses systematic verification. At level 2, verification "
                    "methods are applied. At level 3, verification strategy is documented and comprehensively applied. SUP.9 (Risk Management) addresses risk identification and mitigation. "
                    "Higher ASPICE levels require more disciplined process management, comprehensive documentation, and continuous improvement based on metrics."
                ),
                "keywords": ["process management", "configuration management", "quality assurance", "verification", "risk management", "discipline", "standards", "metrics"],
            },
        },
    },
    "autosar": {
        "title": "AUTOSAR — Automotive Open System Architecture",
        "content": (
            "AUTOSAR defines a standardized software architecture for automotive electrical/electronic systems. The architecture enables interoperability between components from "
            "different suppliers and supports model-based software development. AUTOSAR specifies a layered architecture with Application, Runtime Environment (RTE), Basic Software, "
            "and hardware abstraction layers. The architecture supports functional safety through deterministic execution, clear interfaces, and abstraction of hardware details. "
            "AUTOSAR enables reuse of software components across vehicle platforms and manufacturers. Model-based development using AUTOSAR tools supports automatic code generation "
            "from models, reducing manual coding and associated defect risks. Verification of AUTOSAR software must address both application logic and integration with the underlying "
            "platform."
        ),
        "sections": {
            "architecture": {
                "title": "AUTOSAR Layered Architecture and Integration",
                "part": "AUTOSAR Specification",
                "clause": "Architecture Overview",
                "content": (
                    "AUTOSAR architecture comprises four main layers: Application Layer (APP) contains functional software components independent of hardware. Runtime Environment "
                    "(RTE) provides abstract interfaces between application components and basic software, enabling portability. Basic Software (BSW) provides operating system, "
                    "communication stacks, and hardware drivers. Hardware Abstraction Layer (HAL) abstracts hardware specifics. Components communicate through standardized interfaces. "
                    "The RTE mediates all communication, decoupling application from hardware. This architecture supports testing at multiple levels: unit testing of individual components, "
                    "integration testing verifying component interactions through RTE, and system testing in the vehicle environment. Component reuse across platforms is simplified because "
                    "RTE abstracts hardware differences. Testing strategies must address RTE behavior including timing, message ordering, and error handling. Vendor-supplied components "
                    "must be tested for compatibility with the RTE implementation and other components in the system."
                ),
                "keywords": ["AUTOSAR", "architecture", "RTE", "basic software", "abstraction", "integration", "portability", "component reuse"],
            },
            "model_based_development": {
                "title": "Model-Based Software Development and Code Generation",
                "part": "AUTOSAR Specification",
                "clause": "Development Process",
                "content": (
                    "AUTOSAR supports model-based development where system behavior is defined in models (diagrams, state machines, data flow) and implementation code is automatically "
                    "generated. Code generation from models reduces manual coding, improves consistency, and enables traceability from model to code. Generated code is typically verified "
                    "through back-to-back testing comparing model execution with code execution. The code generator tool itself is a safety-critical component and requires TCL qualification. "
                    "Developers must verify that generated code correctly implements the model. Manual modifications to generated code should be minimized and tracked carefully as they may "
                    "complicate verification and maintenance. Model development requires quality discipline similar to manual coding—design review, version control, and testing of model behavior. "
                    "Simulation tools enable testing models before code generation, providing early defect detection. Integration of generated code with hand-written code requires careful "
                    "testing of boundaries and interactions."
                ),
                "keywords": ["model-based development", "code generation", "back-to-back testing", "simulation", "tool qualification", "traceability", "design review"],
            },
        },
    },
    "sotif": {
        "title": "ISO 21448 — Safety of the Intended Functionality (SOTIF)",
        "content": (
            "ISO 21448 (SOTIF) addresses safety risks arising from unintended functionality or safe system behavior that creates hazards. While ISO 26262 addresses failures of "
            "intended safety functions, SOTIF addresses failures that occur even when the system operates as designed. This distinction is critical for autonomous driving systems, "
            "machine learning-based features, and systems operating in variable real-world environments. SOTIF requires identifying performance limitations and edge cases, validating "
            "behavior in diverse scenarios, and ensuring safe fallback behavior when system limitations are exceeded. For AI/ML systems, SOTIF emphasizes the importance of validating "
            "performance across representative operational domains and identifying scenarios where machine learning models may fail. Continuous monitoring and feedback mechanisms are "
            "essential for post-market SOTIF assurance."
        ),
        "sections": {
            "sotif_framework": {
                "title": "SOTIF Concept and Unknown Unsafe Scenarios",
                "part": "ISO 21448:2022",
                "clause": "Framework Overview",
                "content": (
                    "SOTIF addresses situations where a system behaves as designed but creates a hazardous situation due to incomplete specification, misunderstanding of use, or "
                    "limitations in the system's capabilities. For example, an autonomous vehicle sensor might fail to detect obstacles in heavy rain—not because the sensor is broken "
                    "(that's ISO 26262), but because the sensor specification didn't account for that environmental condition (that's SOTIF). Unknown unsafe scenarios are situations "
                    "where intended functionality creates hazards in ways not anticipated during design. A machine learning model that makes decisions outside its training domain exemplifies "
                    "SOTIF concern. SOTIF assurance involves identifying possible operational domains, testing behavior across representative scenarios, discovering edge cases where "
                    "performance degrades, and ensuring safe degradation or fallback when limitations are exceeded. For systems using sensors, SOTIF includes validating sensor performance "
                    "across environmental variations (rain, snow, dust, temperature extremes). For autonomous systems, SOTIF includes validating decision quality in diverse traffic and "
                    "environmental conditions."
                ),
                "keywords": ["SOTIF", "unknown unsafe scenarios", "intended functionality", "operational domain", "edge cases", "safe degradation", "machine learning"],
            },
            "machine_learning_validation": {
                "title": "Machine Learning and AI System Validation",
                "part": "ISO 21448:2022",
                "clause": "Application to Advanced Systems",
                "content": (
                    "Machine learning models learn patterns from training data and apply learned patterns to new data. SOTIF challenges for ML include identifying the operational domain "
                    "where the model performs acceptably, discovering inputs where model performance degrades, and ensuring safe behavior when inputs are outside the training domain. "
                    "Validation methodologies include training-data analysis ensuring representative coverage of expected operational scenarios, performance evaluation on diverse test sets "
                    "measuring accuracy, precision, recall, and robustness metrics, adversarial testing probing for vulnerable inputs, and simulation testing driving the model through "
                    "scenarios with known ground truth. Out-of-distribution detection identifies when inputs fall outside the training domain, triggering safe fallback. Continuous learning "
                    "systems must be carefully managed to prevent models from degrading as new data is incorporated. For safety-critical ML applications, human-in-the-loop validation may be "
                    "appropriate, with human oversight for high-risk decisions. Version control of training data and model artifacts is essential. Interpretability of model decisions is "
                    "important for understanding failure modes and building confidence in safety."
                ),
                "keywords": ["machine learning", "AI", "validation", "training data", "adversarial testing", "out-of-distribution", "robustness", "interpretability"],
            },
            "operational_validation": {
                "title": "Operational Design Domain (ODD) and Testing",
                "part": "ISO 21448:2022",
                "clause": "Operational Design Domain Definition",
                "content": (
                    "The Operational Design Domain defines the conditions under which a system is intended to operate safely. ODD specification is critical for autonomous systems and "
                    "systems using sensors. ODD includes environmental conditions (weather, lighting, road types), operating scenarios (urban, highway, parking), and user interactions. "
                    "For example, an autonomous vehicle's ODD might specify operation on well-marked highways in daylight with dry conditions, excluding heavy rain or snow. Systems must "
                    "be validated to operate safely within the ODD and must have safe fallback when conditions exceed ODD boundaries. Testing should systematically cover the ODD space. "
                    "Edge cases at ODD boundaries are particularly important—behavior should degrade gracefully, not abruptly. For machine learning systems, training data should be "
                    "representative of the ODD. Post-market, actual operating conditions should be monitored to identify ODD violations and edge cases encountered in real use. If actual "
                    "conditions extend beyond specified ODD, ODD should be updated or the system should be modified to handle expanded conditions."
                ),
                "keywords": ["operational design domain", "ODD", "environmental conditions", "operating scenarios", "boundary conditions", "validation", "safe fallback"],
            },
            "continuous_monitoring": {
                "title": "Post-Market Monitoring and Continuous Assurance",
                "part": "ISO 21448:2022",
                "clause": "Post-Development Assessment",
                "content": (
                    "Post-market SOTIF assurance involves monitoring real-world system performance to identify unknown unsafe scenarios emerging from actual usage. Telemetry data collection "
                    "including sensor readings, decision metrics, and outcomes provides feedback on system performance. Anomaly detection identifies operating conditions or scenarios "
                    "differing from expected. Accident investigation analyzing incidents involving the system identifies previously unknown failure modes. Machine learning models can "
                    "degrade over time as operating conditions shift or as systems are used outside their training domain—continuous monitoring enables proactive detection. Feedback loops "
                    "enable periodic model retraining or system updates to address discovered issues. For safety-critical systems, a human-in-the-loop approach may be appropriate, where "
                    "humans review high-risk situations before autonomous actions. Transparency to users about system limitations is important—users must understand what tasks the system "
                    "can perform safely and should avoid relying on the system beyond its capabilities. Post-market surveillance data feeds back into development, improving next-generation "
                    "systems."
                ),
                "keywords": ["post-market", "monitoring", "telemetry", "anomaly detection", "feedback loops", "retraining", "user transparency", "continuous assurance"],
            },
        },
    },
    "un_r155_r156": {
        "title": "UN R155 and R156 — Cybersecurity and Software Update Management",
        "content": (
            "UN R155 (Cybersecurity and Cyber-Physical Security) and UN R156 (Software Updates) are United Nations regulations adopted by many countries including EU, Japan, and China, "
            "establishing mandatory cybersecurity and update management requirements for connected vehicles. Regulations apply to vehicles with dedicated short-range communications (DSRC), "
            "cellular connections, or other network connectivity. UN R155 requires establishment of a cybersecurity management system, threat and vulnerability assessment, secure design, "
            "and incident response. UN R156 requires secure update mechanisms, secure storage of update packages, and controlled update deployment. Compliance is mandatory for new vehicles "
            "in regulated markets. The regulations create a framework for continuous security management addressing evolving threats during vehicle operation, moving beyond development-phase "
            "security assurance toward operational security monitoring."
        ),
        "sections": {
            "cybersecurity_management": {
                "title": "Cybersecurity Management System (UN R155)",
                "part": "UN R155 Regulation",
                "clause": "Core Requirements",
                "content": (
                    "Manufacturers must establish a cybersecurity management system addressing organizational policies, processes, and technical controls. A cybersecurity manager must be "
                    "designated responsible for the program. Threat and vulnerability assessment identifies potential attacks and system weaknesses. Security requirements must be derived from "
                    "threat assessment and incorporated into design specifications. Secure design includes defense-in-depth principles, secure coding practices, and architectural controls. "
                    "Security testing validates that controls are effective and vulnerabilities are not present. Testing includes penetration testing, fuzzing, and adversarial testing probing "
                    "for attack vectors. A vulnerability disclosure program enables external researchers to report discovered vulnerabilities without public disclosure, enabling coordinated "
                    "disclosure and patching. Incident response procedures define investigation and remediation steps if security incidents occur. Documentation must demonstrate compliance "
                    "with UN R155 requirements. Regular updates to the cybersecurity program address emerging threats. For complex vehicles with many connected systems, establishing clear "
                    "architectural boundaries helps manage cybersecurity scope and enables focused defense strategies."
                ),
                "keywords": ["cybersecurity management", "threat assessment", "vulnerability assessment", "penetration testing", "incident response", "disclosure program", "UN R155"],
            },
            "software_updates": {
                "title": "Software Update Management (UN R156)",
                "part": "UN R156 Regulation",
                "clause": "Update Requirements",
                "content": (
                    "Software update mechanisms enable delivery of security patches, functional improvements, and bug fixes to vehicles after release. Updates must be cryptographically signed "
                    "to ensure authenticity and prevent installation of unauthorized or malicious updates. Update packages must be encrypted in transit to prevent interception and modification. "
                    "Secure storage protects updates before installation. Update deployment procedures must verify update integrity before installation and provide rollback capability if an "
                    "update introduces problems. Updates must be verified to maintain safety and functional correctness—security patches must not break existing safety functions or features. "
                    "Staged rollout enables monitoring for unexpected issues before widespread deployment. Users must be informed of available updates and update status. For critical security "
                    "vulnerabilities, manufacturers should push updates automatically or strongly encourage immediate installation. Testing should verify that the update mechanism works, "
                    "that updates install correctly, and that rollback functions properly. Update procedures should handle network interruptions and vehicle power-down scenarios that might "
                    "occur during installation."
                ),
                "keywords": ["software updates", "cryptographic signing", "encryption", "update deployment", "rollback", "security patches", "staged rollout", "UN R156"],
            },
            "threat_modeling": {
                "title": "Threat Modeling and Attack Scenarios",
                "part": "UN R155/R156",
                "clause": "Security Analysis",
                "content": (
                    "Systematic threat modeling identifies potential attacks and security risks. STRIDE methodology (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, "
                    "Elevation of Privilege) provides a framework for threat identification. Attack trees enumerate attack chains from attacker goals through intermediate objectives to concrete "
                    "attack actions. For vehicles, threat scenarios include: compromised communication channels enabling remote commands, compromised software components enabling arbitrary code "
                    "execution, compromised supply chain enabling backdoors, insider threats from employees with system access, and physical attacks accessing vehicle systems. Each threat scenario "
                    "should be analyzed for likelihood, impact, and available mitigations. Security requirements should address the most significant threats. Testing should validate that "
                    "mitigations are effective. As new attack techniques emerge or new vulnerabilities are discovered, threat models should be updated and remediation strategies should be "
                    "adjusted. Sharing threat information industry-wide (through organizations like AutoSAR and industry working groups) enables learning from others' discoveries."
                ),
                "keywords": ["threat modeling", "STRIDE", "attack trees", "risk analysis", "attack scenarios", "mitigations", "remote attacks", "insider threats"],
            },
        },
    },
}
