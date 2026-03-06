"""
Domain configuration models.

Represents the user's industry domain selection and regulatory context,
which fundamentally changes the test strategy generated.
"""

from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class IndustryDomain(str, Enum):
    """Supported industry domains, each activating domain-specific standards."""
    GENERAL_SOFTWARE = "general_software"
    MEDICAL_DEVICE = "medical_device"
    AUTOMOTIVE = "automotive"
    AEROSPACE = "aerospace"
    FINANCIAL = "financial"
    EMBEDDED_IOT = "embedded_iot"
    TELECOM = "telecom"
    RAILWAY = "railway"
    NUCLEAR = "nuclear"
    GAMING_GAMBLING = "gaming_gambling"
    GOVERNMENT = "government"


class SafetyLevel(str, Enum):
    """Safety integrity levels across domains (normalized)."""
    # Generic
    NONE = "none"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"
    # Automotive (ASIL)
    ASIL_A = "asil_a"
    ASIL_B = "asil_b"
    ASIL_C = "asil_c"
    ASIL_D = "asil_d"
    # IEC 61508 (SIL)
    SIL_1 = "sil_1"
    SIL_2 = "sil_2"
    SIL_3 = "sil_3"
    SIL_4 = "sil_4"
    # Aerospace (DAL)
    DAL_A = "dal_a"
    DAL_B = "dal_b"
    DAL_C = "dal_c"
    DAL_D = "dal_d"
    DAL_E = "dal_e"


class DomainConfig(BaseModel):
    """
    User-provided domain configuration.

    This is collected in Step 2 of the workflow, before AI analysis begins.
    It activates domain-specific standards retrieval and output templates.
    """
    domain: IndustryDomain = Field(
        default=IndustryDomain.GENERAL_SOFTWARE,
        description="Primary industry domain of the product under test.",
    )
    safety_level: SafetyLevel = Field(
        default=SafetyLevel.NONE,
        description="Applicable safety integrity level (ASIL, SIL, DAL, etc.).",
    )
    regulatory_frameworks: list[str] = Field(
        default_factory=list,
        description="Specific regulatory frameworks (e.g., 'HIPAA', 'GDPR', 'PCI-DSS v4.0').",
    )
    deployment_jurisdictions: list[str] = Field(
        default_factory=list,
        description="Deployment regions affecting compliance (e.g., 'EU', 'US', 'UK').",
    )
    hardware_constraints: Optional[str] = Field(
        default=None,
        description="Hardware constraints for embedded systems (e.g., '32KB RAM, RTOS').",
    )
    deployment_environment: str = Field(
        default="cloud",
        description="Deployment type: cloud, on-premise, hybrid, edge.",
    )
    additional_context: Optional[str] = Field(
        default=None,
        description="Any additional context the user wants the AI to consider.",
    )
