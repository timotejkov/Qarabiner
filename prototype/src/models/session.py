"""
In-memory session management.

For the prototype, sessions are stored in a dict. Production would use
PostgreSQL or Redis.
"""

import uuid
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

from src.models.domain_config import DomainConfig
from src.models.profile import SystemProfile
from src.models.strategy import PipelineResult, ValidationResult


class Session(BaseModel):
    """Tracks state across the multi-step workflow for one user project."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    created_at: datetime = Field(default_factory=datetime.utcnow)

    # Step 1: Input
    prd_text: str = Field(default="")

    # Step 2: Domain config
    domain_config: DomainConfig = Field(default_factory=DomainConfig)

    # Step 3: Profile (from Profiler agent)
    profile: Optional[SystemProfile] = None

    # Step 4: Q&A answers
    answered_questions: dict[str, str] = Field(default_factory=dict)

    # Step 5: Generated strategy
    result: Optional[PipelineResult] = None
    validation: Optional[ValidationResult] = None

    # Pipeline state
    status: str = Field(default="created", description="created, profiling, researching, generating, validating, complete, error")
    error_message: Optional[str] = None


class SessionStore:
    """In-memory session storage. Thread-safe for prototype use."""

    def __init__(self) -> None:
        self._sessions: dict[str, Session] = {}

    def create(self, prd_text: str, domain_config: DomainConfig) -> Session:
        """Create a new session."""
        session = Session(prd_text=prd_text, domain_config=domain_config)
        self._sessions[session.id] = session
        return session

    def get(self, session_id: str) -> Optional[Session]:
        """Retrieve a session by ID."""
        return self._sessions.get(session_id)

    def update(self, session: Session) -> None:
        """Update an existing session."""
        self._sessions[session.id] = session

    def list_all(self) -> list[Session]:
        """List all sessions (for dashboard)."""
        return list(self._sessions.values())
