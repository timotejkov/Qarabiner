"""
ISO/IEC 25010:2023 — Software Product Quality Model.

Defines the quality characteristics and sub-characteristics that the
Architect agent uses for non-functional requirements mapping.
"""

STANDARD_ID = "ISO/IEC 25010:2023"

SECTIONS: dict[str, dict] = {
    "25010:2023": {
        "title": "Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model",
        "sections": {
            "functional_suitability": {
                "title": "Functional Suitability",
                "content": (
                    "Degree to which a product provides functions that meet stated and implied needs. "
                    "Sub-characteristics: Functional Completeness (degree to which the set of functions "
                    "covers all specified tasks and user objectives), Functional Correctness (degree to "
                    "which a product provides correct results with the needed degree of precision), "
                    "Functional Appropriateness (degree to which functions facilitate the accomplishment "
                    "of specified tasks and objectives)."
                ),
                "keywords": ["functional", "completeness", "correctness", "appropriateness"],
            },
            "performance_efficiency": {
                "title": "Performance Efficiency",
                "content": (
                    "Performance relative to the amount of resources used under stated conditions. "
                    "Sub-characteristics: Time Behaviour (response times, processing times, throughput), "
                    "Resource Utilization (CPU, memory, disk, network bandwidth usage), "
                    "Capacity (maximum limits of a product parameter — concurrent users, transactions/sec, "
                    "data volume). Testing requires defined load profiles and acceptance thresholds."
                ),
                "keywords": ["performance", "latency", "throughput", "capacity", "load", "resource"],
            },
            "compatibility": {
                "title": "Compatibility",
                "content": (
                    "Degree to which a product can exchange information with other products and/or "
                    "perform its required functions while sharing the same hardware or software environment. "
                    "Sub-characteristics: Co-existence (can operate alongside other products without detrimental impact), "
                    "Interoperability (can exchange and use information with other systems)."
                ),
                "keywords": ["compatibility", "interoperability", "co-existence", "integration"],
            },
            "usability": {
                "title": "Usability",
                "content": (
                    "Degree to which a product can be used by specified users to achieve specified goals "
                    "with effectiveness, efficiency, and satisfaction. Sub-characteristics: "
                    "Appropriateness Recognizability, Learnability, Operability, User Error Protection, "
                    "User Interface Aesthetics, Accessibility (usable by people with the widest range of "
                    "characteristics and capabilities — see WCAG 2.2)."
                ),
                "keywords": ["usability", "learnability", "accessibility", "UX", "user interface"],
            },
            "reliability": {
                "title": "Reliability",
                "content": (
                    "Degree to which a system performs specified functions under specified conditions "
                    "for a specified period of time. Sub-characteristics: Maturity (meets needs for "
                    "reliability under normal operation), Availability (operational and accessible when "
                    "required — measured as uptime percentage, e.g., 99.9%), Fault Tolerance (operates "
                    "as intended despite hardware or software faults), Recoverability (can recover data "
                    "and re-establish desired state after interruption or failure — RTO/RPO metrics)."
                ),
                "keywords": ["reliability", "availability", "fault tolerance", "recovery", "uptime", "RTO", "RPO"],
            },
            "security": {
                "title": "Security",
                "content": (
                    "Degree to which a product protects information and data so that persons or other "
                    "products have the degree of data access appropriate to their types and levels of "
                    "authorization. Sub-characteristics: Confidentiality (data accessible only to authorized), "
                    "Integrity (prevents unauthorized modification), Non-repudiation (actions can be proven "
                    "to have taken place), Accountability (actions traceable to the entity), "
                    "Authenticity (identity of subject/resource can be proved)."
                ),
                "keywords": ["security", "confidentiality", "integrity", "authentication", "authorization", "OWASP"],
            },
            "maintainability": {
                "title": "Maintainability",
                "content": (
                    "Degree of effectiveness and efficiency with which a product can be modified. "
                    "Sub-characteristics: Modularity (changes to one component have minimal impact on others), "
                    "Reusability (asset can be used in more than one system), Analysability (impact of intended "
                    "change can be assessed), Modifiability (can be modified without introducing defects), "
                    "Testability (test criteria can be established and tests performed to determine met)."
                ),
                "keywords": ["maintainability", "modularity", "testability", "modifiability"],
            },
            "portability": {
                "title": "Portability",
                "content": (
                    "Degree of effectiveness and efficiency with which a system can be transferred from "
                    "one environment to another. Sub-characteristics: Adaptability (can be adapted for "
                    "different environments), Installability (can be installed/uninstalled successfully), "
                    "Replaceability (can replace another product for the same purpose)."
                ),
                "keywords": ["portability", "adaptability", "installability", "migration"],
            },
        },
    },
}
