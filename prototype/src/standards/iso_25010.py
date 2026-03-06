"""
ISO/IEC 25010:2023 — Software Product Quality Model.

Defines the quality characteristics and sub-characteristics that the
Architect agent uses for non-functional requirements mapping.

This module provides comprehensive quality characteristics across eight
main dimensions: functional suitability, performance efficiency, compatibility,
usability, reliability, security, maintainability, and portability.

Each characteristic includes sub-characteristics with detailed definitions,
quality metrics, testing approaches, and common defect patterns.

References:
    - ISO/IEC 25010:2023 Systems and software Quality Requirements and Evaluation (SQuaRE)
    - Product quality model
"""

STANDARD_ID = "ISO/IEC 25010:2023"

SECTIONS: dict[str, dict] = {
    "25010:2023": {
        "title": "Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model",
        "sections": {
            "functional_suitability": {
                "part": "Part 1",
                "clause": "4.1",
                "title": "Functional Suitability",
                "content": (
                    "Functional Suitability is the degree to which a product or system provides functions that meet "
                    "stated and implied needs when used under specified conditions. It encompasses the extent to which "
                    "implemented functions match user expectations and requirements, encompassing both explicit requirements "
                    "and implied user needs derived from business context and domain standards. The quality of functional "
                    "suitability directly impacts user satisfaction and determines whether a system can accomplish its intended "
                    "business objectives. Assessment involves comparing actual system behavior against requirements specifications, "
                    "user stories, and acceptance criteria across normal and edge-case scenarios."
                ),
                "keywords": ["functional", "completeness", "correctness", "appropriateness", "requirements", "functions"],
                "sub_characteristics": {
                    "functional_completeness": {
                        "title": "Functional Completeness",
                        "definition": (
                            "The degree to which the set of functions covers all specified tasks and user objectives. "
                            "This characteristic measures whether all required functionality described in requirements and use cases "
                            "has been implemented in the product. Completeness is often measured as the ratio of implemented features "
                            "to required features, accounting for prioritization and scope decisions. Incomplete functionality can leave "
                            "users unable to perform critical tasks or workarounds, impacting system utility and user productivity."
                        ),
                        "quality_metrics": [
                            "Percentage of required features implemented",
                            "Feature coverage ratio",
                            "Requirements traceability percentage",
                            "Use case implementation rate",
                            "Test case coverage against requirements"
                        ],
                        "testing_approaches": [
                            "Requirements-based testing: map each requirement to test cases",
                            "Use case testing: execute complete business scenarios",
                            "Features audit: verify all listed features are accessible and functional",
                            "Requirements traceability matrix review",
                            "User acceptance testing against feature checklist"
                        ],
                        "common_defect_patterns": [
                            "Missing features entirely unimplemented",
                            "Partial implementation of features (incomplete workflows)",
                            "Features hidden or inaccessible through UI",
                            "Features missing in specific product variants or configurations",
                            "Requirements misunderstood leading to incomplete implementations"
                        ]
                    },
                    "functional_correctness": {
                        "title": "Functional Correctness",
                        "definition": (
                            "The degree to which a product provides correct results with the needed degree of precision. "
                            "Correctness addresses both logical accuracy and numerical/data precision, ensuring computations, "
                            "transformations, and business logic operations produce expected outputs. This includes verification that "
                            "data integrity is maintained through processing, calculations match specifications, and state transitions "
                            "occur correctly. Correctness failures can have severe consequences in safety-critical, financial, or "
                            "data-sensitive applications, making this a critical quality characteristic."
                        ),
                        "quality_metrics": [
                            "Percentage of test cases passed",
                            "Defect detection rate in correctness category",
                            "Calculation error frequency",
                            "Data consistency violations",
                            "Business logic error count"
                        ],
                        "testing_approaches": [
                            "Black-box functional testing with boundary value analysis",
                            "Data-driven testing with expected output validation",
                            "Mathematical/algorithmic verification testing",
                            "State machine testing to verify correct state transitions",
                            "Precision testing for floating-point and financial calculations"
                        ],
                        "common_defect_patterns": [
                            "Incorrect business logic implementation",
                            "Off-by-one errors in loops and array access",
                            "Incorrect operator precedence in calculations",
                            "Floating-point precision loss in financial calculations",
                            "Incorrect conditional logic (wrong operators, inversions)",
                            "Data transformation errors (encoding, type conversion)",
                            "Race conditions causing incorrect state"
                        ]
                    },
                    "functional_appropriateness": {
                        "title": "Functional Appropriateness",
                        "definition": (
                            "The degree to which functions facilitate the accomplishment of specified tasks and objectives "
                            "in ways that are suitable for the user's context and work process. Beyond mere existence of features, "
                            "appropriateness evaluates whether implemented functions are presented in logical groupings, "
                            "accessible through efficient interaction patterns, and aligned with user workflow. This includes "
                            "considering whether the functional scope matches user expectations and whether additional convenience "
                            "features accelerate task completion. Inappropriately designed functions may exist but fail to meet user needs effectively."
                        ),
                        "quality_metrics": [
                            "User task completion rate and time",
                            "Feature utilization frequency",
                            "User satisfaction with feature presentation",
                            "Workflow efficiency metrics",
                            "Task abandonment rate"
                        ],
                        "testing_approaches": [
                            "User acceptance testing with realistic workflows",
                            "Usability testing observing user task execution",
                            "Workflow analysis and optimization testing",
                            "Survey-based user feedback collection",
                            "A/B testing alternative feature implementations"
                        ],
                        "common_defect_patterns": [
                            "Features poorly organized in user interface",
                            "Inefficient workflows requiring excessive steps",
                            "Missing convenience features that speed common tasks",
                            "Features grouped inappropriately causing user confusion",
                            "Inadequate shortcuts or keyboard navigation",
                            "Functions requiring context switches between screens"
                        ]
                    }
                }
            },
            "performance_efficiency": {
                "part": "Part 1",
                "clause": "4.2",
                "title": "Performance Efficiency",
                "content": (
                    "Performance Efficiency describes the relationship between the level of performance of a product "
                    "and the amount of resources used under stated conditions. It encompasses both absolute performance metrics "
                    "(how fast operations complete) and resource efficiency (how well system resources are utilized). This characteristic "
                    "is critical in systems serving multiple users, processing large datasets, or operating under resource constraints "
                    "such as mobile devices or embedded systems. Performance degradation can significantly impact user experience, "
                    "system availability, and operational costs, particularly in high-volume transaction processing or data-intensive applications. "
                    "Acceptable performance thresholds must be defined during requirements analysis, accounting for user expectations, "
                    "SLAs, and competitive benchmarks."
                ),
                "keywords": ["performance", "latency", "throughput", "capacity", "load", "resource", "efficiency", "scalability"],
                "sub_characteristics": {
                    "time_behaviour": {
                        "title": "Time Behaviour",
                        "definition": (
                            "The degree to which response times, processing times, and throughput rates meet specified requirements. "
                            "Time behaviour measures latency (time to first response), throughput (transactions per unit time), "
                            "and processing duration for various operations. Different operations may have different acceptable "
                            "time windows (interactive operations typically need <100ms response; batch operations may tolerate minutes). "
                            "Time behaviour is user-perceivable and directly impacts satisfaction; even high-correctness systems "
                            "perceived as slow degrade user experience significantly."
                        ),
                        "quality_metrics": [
                            "Response time (p50, p95, p99 percentiles)",
                            "Throughput (requests/second, transactions/second)",
                            "Processing latency by operation type",
                            "Time to first byte (TTFB)",
                            "API endpoint response time distribution",
                            "Database query execution time"
                        ],
                        "testing_approaches": [
                            "Load testing with realistic user load profiles",
                            "Latency measurement during baseline testing",
                            "Response time profiling across operations",
                            "Scalability testing: measure response time degradation with increasing load",
                            "Real user monitoring (RUM) and synthetic monitoring"
                        ],
                        "common_defect_patterns": [
                            "N+1 query problems in database access",
                            "Inefficient algorithms with poor time complexity",
                            "Memory leaks causing gradual performance degradation",
                            "Blocking I/O in multi-threaded environments",
                            "Unoptimized search or filtering algorithms",
                            "Excessive network round-trips for data retrieval",
                            "Missing database indexes on commonly searched fields"
                        ]
                    },
                    "resource_utilization": {
                        "title": "Resource Utilization",
                        "definition": (
                            "The degree to which CPU, memory, disk storage, and network bandwidth are used efficiently. "
                            "Resource utilization metrics measure consumption relative to workload; efficient systems accomplish "
                            "more work with fewer resources. Over-consumption leads to higher operational costs (cloud computing charges), "
                            "environmental impact, and can prevent systems from scaling to support business growth. Different resource "
                            "constraints apply to different deployment scenarios: cloud applications prioritize memory and CPU efficiency; "
                            "mobile applications prioritize battery and memory; desktop applications may be less constrained but still "
                            "subject to user expectations about system impact."
                        ),
                        "quality_metrics": [
                            "Memory consumption (peak, average, per-user)",
                            "CPU utilization percentage",
                            "Disk I/O rate and efficiency",
                            "Network bandwidth consumption",
                            "Memory leak detection rate",
                            "Resource consumption per transaction",
                            "Cache hit ratio"
                        ],
                        "testing_approaches": [
                            "Memory profiling and leak detection testing",
                            "CPU profiling to identify hot spots",
                            "Disk I/O monitoring during extended testing",
                            "Network traffic analysis",
                            "Long-duration stress testing to detect leaks",
                            "Comparison testing: resource consumption baseline vs. optimized",
                            "Monitoring resource consumption across deployment environments"
                        ],
                        "common_defect_patterns": [
                            "Memory leaks in connection pooling or caching",
                            "Unbounded data structure growth (queues, caches)",
                            "Excessive logging causing disk and CPU overhead",
                            "Inefficient serialization/deserialization",
                            "Large data structure allocations in loops",
                            "Missing resource cleanup (file handles, database connections)",
                            "Cached data never invalidated or garbage collected"
                        ]
                    },
                    "capacity": {
                        "title": "Capacity",
                        "definition": (
                            "The degree to which maximum limits of product parameters meet specified requirements. "
                            "Capacity defines scalability boundaries: maximum concurrent users, peak transactions per second, "
                            "maximum data volume supported, and maximum transaction size. Capacity planning ensures systems can "
                            "accommodate expected business growth and peak load scenarios. Capacity constraints manifest as service "
                            "degradation or failures when limits are approached. Understanding and communicating capacity boundaries "
                            "is essential for operational planning and customer expectation management."
                        ),
                        "quality_metrics": [
                            "Maximum concurrent users supported",
                            "Peak transactions per second (TPS)",
                            "Maximum data volume (GB/TB)",
                            "Maximum transaction size (bytes/records)",
                            "Connection pool capacity",
                            "Queue depth limits",
                            "Headroom before performance degradation"
                        ],
                        "testing_approaches": [
                            "Load testing to capacity limits",
                            "Spike testing: sudden load increase to peak levels",
                            "Endurance testing: sustained load over extended periods",
                            "Capacity limit testing: progressively increase load until failure",
                            "Data volume testing: exercise with maximum expected data sizes",
                            "Concurrency testing: stress test with maximum user counts"
                        ],
                        "common_defect_patterns": [
                            "Connection pool exhaustion under load",
                            "Out of memory errors at high concurrency",
                            "Database connection limits exceeded",
                            "Queue overflow causing message loss",
                            "Thread pool saturation",
                            "File descriptor exhaustion",
                            "Hardcoded limits preventing scaling"
                        ]
                    }
                }
            },
            "compatibility": {
                "part": "Part 1",
                "clause": "4.3",
                "title": "Compatibility",
                "content": (
                    "Compatibility describes the degree to which a product can exchange information with other products "
                    "and perform its required functions while sharing the same hardware or software environment. In modern "
                    "interconnected systems, few applications operate in isolation; most must integrate with existing platforms, "
                    "databases, services, and third-party components. Compatibility encompasses both data interchange (the ability "
                    "to read/write common formats and communicate through standard protocols) and operational co-existence (ability "
                    "to run alongside other software without conflicts). Compatibility failures often emerge only in integration "
                    "testing or production environments when actual system landscapes are encountered."
                ),
                "keywords": ["compatibility", "interoperability", "co-existence", "integration", "standards", "protocols"],
                "sub_characteristics": {
                    "co_existence": {
                        "title": "Co-existence",
                        "definition": (
                            "The degree to which a product can operate alongside other products without detrimental impact. "
                            "Co-existence addresses shared resource consumption (disk space, memory, CPU), port conflicts, "
                            "service interference, and environmental variable collisions. Applications must not monopolize shared "
                            "resources, interfere with other services, or make exclusive demands on system infrastructure. "
                            "Co-existence testing is often neglected until production deployment reveals conflicts with existing systems."
                        ),
                        "quality_metrics": [
                            "Successful parallel installation with other products",
                            "Absence of resource conflicts",
                            "Service interference incidents",
                            "Port/socket conflict count",
                            "Registry/configuration collision count",
                            "Successful operation with typical system configurations"
                        ],
                        "testing_approaches": [
                            "Installation testing on systems with competing software",
                            "Resource conflict testing (ports, memory, disk)",
                            "Service interaction testing",
                            "Dependency conflict verification",
                            "Testing with common antivirus, firewall, and security software",
                            "Multi-application performance measurement"
                        ],
                        "common_defect_patterns": [
                            "Hardcoded port numbers causing conflicts",
                            "Exclusive resource claims preventing concurrent operation",
                            "Shared library version conflicts",
                            "Registry/configuration file collisions",
                            "Global state not properly isolated",
                            "Dependency version incompatibilities",
                            "Temporary file name collisions"
                        ]
                    },
                    "interoperability": {
                        "title": "Interoperability",
                        "definition": (
                            "The degree to which a product can exchange information with other systems and make use of that "
                            "information. Interoperability addresses data format compatibility (JSON, XML, CSV, proprietary formats), "
                            "protocol compatibility (HTTP, REST, SOAP, gRPC), and semantic compatibility (shared understanding of "
                            "data meaning). Modern systems rarely operate as silos; they integrate through APIs, message queues, "
                            "databases, and file exchanges. Interoperability requirements must specify target systems, supported formats, "
                            "API versions, and protocol versions."
                        ),
                        "quality_metrics": [
                            "Successful data exchange with specified systems",
                            "Format compatibility compliance",
                            "API version compatibility",
                            "Protocol version support",
                            "Data transformation accuracy",
                            "Integration test pass rate"
                        ],
                        "testing_approaches": [
                            "API contract testing against published specifications",
                            "Data format testing (serialization/deserialization)",
                            "Protocol compliance testing",
                            "Integration testing with actual partner systems",
                            "Version compatibility testing",
                            "Mock/stub testing of external system interactions",
                            "End-to-end integration scenarios"
                        ],
                        "common_defect_patterns": [
                            "API version mismatches",
                            "Missing or incorrect data format conversion",
                            "Protocol implementation deviations",
                            "Data type conversion errors between systems",
                            "Incomplete API implementation",
                            "Missing error handling for malformed external data",
                            "Timeout handling for slow external systems"
                        ]
                    }
                }
            },
            "usability": {
                "part": "Part 1",
                "clause": "4.4",
                "title": "Usability",
                "content": (
                    "Usability is the degree to which a product can be used by specified users to achieve specified goals "
                    "with effectiveness, efficiency, and satisfaction in a specified context of use. Usability extends beyond "
                    "aesthetic design to encompass the entire user experience: how intuitively users understand the system, how "
                    "easily they learn to operate it, how efficiently they accomplish tasks, and how satisfied they feel using it. "
                    "Usability is particularly critical for systems serving diverse user populations with varying technical expertise. "
                    "Poor usability results in user frustration, decreased productivity, reduced adoption, support costs, and potential "
                    "safety issues. Usability assessment requires user-centric testing methodologies including observation, interviews, "
                    "and accessibility evaluation."
                ),
                "keywords": ["usability", "learnability", "accessibility", "UX", "user interface", "effectiveness", "efficiency", "satisfaction"],
                "sub_characteristics": {
                    "appropriateness_recognizability": {
                        "title": "Appropriateness Recognizability",
                        "definition": (
                            "The degree to which it is clear to users that a product is appropriate for their needs. "
                            "Recognizability addresses whether the system's purpose, capabilities, and suitable use cases are "
                            "immediately apparent to potential users. This includes clear value proposition communication, visible "
                            "feature sets that align with stated objectives, and absence of misleading interface cues. Users should "
                            "quickly understand whether a product meets their requirements without extended exploration. Failure in "
                            "recognizability leads to user rejection or misuse of systems."
                        ),
                        "quality_metrics": [
                            "Time to recognize system purpose and capabilities",
                            "Percentage of users who immediately understand value",
                            "Feature discovery rate",
                            "User feedback on perceived relevance",
                            "First-impression satisfaction rating"
                        ],
                        "testing_approaches": [
                            "First-time user testing and feedback",
                            "Onboarding testing with target user personas",
                            "Feature visibility audit",
                            "Value proposition clarity testing",
                            "User interviews about perceived purpose and capabilities"
                        ],
                        "common_defect_patterns": [
                            "Unclear value proposition in UI",
                            "Features hidden or difficult to discover",
                            "Confusing terminology not aligned with user domain",
                            "Visual design suggesting wrong system purpose",
                            "Missing help documentation for quick understanding"
                        ]
                    },
                    "learnability": {
                        "title": "Learnability",
                        "definition": (
                            "The degree to which a product can be learned by a specified user. Learnability measures how quickly "
                            "users progress from novice to competent operation. This includes the time required to perform basic tasks, "
                            "presence of effective learning aids (tooltips, help, tutorials), consistency of interaction patterns, "
                            "and error message clarity. Systems with poor learnability create support burden and user frustration. "
                            "Learnability is especially critical for infrequently-used features or for systems serving occasional users "
                            "who cannot develop expertise through frequent use."
                        ),
                        "quality_metrics": [
                            "Time to perform first task independently",
                            "Time to competency (80% task efficiency)",
                            "Support request frequency from new users",
                            "Tutorial/help system usage effectiveness",
                            "Error rate for novice users",
                            "User confidence growth over time"
                        ],
                        "testing_approaches": [
                            "Usability testing with first-time users",
                            "Learning curve measurement",
                            "Tutorial effectiveness evaluation",
                            "Online help and documentation effectiveness",
                            "Contextual help (tooltips) testing",
                            "Error message clarity assessment",
                            "Task-based learning testing without guidance"
                        ],
                        "common_defect_patterns": [
                            "Inconsistent interaction patterns across features",
                            "Unclear error messages or error recovery steps",
                            "Hidden or non-obvious functionality",
                            "Missing helpful hints or contextual help",
                            "Tutorials too simplistic or overly complex",
                            "Terminology inconsistency between help and UI",
                            "High cognitive load for complex operations"
                        ]
                    },
                    "operability": {
                        "title": "Operability",
                        "definition": (
                            "The degree to which a product can be operated easily and comfortably. Operability encompasses UI "
                            "responsiveness, clear navigation, intuitive control mechanisms, and minimal required steps to accomplish "
                            "common tasks. Users should be able to operate the system comfortably for extended periods without fatigue "
                            "or frustration. This includes accessibility of controls, logical workflow sequences, and absence of "
                            "needless complexity. Poor operability manifests in user complaints about awkwardness, excessive clicking, "
                            "and inefficient workflows."
                        ),
                        "quality_metrics": [
                            "Steps required to accomplish common tasks",
                            "UI responsiveness/latency",
                            "Navigation clarity rating",
                            "User comfort/satisfaction during operation",
                            "Keyboard shortcut utilization",
                            "User-reported operational friction"
                        ],
                        "testing_approaches": [
                            "Workflow efficiency testing",
                            "Task step count analysis",
                            "Keyboard navigation testing",
                            "Navigation architecture review",
                            "UI responsiveness measurement",
                            "Usability testing for operational comfort",
                            "Accessibility testing for various input modalities"
                        ],
                        "common_defect_patterns": [
                            "Excessive steps for common tasks",
                            "Missing keyboard navigation or shortcuts",
                            "Unresponsive UI elements causing perceived freezing",
                            "Poor button/control placement requiring excessive movement",
                            "Non-intuitive navigation requiring exploration",
                            "Modeless dialogs blocking needed functionality",
                            "Missing undo/cancel recovery mechanisms"
                        ]
                    },
                    "user_error_protection": {
                        "title": "User Error Protection",
                        "definition": (
                            "The degree to which a product protects users against making errors. Error protection includes "
                            "input validation preventing invalid entries, warnings before destructive actions, confirmation dialogs, "
                            "undo functionality, and recovery mechanisms. Systems should gracefully handle user mistakes through "
                            "informative error messages and paths to correction. Effective error protection reduces support burden and "
                            "user frustration, while also preventing data corruption or loss. Error protection is critical in safety-critical "
                            "systems and high-stakes financial applications."
                        ),
                        "quality_metrics": [
                            "Percentage of user errors caught and prevented",
                            "Destructive action confirmation effectiveness",
                            "Error recovery success rate",
                            "Undo functionality coverage",
                            "Input validation completeness",
                            "Error message usefulness rating"
                        ],
                        "testing_approaches": [
                            "Negative testing: deliberate invalid input submission",
                            "Boundary value error testing",
                            "Destructive action testing (delete, clear, overwrite)",
                            "Undo/redo functionality testing",
                            "Error message clarity and correctness testing",
                            "Usability testing observing user error patterns",
                            "Edge case error handling verification"
                        ],
                        "common_defect_patterns": [
                            "Missing input validation",
                            "Insufficient validation error messages",
                            "Allowing destructive actions without confirmation",
                            "Missing undo capability for reversible operations",
                            "Unclear error messages not indicating correction steps",
                            "Allowing invalid state transitions",
                            "No recovery options after errors"
                        ]
                    },
                    "user_interface_aesthetics": {
                        "title": "User Interface Aesthetics",
                        "definition": (
                            "The degree to which a user interface is visually appealing and well-designed. UI aesthetics encompass "
                            "visual consistency, color harmony, typography clarity, appropriate use of whitespace, and overall design "
                            "coherence. While aesthetics might seem superficial compared to functionality, they significantly impact "
                            "user perception of quality, professional credibility, and satisfaction. Aesthetically pleasing interfaces "
                            "also facilitate usability through improved visual hierarchy and reduced cognitive load."
                        ),
                        "quality_metrics": [
                            "User satisfaction with visual design",
                            "Design consistency scoring",
                            "Visual element alignment and spacing",
                            "Color contrast ratios",
                            "Typography readability metrics",
                            "Professional appearance rating"
                        ],
                        "testing_approaches": [
                            "Design review against aesthetic standards",
                            "User feedback on visual appeal",
                            "Visual consistency testing across pages/screens",
                            "Color contrast and readability testing",
                            "Design pattern consistency audit",
                            "Responsive design testing across devices",
                            "Accessibility color testing (color-blind simulation)"
                        ],
                        "common_defect_patterns": [
                            "Inconsistent colors across interface",
                            "Misaligned or poorly spaced elements",
                            "Clashing color combinations",
                            "Excessive visual elements or clutter",
                            "Poor typography readability",
                            "Inconsistent button styles or iconography",
                            "Outdated or unprofessional visual design"
                        ]
                    },
                    "accessibility": {
                        "title": "Accessibility",
                        "definition": (
                            "The degree to which a product is usable by people with the widest range of characteristics and "
                            "capabilities, including people with disabilities. Accessibility addresses visual, auditory, motor, and "
                            "cognitive disabilities through design principles and technologies. This includes screen reader compatibility, "
                            "keyboard navigation, color contrast for low-vision users, closed captions for deaf users, and cognitive "
                            "simplification for users with intellectual disabilities. Accessibility is both an ethical imperative and "
                            "increasingly a legal requirement (ADA, WCAG 2.2, Section 508). Accessible design benefits all users, not "
                            "just those with disabilities (e.g., keyboard shortcuts benefit power users; clear language benefits non-native speakers)."
                        ),
                        "quality_metrics": [
                            "WCAG 2.2 compliance level (A, AA, AAA)",
                            "Screen reader compatibility testing results",
                            "Keyboard navigation coverage",
                            "Color contrast ratio compliance",
                            "Focus visibility on all interactive elements",
                            "Accessibility violations count",
                            "Assistive technology compatibility"
                        ],
                        "testing_approaches": [
                            "WCAG 2.2 compliance testing",
                            "Screen reader testing (NVDA, JAWS, VoiceOver)",
                            "Keyboard-only navigation testing",
                            "Color contrast measurement tools",
                            "Accessibility automated scanning",
                            "Testing with users who have disabilities",
                            "Voice/speech input testing",
                            "Magnification and zoom testing"
                        ],
                        "common_defect_patterns": [
                            "Missing alt text for images",
                            "Color used as sole means of conveying information",
                            "Missing focus indicators",
                            "Keyboard navigation not possible for all controls",
                            "Missing form labels or incorrect label associations",
                            "Automatic media playback without pause control",
                            "Flashing or blinking content triggering seizures",
                            "Missing closed captions for videos",
                            "Non-semantic HTML structure"
                        ]
                    }
                }
            },
            "reliability": {
                "part": "Part 1",
                "clause": "4.5",
                "title": "Reliability",
                "content": (
                    "Reliability is the degree to which a system or product performs specified functions under specified "
                    "conditions for a specified period of time. Reliability encompasses the system's ability to maintain correct "
                    "operation through normal usage, handle hardware and software faults gracefully, and recover to a consistent "
                    "state after failures. Reliability is foundational to user trust and critical for mission-critical systems where "
                    "failures cause financial loss, safety hazards, or service disruption. Reliability assessment requires extended "
                    "testing including stress testing, fault injection, and extended duration testing to detect latent defects. Modern "
                    "systems employ redundancy, monitoring, and automated recovery to achieve high reliability despite component failures."
                ),
                "keywords": ["reliability", "availability", "fault tolerance", "recovery", "uptime", "RTO", "RPO", "MTBF", "MTTF"],
                "sub_characteristics": {
                    "maturity": {
                        "title": "Maturity",
                        "definition": (
                            "The degree to which a system meets needs for reliability under normal operation. Maturity measures "
                            "the probability that a system will fail during a reference mission period under normal conditions. This "
                            "characteristic captures defect density and the effectiveness of quality assurance processes. Systems become "
                            "more mature as defects are discovered and corrected, and through extended usage revealing latent defects. "
                            "Mean Time Between Failures (MTBF) is a common maturity metric expressing average operation duration between failures."
                        ),
                        "quality_metrics": [
                            "Defect density (defects per lines of code)",
                            "Mean Time Between Failures (MTBF)",
                            "Failure rate",
                            "Test coverage percentage",
                            "Escaped defect count post-release",
                            "Stability during extended use"
                        ],
                        "testing_approaches": [
                            "Extended duration testing (soak testing)",
                            "Stress testing to failure",
                            "Defect injection testing",
                            "Regression testing after fixes",
                            "Field testing in production-like environments",
                            "Beta testing to identify edge case failures",
                            "Accelerated life testing with elevated stress"
                        ],
                        "common_defect_patterns": [
                            "Memory leaks causing eventual failure",
                            "File descriptor leaks exhausting resources",
                            "Connection pool exhaustion",
                            "Unhandled null pointer exceptions",
                            "Uncaught exceptions causing crashes",
                            "State corruption under specific sequences",
                            "Race conditions manifesting intermittently",
                            "Timer/scheduling issues"
                        ]
                    },
                    "availability": {
                        "title": "Availability",
                        "definition": (
                            "The degree to which a system is operational and accessible when required. Availability is often "
                            "expressed as a percentage of uptime (e.g., 99.9% availability allows ~8.75 hours downtime annually). "
                            "Availability depends on reliability (fewer failures) and recoverability (faster recovery). Modern systems "
                            "achieve high availability through redundancy, load balancing, automated failover, and monitoring. Service "
                            "Level Agreements (SLAs) typically specify availability targets and consequences for missing them. Availability "
                            "is critical for revenue-generating or mission-critical systems where downtime has direct financial or operational impact."
                        ),
                        "quality_metrics": [
                            "Uptime percentage (99%, 99.9%, 99.99%)",
                            "Downtime hours annually",
                            "Planned vs. unplanned downtime",
                            "Mean Time To Repair (MTTR)",
                            "Scheduled maintenance window duration",
                            "SLA compliance percentage"
                        ],
                        "testing_approaches": [
                            "Redundancy and failover testing",
                            "Load balancer testing",
                            "Infrastructure failure simulation",
                            "Database failover testing",
                            "Monitoring and alerting effectiveness",
                            "Graceful degradation testing",
                            "Zero-downtime deployment validation"
                        ],
                        "common_defect_patterns": [
                            "Single points of failure (no redundancy)",
                            "Failover mechanisms not automatically triggered",
                            "Data loss during failover",
                            "Extended recovery time after failures",
                            "Cascading failures due to poor isolation",
                            "Manual intervention required for failover",
                            "Monitoring systems unable to detect failures"
                        ]
                    },
                    "fault_tolerance": {
                        "title": "Fault Tolerance",
                        "definition": (
                            "The degree to which a system continues to operate correctly despite hardware or software faults. "
                            "Fault tolerance addresses component failures (hardware errors, service outages), software bugs (latent "
                            "defects), and data corruption. This is achieved through redundancy, error detection and correction, "
                            "and isolated failure domains. Fault tolerance must be designed in from the start; it cannot be added "
                            "to poorly architected systems. Byzantine fault tolerance (handling malicious faults) applies to distributed "
                            "consensus systems."
                        ),
                        "quality_metrics": [
                            "Fault tolerance coverage percentage",
                            "Mean Time To Detect (MTTD)",
                            "Mean Time To Isolate (MTTI)",
                            "Failure propagation prevented",
                            "Recovery success rate",
                            "Data corruption incidents"
                        ],
                        "testing_approaches": [
                            "Fault injection testing (hardware, network, software)",
                            "Chaos engineering testing",
                            "Network partition simulation",
                            "Disk failure simulation",
                            "Service dependency failure testing",
                            "Cascading failure prevention testing",
                            "Graceful degradation testing"
                        ],
                        "common_defect_patterns": [
                            "Assumptions about component availability",
                            "Missing timeout handling for slow components",
                            "Unbounded retry loops",
                            "Global error conditions affecting entire system",
                            "Cascading failures through service calls",
                            "Missing circuit breaker patterns",
                            "Insufficient error logging for troubleshooting"
                        ]
                    },
                    "recoverability": {
                        "title": "Recoverability",
                        "definition": (
                            "The degree to which a system can recover data and re-establish the desired operational state "
                            "after an interruption or failure. Recoverability encompasses backup strategies, disaster recovery procedures, "
                            "transaction rollback mechanisms, and state restoration. Recovery objectives are defined as Recovery Time "
                            "Objective (RTO: maximum acceptable downtime) and Recovery Point Objective (RPO: maximum acceptable data loss). "
                            "Recoverability must be regularly tested through disaster recovery drills to ensure procedures are effective "
                            "and personnel are trained."
                        ),
                        "quality_metrics": [
                            "Recovery Time Objective (RTO) achievement",
                            "Recovery Point Objective (RPO) achievement",
                            "Backup completeness and accuracy",
                            "Restore time from backups",
                            "Data recovery success rate",
                            "Transaction rollback success rate"
                        ],
                        "testing_approaches": [
                            "Disaster recovery testing and drills",
                            "Backup restoration testing",
                            "Point-in-time recovery testing",
                            "Transaction rollback testing",
                            "Data consistency verification after recovery",
                            "Recovery automation effectiveness testing",
                            "Backup integrity verification"
                        ],
                        "common_defect_patterns": [
                            "Backups not being created successfully",
                            "Backups not tested regularly",
                            "Manual recovery procedures that are error-prone",
                            "Incomplete data backups",
                            "Recovery procedures requiring excessive time",
                            "Lost logs preventing transaction reconstruction",
                            "Inconsistent state after partial recovery"
                        ]
                    }
                }
            },
            "security": {
                "part": "Part 1",
                "clause": "4.6",
                "title": "Security",
                "content": (
                    "Security is the degree to which a product protects information and data so that persons or other "
                    "products have the degree of data access appropriate to their type and level of authorization. Security "
                    "addresses confidentiality (data visible only to authorized parties), integrity (data unchanged without authorization), "
                    "availability (authorized access not denied), authenticity (verifiable identity), and non-repudiation (actions provably "
                    "attributable to parties). Security breaches can result in regulatory fines (GDPR, HIPAA), financial loss, reputational "
                    "damage, and legal liability. Security must be addressed throughout the development lifecycle through threat modeling, "
                    "secure coding, code review, penetration testing, and vulnerability management. OWASP publishes authoritative guidance on "
                    "web application security vulnerabilities and mitigation strategies."
                ),
                "keywords": ["security", "confidentiality", "integrity", "authentication", "authorization", "OWASP", "encryption", "vulnerability"],
                "sub_characteristics": {
                    "confidentiality": {
                        "title": "Confidentiality",
                        "definition": (
                            "The degree to which data is accessible only to authorized individuals or systems. Confidentiality "
                            "protection encompasses both data in transit (encryption during network transmission) and data at rest "
                            "(encryption in storage). Confidentiality breaches expose sensitive information including personally identifiable "
                            "information (PII), financial records, trade secrets, and health information. Methods include access controls, "
                            "encryption, and secure key management. Regulatory requirements often mandate specific confidentiality protections "
                            "and breach notification requirements."
                        ),
                        "quality_metrics": [
                            "Unauthorized access attempts blocked",
                            "Data classification coverage",
                            "Encryption coverage for sensitive data",
                            "Access control policy compliance",
                            "Audit log completeness",
                            "Data exposure incidents"
                        ],
                        "testing_approaches": [
                            "Penetration testing for unauthorized access",
                            "Access control testing with various user roles",
                            "Encryption verification (TLS/SSL version, cipher strength)",
                            "Data leakage testing (logs, error messages, backups)",
                            "Insecure direct object reference (IDOR) testing",
                            "Session management testing",
                            "Testing for data exposure in backups/logs"
                        ],
                        "common_defect_patterns": [
                            "Passwords transmitted over unencrypted connections",
                            "Sensitive data in logs or error messages",
                            "Missing encryption for data at rest",
                            "Hardcoded credentials",
                            "Weak or missing access controls",
                            "Session tokens not secured (missing HttpOnly, Secure flags)",
                            "Sensitive data in URLs or query parameters",
                            "Information disclosure through error messages"
                        ]
                    },
                    "integrity": {
                        "title": "Integrity",
                        "definition": (
                            "The degree to which data is protected against unauthorized modification. Data integrity ensures "
                            "that information remains accurate, complete, and unchanged during storage and transmission except by "
                            "authorized parties with explicit intent. Integrity is verified through checksums, digital signatures, and "
                            "cryptographic hashes. Without integrity protection, attackers can modify data undetected, leading to data "
                            "corruption, system malfunction, or fraud. Financial systems, medical records, and critical infrastructure "
                            "rely heavily on integrity verification."
                        ),
                        "quality_metrics": [
                            "Unauthorized modification attempts detected",
                            "Checksum/hash verification coverage",
                            "Digital signature validation success rate",
                            "Data corruption incidents detected",
                            "Integrity violation incidents"
                        ],
                        "testing_approaches": [
                            "Modification detection testing (checksums, hashes)",
                            "Digital signature verification",
                            "SQL injection and command injection testing",
                            "Cross-site scripting (XSS) prevention verification",
                            "Input validation testing",
                            "Data consistency verification",
                            "Integrity monitoring effectiveness"
                        ],
                        "common_defect_patterns": [
                            "Missing input validation",
                            "SQL injection vulnerabilities",
                            "Command injection vulnerabilities",
                            "Cross-site scripting (XSS) vulnerabilities",
                            "Missing integrity checks on data transport",
                            "Deserialization of untrusted data",
                            "Lack of change detection mechanisms"
                        ]
                    },
                    "non_repudiation": {
                        "title": "Non-repudiation",
                        "definition": (
                            "The degree to which actions or events can be proven to have taken place and cannot be denied by "
                            "the party responsible. Non-repudiation ensures that a party cannot deny having sent a message, received "
                            "data, or performed an action. This is achieved through digital signatures, audit logs with digital evidence, "
                            "and secure logging mechanisms. Non-repudiation is critical for financial transactions, contracts, and legal "
                            "compliance. Parties must be held accountable for their actions through irrefutable evidence of action and timestamp."
                        ),
                        "quality_metrics": [
                            "Digital signature generation and verification",
                            "Audit log completeness for critical actions",
                            "Timestamp accuracy and precision",
                            "Audit log tampering detection",
                            "Evidence preservation success rate"
                        ],
                        "testing_approaches": [
                            "Digital signature testing and validation",
                            "Audit log generation and review",
                            "Timestamp accuracy verification",
                            "Audit log integrity protection testing",
                            "Log tamper-detection effectiveness",
                            "Action attribution verification"
                        ],
                        "common_defect_patterns": [
                            "Missing digital signatures for critical transactions",
                            "Audit logs not generated for all critical actions",
                            "Timestamps inaccurate or missing",
                            "Audit logs editable or deletable",
                            "Insufficient detail in audit logs for action reconstruction",
                            "Weak cryptography for digital signatures"
                        ]
                    },
                    "accountability": {
                        "title": "Accountability",
                        "definition": (
                            "The degree to which actions traceable to an entity ensure that the entity's actions can be uniquely "
                            "identified and linked to that entity. Accountability creates responsibility for actions through unique "
                            "identification (user IDs, system identifiers), detailed logging of actions, and association of users with "
                            "actions taken on their behalf. Accountability supports both security investigations and regulatory compliance. "
                            "This includes protection against privilege escalation and delegation of authority."
                        ),
                        "quality_metrics": [
                            "User action traceability completeness",
                            "Privilege escalation attempts blocked",
                            "Audit trail completeness",
                            "User identification accuracy",
                            "Session accountability"
                        ],
                        "testing_approaches": [
                            "Privilege escalation testing",
                            "Audit trail verification for each user action",
                            "Identity spoofing testing",
                            "Session hijacking prevention verification",
                            "Multi-user action correlation testing"
                        ],
                        "common_defect_patterns": [
                            "Shared user accounts preventing individual accountability",
                            "Missing user identification in logs",
                            "Actions not attributed to responsible user",
                            "Privilege escalation vulnerabilities",
                            "Insufficient logging detail for accountability",
                            "Anonymous functionality not appropriately restricted"
                        ]
                    },
                    "authenticity": {
                        "title": "Authenticity",
                        "definition": (
                            "The degree to which the identity of a subject or resource can be proven. Authenticity verification "
                            "ensures that parties are who they claim to be and that data originates from claimed sources. Authentication "
                            "mechanisms include password-based authentication, multi-factor authentication, certificate-based authentication, "
                            "and biometric authentication. Authenticity failures allow impersonation and unauthorized access. Modern systems "
                            "typically employ multi-factor authentication combining something you know (password), something you have (device), "
                            "and something you are (biometrics)."
                        ),
                        "quality_metrics": [
                            "Authentication success rate for legitimate users",
                            "False rejection rate (legitimate users denied)",
                            "False acceptance rate (attackers accepted)",
                            "Credential attack resistance",
                            "Multi-factor authentication coverage"
                        ],
                        "testing_approaches": [
                            "Credential validation testing",
                            "Brute force attack resistance testing",
                            "Password strength enforcement testing",
                            "Multi-factor authentication testing",
                            "Single sign-on (SSO) security testing",
                            "Certificate validation testing",
                            "Biometric authentication testing"
                        ],
                        "common_defect_patterns": [
                            "Weak password policies (length, complexity)",
                            "Missing or ineffective rate limiting on login attempts",
                            "Plaintext password storage",
                            "Missing multi-factor authentication",
                            "Session tokens not validated",
                            "Missing certificate pinning in mobile apps",
                            "Insufficient protection against credential stuffing"
                        ]
                    }
                }
            },
            "maintainability": {
                "part": "Part 1",
                "clause": "4.7",
                "title": "Maintainability",
                "content": (
                    "Maintainability is the degree of effectiveness and efficiency with which a product can be modified. "
                    "Maintainability is often the largest total cost of ownership factor for software systems, as they spend most "
                    "of their lifecycle receiving updates, bug fixes, and enhancements rather than initial development. Maintainability "
                    "encompasses code structure (modularity, coupling, cohesion), documentation clarity, test coverage, and consistency "
                    "of design patterns. Systems with high maintainability allow developers to make changes quickly with confidence, while "
                    "low maintainability systems accumulate technical debt that slows all future development. Code reviews, automated testing, "
                    "and architectural governance support maintainability throughout the development lifecycle."
                ),
                "keywords": ["maintainability", "modularity", "testability", "modifiability", "technical debt", "documentation"],
                "sub_characteristics": {
                    "modularity": {
                        "title": "Modularity",
                        "definition": (
                            "The degree to which a system is composed of discrete components such that a change to one component "
                            "has minimal impact on other components. Modularity reduces coupling between components through well-defined "
                            "interfaces and separation of concerns. Modules should have high cohesion (elements within module are closely related) "
                            "and low coupling (dependencies between modules are minimal). Proper modularity allows teams to work on different "
                            "components independently and deploy changes to specific modules without affecting others."
                        ),
                        "quality_metrics": [
                            "Coupling metrics (e.g., LCOM, cyclomatic complexity)",
                            "Module interface stability",
                            "Dependency graph complexity",
                            "Change isolation ability",
                            "Component independence assessment"
                        ],
                        "testing_approaches": [
                            "Unit testing individual modules in isolation",
                            "Module interface contract verification",
                            "Dependency analysis and visualization",
                            "Change impact analysis",
                            "Integration testing between modules",
                            "Architectural compliance testing"
                        ],
                        "common_defect_patterns": [
                            "High coupling through direct object references",
                            "Shared global state between modules",
                            "Bidirectional dependencies between components",
                            "Missing or poorly defined interfaces",
                            "Circular dependencies",
                            "God objects with too many responsibilities",
                            "Hard to test due to entangled dependencies"
                        ]
                    },
                    "reusability": {
                        "title": "Reusability",
                        "definition": (
                            "The degree to which an asset can be used in more than one system, or in building other assets. "
                            "Reusability reduces development time and cost by leveraging existing components. Reusable assets must be "
                            "well-documented, thoroughly tested, and designed for general applicability beyond their initial use case. "
                            "Libraries, frameworks, and reusable components require greater upfront investment in design and documentation "
                            "but pay dividends through reduced development effort across multiple projects."
                        ),
                        "quality_metrics": [
                            "Component reuse frequency",
                            "Code duplication percentage",
                            "Library/framework adoption rate",
                            "Reusable asset quality metrics",
                            "Asset maintenance burden"
                        ],
                        "testing_approaches": [
                            "Testing reusable components in multiple contexts",
                            "API design for general applicability",
                            "Backward compatibility testing for reused libraries",
                            "Code duplication detection and elimination",
                            "Reusable asset quality verification"
                        ],
                        "common_defect_patterns": [
                            "Components too specific to initial use case",
                            "Poorly documented reusable assets",
                            "Inadequate test coverage for reusable components",
                            "Hard-coded assumptions about usage context",
                            "Reusable assets with high maintenance requirements",
                            "APIs that are difficult to learn and use"
                        ]
                    },
                    "analysability": {
                        "title": "Analysability",
                        "definition": (
                            "The degree to which the impact of an intended change can be assessed and understood. Analysability "
                            "requires clear code structure, comprehensive documentation, and good test coverage. Developers must be able "
                            "to understand system behavior, identify what code implements which requirements, and predict consequences of "
                            "proposed changes. Poor analysability leads to excessive time spent investigating code and uncertainty about "
                            "change impacts, increasing risk of introducing defects."
                        ),
                        "quality_metrics": [
                            "Change impact analysis accuracy",
                            "Code comprehension time",
                            "Documentation completeness",
                            "Test coverage percentage",
                            "Defect introduction rate in modifications"
                        ],
                        "testing_approaches": [
                            "Code complexity measurement",
                            "Documentation quality review",
                            "Test coverage analysis",
                            "Change impact analysis effectiveness",
                            "Code readability assessment",
                            "Requirements traceability verification"
                        ],
                        "common_defect_patterns": [
                            "Undocumented code and complex algorithms",
                            "Poor naming conventions (unclear variable/function names)",
                            "Lack of architectural documentation",
                            "Missing requirements traceability",
                            "Complex conditional logic difficult to follow",
                            "Code comments explaining 'what' rather than 'why'",
                            "Inadequate test coverage hiding behavior"
                        ]
                    },
                    "modifiability": {
                        "title": "Modifiability",
                        "definition": (
                            "The degree to which a system can be modified without introducing defects. Modifiability requires "
                            "isolated change locations (changes shouldn't ripple through unrelated code), sufficient test coverage to "
                            "validate changes, and proper separation of concerns. Systems designed for modifiability use design patterns, "
                            "abstraction layers, and composition over inheritance to minimize change impact. Modifiability reduces "
                            "defect risk when implementing fixes or enhancements."
                        ),
                        "quality_metrics": [
                            "Defect rate per modification",
                            "Regression test failure rate",
                            "Change size and scope",
                            "Test coverage of modified code",
                            "Development velocity in mature systems"
                        ],
                        "testing_approaches": [
                            "Regression testing after modifications",
                            "Test coverage analysis for changed code",
                            "Impact analysis for proposed changes",
                            "Mutation testing to verify test effectiveness",
                            "Code review for change risk assessment"
                        ],
                        "common_defect_patterns": [
                            "Changes required in multiple locations for single feature",
                            "Copy-paste code leading to synchronized bugs",
                            "Missing abstraction layers forcing ripple changes",
                            "Insufficient test coverage leaving holes after modifications",
                            "Global state changes affecting unexpected code paths",
                            "Tight coupling making isolated changes impossible"
                        ]
                    },
                    "testability": {
                        "title": "Testability",
                        "definition": (
                            "The degree to which test criteria can be established and tests performed effectively to determine "
                            "whether those criteria have been met. Testability requires clear specification of requirements that can be "
                            "verified, test points that allow observation of behavior, and controllable inputs. High testability enables "
                            "comprehensive testing reducing defect escape. Low testability leads to incomplete testing and undetected defects. "
                            "Designing for testability (dependency injection, interfaces, configurability) improves test effectiveness."
                        ),
                        "quality_metrics": [
                            "Test coverage percentage (statement, branch, etc.)",
                            "Testable code percentage",
                            "Test execution speed",
                            "Defect detection rate",
                            "Escaped defects post-release"
                        ],
                        "testing_approaches": [
                            "Unit test suite coverage measurement",
                            "Integration test coverage",
                            "Test effectiveness (mutation testing)",
                            "Mock/stub effectiveness for isolating units",
                            "Test data generation capabilities",
                            "Automated test execution capability"
                        ],
                        "common_defect_patterns": [
                            "Hard-coded dependencies preventing unit testing",
                            "Non-deterministic behavior preventing reliable testing",
                            "Insufficient test points/observations for verification",
                            "Untestable code due to tight coupling",
                            "External dependencies not mockable",
                            "Side effects making test isolation difficult",
                            "Complex initialization requirements for testing"
                        ]
                    }
                }
            },
            "portability": {
                "part": "Part 1",
                "clause": "4.8",
                "title": "Portability",
                "content": (
                    "Portability is the degree of effectiveness and efficiency with which a system can be transferred from one "
                    "environment to another. In modern development, systems often deploy across multiple environments (development, staging, "
                    "production) and platforms (on-premises, cloud, edge). Portability encompasses platform independence, containerization, "
                    "configuration management, and data migration. Poor portability locks organizations into specific vendors or environments, "
                    "increasing costs and limiting flexibility. Portability is particularly important for organizations adopting multi-cloud "
                    "strategies or transitioning between deployment models. Standards and open formats promote portability."
                ),
                "keywords": ["portability", "adaptability", "installability", "migration", "containerization", "cloud-native"],
                "sub_characteristics": {
                    "adaptability": {
                        "title": "Adaptability",
                        "definition": (
                            "The degree to which a system can be adapted for different environments such as hardware platforms, "
                            "operating systems, or database systems. Adaptability requires avoiding platform-specific dependencies, "
                            "using abstraction layers, and parameterizing environment-specific configurations. Systems designed for "
                            "adaptability use configuration files (not hard-coded values), environment variables, and dependency injection "
                            "to accommodate different deployment contexts. Adaptability enables reuse across different environments reducing "
                            "development effort."
                        ),
                        "quality_metrics": [
                            "Number of supported platforms/environments",
                            "Platform-specific code percentage",
                            "Configuration flexibility assessment",
                            "Adaptation effort required for new environment",
                            "Successful deployment to different environments"
                        ],
                        "testing_approaches": [
                            "Cross-platform testing (Windows, Linux, macOS)",
                            "Database compatibility testing",
                            "Browser compatibility testing (web apps)",
                            "Operating system version compatibility",
                            "Testing with different configurations",
                            "Container/VM environment testing"
                        ],
                        "common_defect_patterns": [
                            "Hard-coded file paths or directory separators",
                            "Platform-specific system calls without abstraction",
                            "Hard-coded configuration values",
                            "Database-specific SQL syntax",
                            "Unsafe assumptions about environment variables",
                            "Hard-coded line endings (CRLF vs LF)",
                            "Hard-coded locale settings"
                        ]
                    },
                    "installability": {
                        "title": "Installability",
                        "definition": (
                            "The degree to which a system can be successfully installed or uninstalled in a specified environment. "
                            "Installability covers both initial installation and upgrades/patches. Effective installation requires clear "
                            "documentation, minimal dependencies, automated installation scripts, and verification of successful installation. "
                            "Poor installability leads to deployment failures, operational support burden, and extended deployment time. "
                            "Modern systems use containers and deployment automation (Kubernetes, Helm) to improve installability."
                        ),
                        "quality_metrics": [
                            "Installation success rate",
                            "Installation time",
                            "Uninstallation success rate",
                            "Dependency clarity",
                            "Installation verification completeness"
                        ],
                        "testing_approaches": [
                            "Fresh installation testing on clean systems",
                            "Upgrade testing from previous versions",
                            "Downgrade testing (rollback)",
                            "Dependency verification",
                            "Installation documentation validation",
                            "Automated installation testing",
                            "Uninstallation testing"
                        ],
                        "common_defect_patterns": [
                            "Undocumented system requirements",
                            "Dependency version mismatches",
                            "Installation scripts with hard-coded paths",
                            "Incomplete or missing installation scripts",
                            "Configuration files not installed correctly",
                            "Permissions issues during installation",
                            "Installation leaving system in inconsistent state"
                        ]
                    },
                    "replaceability": {
                        "title": "Replaceability",
                        "definition": (
                            "The degree to which a system can replace another product for the same purpose. Replaceability "
                            "includes data migration capability (importing existing data), API compatibility with replaced systems, "
                            "and feature parity. Replaceability enables organizations to switch implementations with minimal disruption. "
                            "This is important for customers evaluating alternatives and for vendor independence. Replaceability concerns "
                            "data ownership and portability: customers should not become locked into proprietary formats."
                        ),
                        "quality_metrics": [
                            "Data import compatibility",
                            "API compatibility with predecessor systems",
                            "Feature parity percentage",
                            "Migration effort and time",
                            "Data loss/corruption during migration"
                        ],
                        "testing_approaches": [
                            "Data migration testing (import/export)",
                            "API compatibility testing",
                            "Feature migration testing",
                            "Data integrity verification after migration",
                            "Performance comparison with replaced system",
                            "Parallel operation testing during migration"
                        ],
                        "common_defect_patterns": [
                            "Proprietary data formats preventing import/export",
                            "Data loss during import/export",
                            "Incomplete API compatibility with replaced systems",
                            "Missing features compared to replaced system",
                            "Excessive migration effort/downtime",
                            "Feature incompatibilities after replacement",
                            "Data format corruption during migration"
                        ]
                    }
                }
            },
        },
    },
}
