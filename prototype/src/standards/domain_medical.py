"""Domain-specific standards: Medical Devices / Healthcare IT."""

STANDARD_ID = "Medical Device Standards"

SECTIONS: dict[str, dict] = {
    "iec_62304:2015": {
        "title": "IEC 62304:2015 — Medical Device Software Lifecycle Processes",
        "sections": {
            "5.1": {
                "title": "Software Development Planning",
                "part": "Part 5: Software Development",
                "clause": "5.1",
                "content": (
                    "The manufacturer shall establish a comprehensive software development plan covering scope, "
                    "objectives, and organizational context. The plan must define the software development process, "
                    "standards, methods, and tools to be used. Traceability mechanisms between system requirements and "
                    "software items must be established and maintained throughout the lifecycle. The plan shall specify "
                    "verification and validation activities proportionate to the software safety class. Risk management "
                    "integration points and configuration management procedures must be documented. The plan serves as "
                    "the basis for all subsequent development activities and must be reviewed and approved by appropriate "
                    "personnel before development commences. Regular review and update of the plan is required when significant "
                    "changes to development scope or approach occur."
                ),
                "keywords": ["development plan", "traceability", "verification", "validation", "medical software", "lifecycle", "process definition", "risk management integration"],
            },
            "5.2": {
                "title": "Software Requirements Analysis",
                "part": "Part 5: Software Development",
                "clause": "5.2",
                "content": (
                    "Software requirements shall be derived from system requirements and defined in a Software Requirements "
                    "Specification (SRS). Each requirement must be clear, unambiguous, testable, and traceable to system requirements. "
                    "Requirements shall address functional behavior, performance characteristics, error handling, and resource constraints. "
                    "For Class B and C software, requirements must address safety-related functions and include acceptance criteria. "
                    "The SRS must be reviewed and approved before proceeding to design. Bidirectional traceability between system and "
                    "software requirements must be maintained. Any changes to requirements undergo formal change control with impact analysis. "
                    "Requirements can be derived through various methods including interviews, prototyping, and iterative refinement, but "
                    "documentation completeness increases with software safety class."
                ),
                "keywords": ["requirements analysis", "SRS", "functional requirements", "safety requirements", "traceability", "acceptance criteria", "Class B", "Class C"],
            },
            "5.3": {
                "title": "Software Architectural Design",
                "part": "Part 5: Software Development",
                "clause": "5.3",
                "content": (
                    "The software architecture defines high-level structure, decomposition into software items, and interfaces between items. "
                    "Architectural design shall address modularity, reusability, and design patterns suitable for medical device context. "
                    "Software items are the smallest units of software that can be uniquely identified and tested. Each item shall have "
                    "defined responsibilities, interfaces, and dependencies. For Class C software, architectural design must consider fault "
                    "tolerance, error handling, and recovery mechanisms. Design rationale documentation supports traceability from requirements "
                    "to architectural decisions. Reuse of components requires qualification and documentation of any modifications. The architecture "
                    "must support the verification strategy and enable effective integration and system-level testing."
                ),
                "keywords": ["architectural design", "software items", "modularity", "interfaces", "decomposition", "fault tolerance", "design patterns", "reusability"],
            },
            "5.4": {
                "title": "Software Detailed Design and Unit Implementation",
                "part": "Part 5: Software Development",
                "clause": "5.4",
                "content": (
                    "Detailed design describes each software unit's internal structure, algorithms, data structures, and internal interfaces. "
                    "The design shall be sufficiently detailed that independent implementation is possible. Coding standards and conventions "
                    "applicable to the organization and target platform must be established and followed. Unit implementation translates detailed "
                    "design into source code using the specified programming language and development environment. For Class B and C software, "
                    "code reviews (static analysis) are required to verify conformance to design and coding standards. Documentation of design "
                    "decisions, assumptions, and constraints enhances maintainability. The detailed design must be reviewed for correctness, "
                    "completeness, and consistency with higher-level design before implementation."
                ),
                "keywords": ["detailed design", "unit implementation", "coding standards", "algorithms", "code review", "static analysis", "data structures", "source code"],
            },
            "5.5": {
                "title": "Software Integration and Integration Testing",
                "part": "Part 5: Software Development",
                "clause": "5.5",
                "content": (
                    "Software integration combines software units into larger functional subsystems according to an integration strategy. "
                    "Integration testing verifies that integrated units work correctly together and that interfaces function as specified. "
                    "Test cases shall be derived from the architectural design and cover interface behaviors, data flow, and error conditions. "
                    "For Class B software, integration test results must be evaluated against acceptance criteria and documented. For Class C, "
                    "complete traceability from test cases to architectural design elements is mandatory, along with regression testing for any "
                    "changes. Integration testing typically progresses from unit-pair integration toward system integration. Documentation of "
                    "integration sequence, test environment setup, test data, and test results is required. Any anomalies discovered must be "
                    "analyzed and resolved before proceeding to system testing."
                ),
                "keywords": ["integration testing", "software items", "Class B", "Class C", "architecture", "interfaces", "integration strategy", "regression testing"],
            },
            "5.6": {
                "title": "Software Verification",
                "part": "Part 5: Software Development",
                "clause": "5.6",
                "content": (
                    "Software verification confirms that software meets its defined requirements and specifications. Verification activities include "
                    "both static and dynamic approaches. Static verification encompasses code review, static analysis tools, and design inspection "
                    "to identify defects before execution. Dynamic verification involves testing to demonstrate correct behavior during execution. "
                    "The extent of verification activities scales with software safety class. Class A may use informal review, while Class B requires "
                    "documented verification and Class C mandates comprehensive verification with traceability matrices. Verification planning must "
                    "define criteria for success, test strategies, and acceptance levels. Records of verification activities, including test cases, "
                    "test results, and any issues identified, must be maintained. Verification results feed into hazard analysis and contribute to "
                    "overall system safety assessment."
                ),
                "keywords": ["verification", "static analysis", "code review", "dynamic testing", "traceability", "hazard analysis", "Class A", "Class B", "Class C"],
            },
            "5.7": {
                "title": "Software System Testing",
                "part": "Part 5: Software Development",
                "clause": "5.7",
                "content": (
                    "System testing verifies that the fully integrated software system meets all software requirements in its operational environment. "
                    "Tests must demonstrate that all defined requirements are implemented and functioning correctly. Test cases shall be derived from "
                    "software requirements and shall cover normal operation, error conditions, boundary conditions, and recovery scenarios. For Class C, "
                    "complete requirements traceability is mandatory—every requirement must have at least one corresponding test case, and test results "
                    "must demonstrate requirement satisfaction. System testing should be conducted in an environment that closely simulates the intended "
                    "use environment. Anomalies and deviations discovered during testing must be thoroughly investigated, documented, and resolved. Testing "
                    "results form the basis for claims of software correctness and contribute to overall device validation activities."
                ),
                "keywords": ["system testing", "requirements", "traceability", "anomalies", "operational environment", "test coverage", "requirement satisfaction"],
            },
            "5.8": {
                "title": "Software Release",
                "part": "Part 5: Software Development",
                "clause": "5.8",
                "content": (
                    "Software release is the formal delivery of software for operational use. Before release, all verification activities must be completed, "
                    "test results reviewed, and identified issues resolved or formally accepted. Release documentation must include the software configuration, "
                    "version identification, and summary of changes from previous releases. For Class B and C, a software release record shall be maintained "
                    "documenting release approval, configuration, and completion of verification activities. The software must be under configuration management "
                    "with unique identification and change control. Release criteria must be defined in the development plan and include completion of all "
                    "planned verification activities, resolution of critical issues, and regulatory compliance verification. Installation and deployment "
                    "procedures should be documented to ensure correct implementation in the target environment."
                ),
                "keywords": ["software release", "configuration management", "release record", "version control", "deployment", "change management", "release criteria"],
            },
            "5.9": {
                "title": "Software Maintenance",
                "part": "Part 5: Software Development",
                "clause": "5.9",
                "content": (
                    "Software maintenance encompasses all activities performed after release to sustain and improve the software. Maintenance includes "
                    "corrective maintenance (bug fixes), adaptive maintenance (changes due to environment changes), and perfective maintenance (enhancements). "
                    "For medical device software, maintenance must follow the same rigorous controls as initial development. A maintenance plan shall define "
                    "procedures for problem reporting, prioritization, and resolution. Changes must undergo impact analysis and appropriate verification. "
                    "For Class B and C, regression testing verifies that changes do not introduce new defects or affect unrelated functionality. Configuration "
                    "management must track all modifications. Version control must be maintained with clear documentation of what changed and why. Post-market "
                    "surveillance data and adverse event reports feed into maintenance decision-making. Maintenance activities must be documented and retained "
                    "as part of the device history record."
                ),
                "keywords": ["maintenance", "corrective", "adaptive", "perfective", "impact analysis", "regression testing", "configuration control", "post-market"],
            },
            "risk_classes": {
                "title": "Software Safety Classification",
                "part": "Part 5: Software Development",
                "clause": "5.0 (Overview)",
                "content": (
                    "Software safety class assignment determines the rigor of development and verification activities. Class A applies when software failure "
                    "poses no injury risk and only minimal business impact. Class A requires basic documentation and standard development practices with no "
                    "specific verification activities mandated. Class B applies when software failure could cause non-serious injury or significant business "
                    "impact. Class B requires documented development process, traceability matrix, code review, and integration testing. Class C applies when "
                    "software failure could result in death or serious injury. Class C mandates comprehensive lifecycle activities including complete requirements "
                    "traceability matrix, detailed design documentation, unit testing with code coverage analysis, integration testing, system testing with full "
                    "requirements coverage, regression testing after any changes, and formal problem resolution procedures. Additionally, Class C software requires "
                    "consideration of design failures, fault tolerance mechanisms, and validation activities that confirm the software supports safe operation across "
                    "all intended use scenarios. The software safety class must be assigned based on risk analysis early in the development lifecycle and documented "
                    "in the development plan."
                ),
                "keywords": ["Class A", "Class B", "Class C", "safety", "risk classification", "lifecycle requirements", "verification rigor", "traceability"],
            },
            "traceability": {
                "title": "Requirements Traceability",
                "part": "Part 5: Software Development",
                "clause": "5.2, 5.5, 5.7 (integrated concept)",
                "content": (
                    "Traceability establishes and maintains relationships between requirements at different levels and between requirements and implementation. "
                    "Upward traceability links software requirements to system requirements, confirming that all system needs are addressed. Downward traceability "
                    "links software requirements to design elements, source code, and test cases, confirming complete implementation. Bidirectional traceability "
                    "provides confidence that requirements are fully implemented and tested. For Class C software, comprehensive traceability matrices are mandatory, "
                    "documenting the mapping between requirements and verification activities. Traceability must be maintained throughout the lifecycle and updated "
                    "whenever requirements or design elements change. Tools supporting traceability (requirements management systems) are often essential for Class B "
                    "and C products. Gaps in traceability indicate missing requirements, untested functionality, or orphaned code that must be investigated. Regular "
                    "traceability audits ensure completeness and accuracy."
                ),
                "keywords": ["traceability", "upward", "downward", "bidirectional", "traceability matrix", "requirements management", "gaps", "implementation"],
            },
        },
    },
    "fda_csa:2025": {
        "title": "FDA Computer Software Assurance (CSA) Guidance — 2025",
        "content": (
            "The FDA's Computer Software Assurance guidance represents a shift from prescriptive Computer System Validation (CSV) toward a "
            "more flexible, risk-based approach to software quality assurance. CSA emphasizes demonstrating assurance proportionate to the "
            "risk posed by the software. This guidance applies to software used in manufacturing, quality systems, and as components of medical devices. "
            "The approach prioritizes critical thinking and evidence-based decision-making over rigid adherence to extensive documentation. "
            "Assurance activities can range from minimal for low-risk functions to comprehensive for high-risk functions. Modern development practices, "
            "including agile methodologies, are accommodated within the CSA framework provided that appropriate verification and documentation are performed."
        ),
        "sections": {
            "risk_based": {
                "title": "Risk-Based Assurance Framework",
                "part": "CSA Main Content",
                "clause": "Core Principle",
                "content": (
                    "Assurance activities should be commensurate with the risk posed by the software function. High-risk functions affecting patient safety, "
                    "system integrity, or data accuracy require extensive assurance including scripted testing with documented evidence, formal verification, "
                    "comprehensive traceability, and independent review. Medium-risk functions benefit from a combination of scripted and unscripted testing, "
                    "with moderate documentation and review. Low-risk functions can employ unscripted or exploratory testing, informal peer review, and lighter "
                    "documentation provided that risks remain acceptably low. Risk assessment should consider potential patient harm, criticality to device function, "
                    "regulatory impact, and data sensitivity. The software development history (legacy vs. newly developed), architectural quality, and use of "
                    "verified components also inform the appropriate assurance level. Risk-based strategies enable organizations to allocate resources efficiently "
                    "to areas of highest concern while maintaining product quality and regulatory compliance."
                ),
                "keywords": ["CSA", "risk-based", "assurance", "scripted", "unscripted", "FDA", "risk assessment", "proportionate assurance"],
            },
            "critical_thinking": {
                "title": "Critical Thinking Framework",
                "part": "CSA Main Content",
                "clause": "Assurance Approach",
                "content": (
                    "CSA guidance emphasizes critical thinking as an alternative to checkbox-oriented compliance. Critical thinking involves understanding the "
                    "business purpose of software, identifying potential failure modes and their consequences, and designing assurance activities that address "
                    "those specific risks. Rather than applying a standard template of activities to all software, organizations should justify their assurance "
                    "approach based on risk analysis. Documentation should support the assurance decisions made, explaining what was tested, how risks informed "
                    "the testing strategy, and what evidence supports the conclusion that software is fit for its intended use. This approach respects that not "
                    "all software activities contribute equally to quality and that blanket requirements for verification methods may not always be the most "
                    "efficient path to assurance. Critical thinking fosters continuous improvement and adaptation as new risks emerge or as organizational capabilities "
                    "and development practices evolve."
                ),
                "keywords": ["critical thinking", "risk analysis", "failure modes", "assurance decisions", "documentation", "fit for use", "judgment"],
            },
            "testing_strategies": {
                "title": "Scripted versus Unscripted Testing",
                "part": "CSA Main Content",
                "clause": "Testing Approaches",
                "content": (
                    "Scripted testing involves predetermined test cases with defined inputs, procedures, and expected outputs documented before execution. "
                    "Scripted testing provides reproducibility, traceability, and clear evidence of what was tested and the results obtained. Scripted testing "
                    "is particularly valuable for high-risk functions, regulatory-critical features, and regression testing to ensure changes do not introduce "
                    "defects. Unscripted testing encompasses exploratory testing, ad-hoc testing, and other flexible approaches where the tester uses judgment "
                    "and knowledge to probe for defects and unexpected behaviors. Unscripted testing is efficient for discovering new defects and exploring edge "
                    "cases. CSA allows unscripted testing for lower-risk software but requires documentation of findings and methodology. The combination of "
                    "scripted and unscripted approaches often optimizes assurance efficiency. Organizations should clearly document which functions receive which "
                    "testing approaches and justify the adequacy of that allocation based on risk."
                ),
                "keywords": ["scripted testing", "unscripted testing", "exploratory testing", "regression testing", "reproducibility", "traceability", "evidence"],
            },
            "documentation": {
                "title": "Documentation and Evidence Requirements",
                "part": "CSA Main Content",
                "clause": "Evidence Sufficiency",
                "content": (
                    "Documentation should support the assurance approach and provide evidence that appropriate activities were performed and risks addressed. "
                    "Rather than extensive documentation of routine activities, CSA focuses on documenting decisions, rationale, and findings. Key documentation "
                    "includes risk assessment results, assurance strategy justification, test cases and results for high-risk functions, verification summaries "
                    "demonstrating requirements coverage, configuration management records, change impact analyses, and formal approvals. Documentation should be "
                    "proportionate to risk—low-risk functions may have summary documentation, while high-risk functions require detailed records. Traceability "
                    "links should connect requirements to design, implementation, and verification activities. Evidence should be sufficient to demonstrate to "
                    "regulators and inspectors that appropriate assurance activities were performed and that risks are acceptably managed. Documentation retention "
                    "should follow regulatory requirements and support device history records."
                ),
                "keywords": ["documentation", "evidence", "rationale", "traceability", "verification summary", "change impact", "regulatory", "history record"],
            },
            "pre_post_market": {
                "title": "Pre-Market and Post-Market Obligations",
                "part": "CSA Main Content",
                "clause": "Lifecycle Considerations",
                "content": (
                    "Pre-market activities establish the foundation for software quality and safety. Pre-market verification must demonstrate that software "
                    "meets design specifications through testing, analysis, or inspection appropriate to the risk level. Pre-market validation confirms that "
                    "software supports safe and effective operation in the intended use environment. Regulatory submissions typically require evidence of pre-market "
                    "verification and validation activities commensurate with the device risk classification and software risk assessment. Post-market obligations "
                    "include monitoring software performance, investigating adverse events potentially related to software, and implementing corrective actions when "
                    "defects are discovered. Post-market surveillance may reveal new risks or failure modes not identified during development, necessitating software "
                    "updates or recalls. Maintenance and update procedures must maintain the same assurance level as initial development. For software-as-a-service "
                    "models and cloud-based systems, post-market monitoring and update procedures require particular attention due to continuous deployment scenarios. "
                    "Clear procedures for managing post-market software changes and their verification are essential."
                ),
                "keywords": ["pre-market", "post-market", "verification", "validation", "adverse events", "corrective action", "surveillance", "updates"],
            },
            "agile_considerations": {
                "title": "Modern Development Practices and Agile",
                "part": "CSA Main Content",
                "clause": "Methodology Flexibility",
                "content": (
                    "CSA guidance accommodates modern development practices including agile methodologies, continuous integration, and DevOps approaches. "
                    "Agile development can maintain the assurance level needed for medical device software through appropriate ceremonies, documentation, and "
                    "verification activities integrated into the agile workflow. Sprint planning should incorporate verification activities proportionate to risk. "
                    "Definition of done criteria should include verification confirmation. Continuous integration with automated testing supports rapid verification "
                    "feedback. However, the software released from agile development must meet the same assurance standards as traditionally developed software. "
                    "Configuration management and traceability remain essential, even in agile environments. Post-sprint verification documentation should clearly "
                    "demonstrate that requirements were addressed and tested. Regulatory submissions from agile development must present evidence equivalent to "
                    "traditional development approaches. Organizations adopting agile practices must maintain software history, change records, and verification "
                    "artifacts suitable for regulatory review."
                ),
                "keywords": ["agile", "continuous integration", "DevOps", "sprint", "automation", "traceability", "definition of done", "regulatory"],
            },
        },
    },
    "hipaa": {
        "title": "HIPAA — Health Insurance Portability and Accountability Act",
        "content": (
            "The Health Insurance Portability and Accountability Act (HIPAA) establishes national standards for protecting patient health information "
            "in the United States. The Privacy Rule defines permitted uses and disclosures of Protected Health Information (PHI). The Security Rule "
            "specifies safeguards for electronic Protected Health Information (ePHI). The Breach Notification Rule requires notification when PHI is "
            "accessed or disclosed improperly. For software used in healthcare settings, HIPAA compliance is mandatory. Organizations using or maintaining "
            "PHI are either covered entities (healthcare providers, health plans, clearinghouses) or business associates performing services on their behalf. "
            "HIPAA compliance is ongoing—not a one-time implementation—requiring continuous monitoring, updates, and verification of safeguards."
        ),
        "sections": {
            "security_rule": {
                "title": "HIPAA Security Rule — Technical Safeguards",
                "part": "45 CFR Parts 160 and 164",
                "clause": "Security Rule Subpart C",
                "content": (
                    "Access control safeguards regulate who can access ePHI and prevent unauthorized access. Required controls include unique user identification "
                    "ensuring each user can be identified, emergency access procedures for legitimate access to ePHI during emergencies, automatic logoff terminating "
                    "sessions after periods of inactivity, and encryption protecting ePHI in storage and transmission. Audit controls create mechanisms to record and "
                    "examine access to ePHI through system logs, identifying who accessed what information when. Integrity controls protect ePHI from improper alteration "
                    "or destruction through mechanisms such as checksums, digital signatures, or audit trails. Transmission security safeguards include encryption of "
                    "data in transit and use of secure communication protocols such as HTTPS, TLS, or VPNs. Testing must verify that all technical safeguards are "
                    "correctly implemented and functioning. Access control testing should verify that authorized users can access needed information and unauthorized "
                    "users are denied. Audit control testing should confirm that access events are logged and can be reviewed. Integrity testing should validate that "
                    "unauthorized alterations are detected. Encryption testing should confirm that data is properly encrypted and decryption works correctly."
                ),
                "keywords": ["HIPAA", "ePHI", "access control", "audit", "encryption", "integrity", "transmission", "healthcare", "safeguards"],
            },
            "privacy_rule": {
                "title": "HIPAA Privacy Rule — Data Protection",
                "part": "45 CFR Parts 160 and 164",
                "clause": "Privacy Rule Subpart A",
                "content": (
                    "The Privacy Rule establishes the standards and procedures for protecting PHI. Protected Health Information includes any information that can "
                    "identify an individual and relates to past, present, or future health status. The Privacy Rule allows use and disclosure of PHI only for "
                    "permitted purposes including direct treatment, healthcare operations, and payment processing. Uses for other purposes require explicit patient "
                    "authorization. Patients have rights to access their records, request amendments, and receive notice of privacy practices. Software supporting "
                    "PHI must enforce privacy controls through role-based access restricting users to information necessary for their job function. Disclosure "
                    "logging tracks when and to whom PHI is provided. Data minimization principles require limiting collection and retention of PHI to what is "
                    "necessary for the intended purpose. De-identification techniques can remove identifiers enabling broader use of health data while protecting "
                    "privacy. Software testing should verify that privacy controls prevent unauthorized disclosure, that logging captures all relevant access events, "
                    "and that de-identification processes correctly remove or obscure identifiers."
                ),
                "keywords": ["privacy", "PHI", "protected health information", "authorization", "access rights", "disclosure", "de-identification", "role-based access"],
            },
            "breach_notification": {
                "title": "HIPAA Breach Notification Rule",
                "part": "45 CFR Part 164",
                "clause": "Breach Notification Subpart D",
                "content": (
                    "A breach is an unauthorized acquisition, access, use, or disclosure of PHI that compromises security or privacy. The Breach Notification Rule "
                    "requires prompt notification to affected individuals, the Secretary of Health and Human Services, and media (for breaches affecting more than "
                    "500 residents of a state). Notification must occur without unreasonable delay, typically within 60 days. The notification must include the date "
                    "and nature of the breach, description of steps individuals should take, details of breach investigation, mitigation measures taken, and contact "
                    "information for the breached entity. Significant penalties (up to $1.5 million per violation type per year) apply for failure to notify or for "
                    "security violations. Software must implement breach detection mechanisms such as intrusion detection systems, anomalous access monitoring, and "
                    "integrity checking. Incident response procedures must be documented and tested. Forensic capabilities should enable investigation of breaches. "
                    "Testing should verify that breach detection mechanisms work, that notification procedures can be executed, and that evidence of breach investigation "
                    "can be collected and preserved."
                ),
                "keywords": ["breach", "breach notification", "unauthorized access", "disclosure", "incident response", "forensics", "penalties", "investigation"],
            },
            "business_associates": {
                "title": "Business Associate Agreements and Compliance",
                "part": "45 CFR Parts 160 and 164",
                "clause": "BA Requirements throughout Privacy and Security Rules",
                "content": (
                    "Business associates are vendors, contractors, and partners that process, store, or transmit PHI on behalf of covered entities. Business "
                    "Associate Agreements (BAAs) establish contractual obligations for PHI protection. All entities handling PHI must execute appropriate BAAs specifying "
                    "permitted uses, required safeguards, breach notification procedures, and audit rights. Business associates must implement administrative, physical, "
                    "and technical safeguards equivalent to those required of covered entities. Subcontracting to additional business associates requires extending the "
                    "BAA chain—each entity must contract with downstream vendors and ensure compliance. Failure to maintain appropriate BAAs is a violation. Software "
                    "vendors must document their HIPAA compliance controls and typically undergo security assessments by customers. Testing should verify that software "
                    "safeguards are implemented, that audit trails demonstrate compliance, and that incident response procedures are effective. Organizations must obtain "
                    "reasonable assurance from vendors that appropriate safeguards are in place through SOC 2 reports, security questionnaires, penetration testing, and "
                    "contractual commitments."
                ),
                "keywords": ["business associate", "BAA", "business associate agreement", "subcontractors", "safeguards", "audit", "vendor assessment", "SOC 2"],
            },
            "organizational_security": {
                "title": "Organizational Security Program and Risk Management",
                "part": "45 CFR 164.308",
                "clause": "Administrative Safeguards",
                "content": (
                    "Organizations must establish a comprehensive security program with written policies and procedures. A Security Official must be designated responsible "
                    "for developing and implementing security policies. Workforce security procedures control who has access to ePHI through role-based access controls and "
                    "segregation of duties. Information access management ensures users can access only information necessary for job functions. Security awareness training "
                    "must educate all workforce members about HIPAA requirements and security risks. Security incident procedures must define investigation and response steps. "
                    "Contingency planning establishes procedures for maintaining system availability during outages or disasters. Business continuity and disaster recovery "
                    "plans should include regular testing. Risk analysis identifies vulnerabilities and threats, assesses likelihood and impact, and recommends remediation. "
                    "Risk management processes continuously monitor for new risks and address emerging threats. Testing should validate that workforce security controls "
                    "function correctly, that training is effective, that incident response procedures work, and that contingency plans can be executed."
                ),
                "keywords": ["security program", "risk management", "security official", "workforce security", "training", "incident response", "contingency", "disaster recovery"],
            },
        },
    },
    "iec_62443": {
        "title": "IEC 62443 — Industrial Automation and Control Systems Security",
        "content": (
            "IEC 62443 provides requirements for the security of industrial automation and control systems (IACS) including those used in medical "
            "device manufacturing, laboratory automation, and healthcare IoT. The standard addresses cybersecurity from system engineering perspectives, "
            "component manufacturing, integration, and operation. For medical device manufacturers, IEC 62443 applies to software and systems used in "
            "manufacturing environments and to networked medical devices. The standard is structured in parts addressing different stakeholder perspectives: "
            "general concepts and terminology, security management systems, system security requirements, and component security requirements. IEC 62443 "
            "emphasizes defense-in-depth strategies, secure-by-design principles, and continuous security improvements throughout the lifecycle."
        ),
        "sections": {
            "security_levels": {
                "title": "Security Levels and Risk Assessment",
                "part": "IEC 62443-1 & 62443-3",
                "clause": "Security Level Determination",
                "content": (
                    "IEC 62443 defines four Security Levels (SL) corresponding to system criticality and threat likelihood. SL1 applies to systems where security "
                    "is a consideration but detailed requirements are not necessary. SL2 applies to systems in controlled environments with specific industrial protocols. "
                    "SL3 applies to systems exposed to external networks or where consequences of compromise are significant. SL4 applies to critical infrastructure where "
                    "sophisticated attackers might target the system. Security Level assignment must be based on risk assessment considering threat sources, vulnerability "
                    "likelihood, and potential impact. For medical device manufacturing systems, SL3 or higher is typically appropriate. Each Security Level prescribes "
                    "specific technical and management requirements that must be implemented. Testing and verification must confirm that security controls appropriate "
                    "to the assigned Security Level are functioning correctly. Risk assessment methodologies such as threat modeling and STRIDE support Security Level "
                    "determination."
                ),
                "keywords": ["security levels", "risk assessment", "SL1", "SL2", "SL3", "SL4", "threat modeling", "criticality", "cybersecurity"],
            },
            "system_architecture": {
                "title": "System Architecture and Defense-in-Depth",
                "part": "IEC 62443-3",
                "clause": "System Design Requirements",
                "content": (
                    "Secure architecture includes multiple defensive layers and security zones. Demilitarized zones (DMZs) separate trusted internal networks from "
                    "untrusted external networks. Network segmentation limits lateral movement if one component is compromised. Access control mechanisms at each zone "
                    "boundary enforce least-privilege principles. Single points of failure should be eliminated or protected through redundancy. Authentication mechanisms "
                    "must verify the identity of users and systems. Authorization controls ensure authenticated entities access only resources necessary for their role. "
                    "Cryptography protects confidentiality and integrity of data. Logging and monitoring detect suspicious activities. Incident response capabilities "
                    "enable rapid identification and containment of security breaches. For medical device systems, secure architecture should consider compatibility "
                    "with existing clinical workflows while maintaining appropriate controls. Testing should verify zone boundaries are enforced, access controls are effective, "
                    "and monitoring detects security anomalies."
                ),
                "keywords": ["system architecture", "defense-in-depth", "network segmentation", "authentication", "authorization", "cryptography", "monitoring", "zones"],
            },
            "software_security": {
                "title": "Software Security Development and Hardening",
                "part": "IEC 62443-4-1",
                "clause": "Product Development Requirements",
                "content": (
                    "Software must be developed using secure development lifecycle principles incorporating security from design through deployment. Secure coding "
                    "practices prevent common vulnerability classes such as buffer overflows, injection attacks, cross-site scripting, and broken authentication. Code "
                    "review identifies security flaws before deployment. Security testing includes dynamic analysis, penetration testing, and fuzzing to discover "
                    "vulnerabilities. Third-party components must be assessed for known vulnerabilities using software composition analysis tools. Update mechanisms "
                    "must enable rapid patching of discovered vulnerabilities. For medical device software, security hardening must balance security with safety—patches "
                    "must be validated to ensure they do not introduce new safety risks. Version control tracks all modifications. Cryptographic implementations must be "
                    "validated against standards. Testing should demonstrate that input validation prevents injection attacks, that cryptography is correctly implemented, "
                    "and that common vulnerabilities are not present."
                ),
                "keywords": ["secure development", "secure coding", "code review", "security testing", "penetration testing", "vulnerabilities", "patching", "cryptography"],
            },
            "authentication_authorization": {
                "title": "Authentication and Access Control",
                "part": "IEC 62443-3",
                "clause": "Technical Security Requirements",
                "content": (
                    "Multi-factor authentication provides stronger user verification than passwords alone. Knowledge factors (passwords), possession factors (tokens), "
                    "and inherence factors (biometrics) can be combined to increase confidence in user identity. Access control models such as role-based access control "
                    "(RBAC) or attribute-based access control (ABAC) enable fine-grained permission management. Principle of least privilege ensures users and systems "
                    "access only resources necessary for their function. Segregation of duties prevents single users from making unauthorized changes. Privilege elevation "
                    "procedures require approval and logging of temporary access increases. Session management controls idle timeout, concurrent session limits, and secure "
                    "session termination. For medical device systems used in hospitals, integration with enterprise authentication systems (LDAP, Active Directory) may be "
                    "appropriate. Testing should verify that authentication mechanisms work correctly, that access is properly restricted, and that privilege escalation "
                    "is prevented."
                ),
                "keywords": ["authentication", "multi-factor", "access control", "RBAC", "ABAC", "least privilege", "session management", "credentials"],
            },
        },
    },
    "eu_mdr": {
        "title": "EU Medical Device Regulation (EU MDR) — Software Requirements",
        "content": (
            "The European Union Medical Device Regulation (EU MDR, Regulation (EU) 2017/745) establishes requirements for medical devices marketed in the EU. "
            "Software-as-a-Medical-Device (SaMD) and software components of medical devices must comply with EU MDR requirements in addition to applicable standards. "
            "The MDR emphasizes risk management, technical documentation, clinical evidence, and post-market surveillance. For software, the regulation addresses lifecycle "
            "documentation, verification and validation, cybersecurity, and update procedures. EU MDR compliance is mandatory for devices marketed in EU member states and "
            "creates a harmonized regulatory framework across Europe. Compliance requires systematic quality management, documentation retention, and periodic reassessment "
            "of software safety and performance."
        ),
        "sections": {
            "documentation": {
                "title": "Technical Documentation and Design Documentation",
                "part": "EU MDR, Annex II",
                "clause": "Design and Manufacturing Information",
                "content": (
                    "Technical documentation must demonstrate that the device is designed and manufactured in compliance with EU MDR requirements. Software documentation "
                    "must include design specifications, functional requirements, architecture diagrams, and test documentation. The software design must be described "
                    "in sufficient detail to enable assessment of compliance. Design rationale must explain key decisions and how safety requirements are addressed. "
                    "Version control records must track all versions released and dates. Change history must document modifications and their justification. Traceability "
                    "from requirements through design to testing must be demonstrated. Documentation must be retained for the entire device lifetime plus additional periods "
                    "specified by national regulations (typically 5-10 years). For devices with regular updates, design documentation must be current with the latest "
                    "released version. Documentation must be available to notified bodies and competent authorities for compliance assessment. Testing and assessment "
                    "should verify that technical documentation is complete, current, and accurately reflects the actual software implementation."
                ),
                "keywords": ["technical documentation", "design documentation", "requirements", "architecture", "version control", "traceability", "change history"],
            },
            "risk_management": {
                "title": "Risk Management and Safety Analysis",
                "part": "EU MDR, Article 4 & Annex I",
                "clause": "General Safety and Performance Requirements",
                "content": (
                    "Risk management must be based on ISO 14971 or equivalent methodologies. Hazard analysis identifies potential dangers and adverse events. Risk "
                    "assessment quantifies likelihood and severity of harm. Risk control measures reduce risk through design changes, protective mechanisms, information "
                    "provision, or risk acceptance if residual risk is acceptably low. Risk evaluation ensures residual risks are acceptable. For software, risks include "
                    "failure modes caused by design defects, implementation errors, security vulnerabilities, and obsolescence. Systematic testing addresses identified risks. "
                    "Post-market surveillance feeds new risks into ongoing assessment. Software safety requirements must address security, availability, and data integrity. "
                    "Cybersecurity risk assessment should consider potential attack vectors and impact. Testing should validate that risk control measures are effective, "
                    "that identified failure modes do not occur, and that residual risks are acceptable."
                ),
                "keywords": ["risk management", "ISO 14971", "hazard analysis", "risk assessment", "risk control", "safety requirements", "cybersecurity", "residual risk"],
            },
            "verification_validation": {
                "title": "Verification and Validation Activities",
                "part": "EU MDR, Annex I",
                "clause": "Clinical Evaluation and Performance Evaluation",
                "content": (
                    "Verification confirms that design outputs correctly implement design input requirements. Validation confirms that the software supports safe and "
                    "effective operation in intended use conditions. Verification activities include design review, testing, and analysis. Validation typically includes "
                    "clinical studies or performance testing in representative environments. For software, verification includes unit testing, integration testing, and system "
                    "testing. Code review and static analysis detect design flaws before execution. Dynamic testing demonstrates correct behavior. Regression testing confirms "
                    "that changes do not introduce defects. Traceability from requirements through testing demonstrates comprehensive coverage. Validation evidence supports "
                    "claims of safety and effectiveness. For SaMD, clinical evidence may be derived from literature, real-world use data, or clinical studies. Documentation "
                    "of verification and validation results must be retained. Testing scope must be proportionate to risk and intended use. Assessment should verify that "
                    "verification activities adequately test design requirements and that validation evidence supports intended use claims."
                ),
                "keywords": ["verification", "validation", "design review", "testing", "requirements coverage", "clinical evidence", "traceability", "safety claims"],
            },
            "cybersecurity": {
                "title": "Cybersecurity Risk Management",
                "part": "EU MDR, Annex I, Section 2",
                "clause": "Software Security Requirements",
                "content": (
                    "Software must be protected against cybersecurity risks. A cybersecurity risk assessment must identify threats, vulnerabilities, and potential impact. "
                    "Threat modeling identifies attack vectors. Vulnerability assessment discovers implementation flaws. Risk controls might include authentication, encryption, "
                    "input validation, access controls, and secure update mechanisms. Penetration testing probes for undiscovered vulnerabilities. Software composition analysis "
                    "identifies risks in third-party components. Security updates must be available to address discovered vulnerabilities. Update procedures must maintain "
                    "device safety and effectiveness. For networked and IoT medical devices, cybersecurity becomes increasingly critical. Software must include integrity "
                    "checks to detect unauthorized modifications. Audit trails enable detection of security breaches. For devices used in critical healthcare roles, breach "
                    "impact could be severe, requiring higher security controls. Testing should validate that cybersecurity controls function correctly and that software "
                    "resists common attacks."
                ),
                "keywords": ["cybersecurity", "threat modeling", "vulnerability assessment", "penetration testing", "authentication", "encryption", "update mechanism"],
            },
            "update_procedures": {
                "title": "Software Updates and Change Management",
                "part": "EU MDR, Annex III, Section 2.4",
                "clause": "Post-Production Obligations",
                "content": (
                    "Software updates are a fundamental mechanism for maintaining device safety and addressing emerging risks. Update procedures must be documented and "
                    "implemented rigorously. Each update must be tracked with unique identification and documentation of changes. Updates addressing safety concerns must "
                    "be validated to ensure they correctly address the issue without introducing new defects. Installation procedures must be clear and tested. Rollback "
                    "procedures should enable reversal if an update introduces problems. Mandatory vs. optional update decisions must be risk-based. For critical safety updates, "
                    "organizations may push updates automatically to ensure widespread deployment. For lower-risk updates, user notification and voluntary installation may "
                    "be acceptable. Version control must track software deployed in the field. Post-market surveillance must monitor update deployment and effectiveness. "
                    "Testing should verify that update installation works correctly, that updates address intended issues, and that devices continue functioning safely after "
                    "updates. Procedures should handle update failure scenarios."
                ),
                "keywords": ["software updates", "change management", "update procedures", "version tracking", "rollback", "post-market surveillance", "deployment"],
            },
            "post_market_surveillance": {
                "title": "Post-Market Surveillance and Adverse Events",
                "part": "EU MDR, Article 80-84",
                "clause": "Post-Market Surveillance Plan",
                "content": (
                    "Manufacturers must establish post-market surveillance plans to collect and analyze data on device safety and performance. Adverse event monitoring "
                    "includes direct reports from users and healthcare professionals, literature searches, regulatory database reviews, and helpdesk data. Analysis must "
                    "identify trends and correlations. Signal detection flagges potential safety issues requiring investigation. Trend analysis reveals patterns suggesting "
                    "systematic problems. For software, post-market data may reveal edge cases not discovered during development. Updates may be required to address newly "
                    "identified issues. Serious adverse events must be reported to authorities within specified timeframes. Post-market surveillance obligations continue "
                    "for the device lifetime and beyond. Documentation of surveillance activities must be retained. For software, version tracking enables correlation "
                    "between software versions and reported issues. Testing from post-market surveillance findings feeds back into development for future versions. Assessment "
                    "should verify that post-market surveillance plans are comprehensive, that adverse event data is actively monitored, and that trends are promptly "
                    "investigated."
                ),
                "keywords": ["post-market surveillance", "adverse events", "signal detection", "trend analysis", "reporting", "version tracking", "regulatory", "investigation"],
            },
        },
    },
}
