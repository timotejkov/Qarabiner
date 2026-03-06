"""Domain-adaptive output templates for the Architect agent."""

from src.models.domain_config import IndustryDomain

BASE_TEMPLATE = """\
# 1. System Under Test (SUT) Profile
(Architecture, technology stack, data flow, user roles, data sensitivity classification)

# 2. Strategic Risk Assessment
(Technical risks, business risks, risk prioritization matrix)

# 3. Test Scope & Quality Objectives
## 3.1 In-Scope Features
## 3.2 Out-of-Scope Elements
## 3.3 ISO 25010 Quality Attribute Mapping
(For each relevant quality characteristic: measurable acceptance criteria)

# 4. Test Strategy & Methodology
## 4.1 Test Levels (ISO 29119-2)
(Component, Integration, System, Acceptance — with specific targets for each)
## 4.2 Functional Test Approach
(Specific module/endpoint targets, ISTQB test design techniques to apply)
## 4.3 Non-Functional Requirements Strategy
(Performance, reliability, usability — with measurable thresholds)
## 4.4 Security & Compliance Strategy
(OWASP verification, domain-specific compliance requirements)

# 5. Entry & Exit Criteria
(Measurable, testable conditions for starting and stopping testing)

# 6. Environment & Tooling Requirements
(Test environments, test data, tools, infrastructure)

# 7. Risk Mitigation & Contingency
(What to do if key risks materialize, fallback strategies)
"""

MEDICAL_EXTENSION = """
# 8. Verification & Validation Evidence Matrix (IEC 62304)
(Requirements ↔ Test Cases ↔ Results traceability)

# 9. Risk Classification Justification
(IEC 62304 Class A/B/C determination with rationale)

# 10. Regulatory Submission Artifacts
(FDA CSA assurance activities, documentation requirements)
"""

AUTOMOTIVE_EXTENSION = """
# 8. ASIL Decomposition & Coverage Metrics (ISO 26262)
(ASIL-specific coverage requirements: statement, branch, MC/DC)

# 9. ASPICE Process Compliance Map
(SWE.4, SWE.5, SWE.6 process area alignment)

# 10. Safety Analysis Integration
(SOTIF considerations, fault injection strategy)
"""

FINANCIAL_EXTENSION = """
# 8. Audit Trail & Logging Requirements
(Transaction logging, regulatory audit readiness)

# 9. PCI-DSS Control Mapping
(PCI-DSS v4.0 requirements mapped to test activities)
"""

# Map domains to their template extensions
DOMAIN_EXTENSIONS: dict[IndustryDomain, str] = {
    IndustryDomain.MEDICAL_DEVICE: MEDICAL_EXTENSION,
    IndustryDomain.AUTOMOTIVE: AUTOMOTIVE_EXTENSION,
    IndustryDomain.FINANCIAL: FINANCIAL_EXTENSION,
}


def get_output_template(domain: IndustryDomain) -> str:
    """
    Get the full output template for a given domain.

    Combines the base template with any domain-specific extensions.
    """
    template = BASE_TEMPLATE
    extension = DOMAIN_EXTENSIONS.get(domain, "")
    if extension:
        template += "\n" + extension
    return template
