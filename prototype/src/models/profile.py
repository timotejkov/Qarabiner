"""
System profile model.

Output of Agent 1 (Profiler): a structured representation of the
system under test, extracted from the raw PRD.
"""

from typing import Optional
from pydantic import BaseModel, Field


class SystemProfile(BaseModel):
    """Structured profile of the system under test, extracted by the Profiler agent."""

    # Technology stack
    backend_stack: list[str] = Field(default_factory=list, description="Backend technologies (e.g., ['Node.js', 'Express'])")
    frontend_stack: list[str] = Field(default_factory=list, description="Frontend technologies (e.g., ['React', 'Next.js'])")
    databases: list[str] = Field(default_factory=list, description="Database systems (e.g., ['PostgreSQL', 'Redis'])")
    infrastructure: list[str] = Field(default_factory=list, description="Infrastructure/deployment (e.g., ['Docker', 'AWS', 'Kubernetes'])")
    languages: list[str] = Field(default_factory=list, description="Programming languages detected")
    message_queues: list[str] = Field(default_factory=list, description="Message brokers (e.g., ['Kafka', 'RabbitMQ'])")

    # Architecture
    architecture_pattern: str = Field(default="unknown", description="Architecture pattern: monolith, microservices, serverless, hybrid")
    api_style: str = Field(default="unknown", description="API style: REST, GraphQL, gRPC, WebSocket, mixed")

    # Data & Security
    data_sensitivity: str = Field(default="internal", description="Data sensitivity: public, internal, confidential, restricted")
    identified_risks: list[str] = Field(default_factory=list, description="Key risks identified from the PRD")
    data_types_handled: list[str] = Field(default_factory=list, description="Types of data: PII, financial, medical, public")

    # Business context
    inferred_domain: Optional[str] = Field(default=None, description="Domain inferred from PRD content (may differ from user-selected)")
    user_roles: list[str] = Field(default_factory=list, description="User roles identified (e.g., admin, end-user, API consumer)")
    integration_points: list[str] = Field(default_factory=list, description="External integrations (e.g., LDAP, payment gateway, email)")

    # Scale
    expected_users: Optional[str] = Field(default=None, description="Expected user scale if mentioned")
    availability_requirements: Optional[str] = Field(default=None, description="Uptime/SLA requirements if mentioned")

    # Raw summary
    summary: str = Field(default="", description="One-paragraph summary of the system")
