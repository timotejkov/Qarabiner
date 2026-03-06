"""
FastAPI application — Qarabiner REST API.

Provides endpoints for strategy generation, question answering, and export.
OpenAPI documentation available at /docs.
"""

import json
import logging
import traceback
from typing import Any

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from src.agents.orchestrator import PipelineOrchestrator
from src.models.domain_config import DomainConfig, IndustryDomain, SafetyLevel
from src.models.session import Session, SessionStore
from src.models.strategy import QuestionsResponse, StrategyResponse
from src.parsers.text_parser import parse_text
from src.standards.library import StandardsLibrary

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("server.log", mode="w"),
    ],
)
logger = logging.getLogger(__name__)

# --- Application setup ---

app = FastAPI(
    title="Qarabiner",
    description=(
        "AI-powered test strategy engine. Analyzes PRDs and generates "
        "standards-compliant test strategies using a 4-agent pipeline "
        "(Profiler → Researcher → Architect → Critic)."
    ),
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# NOTE: CORS is intentionally permissive for this PoC to allow easy local testing from any origin.
# In production, this MUST be restricted to specific allowed origins (e.g., your frontend domain).
# Example for production:
#   allow_origins=["https://example.com"],
#   allow_methods=["GET", "POST"],
#   allow_headers=["Content-Type"],
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# NOTE: Request size limits are handled by Starlette's default middleware (max 16MB).
# The Pydantic model's min_length constraint on prd_text also provides validation.

# Shared state
library = StandardsLibrary()
pipeline = PipelineOrchestrator(library)
sessions = SessionStore()


# --- Request/Response models ---

class GenerateRequest(BaseModel):
    """Request to generate a test strategy from a PRD.

    Only prd_text is required. All other fields are optional — the Profiler
    agent infers domain, safety level, deployment environment, and regulatory
    frameworks directly from the PRD content. User-provided values act as
    overrides.
    """
    prd_text: str = Field(
        ...,
        min_length=10,
        description="The Product Requirements Document, system description text, or a GitHub URL.",
        json_schema_extra={"example": "A Node.js REST API backend with React frontend handling user authentication..."},
    )
    domain: IndustryDomain | None = Field(
        default=None,
        description="Optional industry domain override. If omitted, inferred from PRD.",
    )
    safety_level: SafetyLevel | None = Field(
        default=None,
        description="Optional safety level override. If omitted, inferred from PRD.",
    )
    regulatory_frameworks: list[str] = Field(
        default_factory=list,
        description="Optional regulatory frameworks override (e.g., ['HIPAA', 'GDPR']).",
    )
    deployment_jurisdictions: list[str] = Field(
        default_factory=list,
        description="Deployment regions (e.g., ['EU', 'US']).",
    )
    hardware_constraints: str | None = Field(
        default=None,
        description="Hardware constraints for embedded systems.",
    )
    deployment_environment: str | None = Field(
        default=None,
        description="Optional deployment type override: cloud, on-premise, hybrid, edge.",
    )


class AnswerRequest(BaseModel):
    """Request to answer clarifying questions and regenerate strategy."""
    session_id: str = Field(..., description="Session ID from the generate response.")
    answers: dict[str, str] = Field(
        ...,
        description="Map of question text → answer text.",
        json_schema_extra={"example": {"What is the expected peak concurrent user count?": "500 users"}},
    )


class GenerateResponse(BaseModel):
    """Response from strategy generation."""
    session_id: str = Field(description="Session ID for follow-up requests.")
    status: str = Field(description="Pipeline status: questions, strategy, error.")
    questions: list[dict[str, Any]] | None = Field(default=None, description="Clarifying questions (if gaps detected).")
    strategy_markdown: str | None = Field(default=None, description="Generated test strategy in Markdown.")
    validation: dict[str, Any] | None = Field(default=None, description="Critic validation result.")
    profile_summary: str | None = Field(default=None, description="Brief system profile summary.")


class ExportResponse(BaseModel):
    """Exported strategy."""
    markdown: str = Field(description="Strategy in Markdown format.")


class StatsResponse(BaseModel):
    """Standards library statistics."""
    total_sections: int
    standard_ids: list[str]


# --- Endpoints ---

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def serve_frontend() -> HTMLResponse:
    """Serve the single-page frontend."""
    try:
        with open("frontend/index.html", "r") as f:
            return HTMLResponse(content=f.read())
    except FileNotFoundError:
        logger.error("Frontend HTML file not found at frontend/index.html")
        raise HTTPException(status_code=500, detail="Frontend not available")


@app.get("/api/health", tags=["System"])
async def health_check() -> dict[str, str]:
    """Check if the API is running and the standards library is loaded."""
    return {
        "status": "healthy",
        "standards_loaded": str(library.total_sections),
        "version": "0.1.0",
    }


@app.get("/api/standards/stats", response_model=StatsResponse, tags=["Standards"])
async def standards_stats() -> StatsResponse:
    """Get statistics about the loaded standards library."""
    return StatsResponse(
        total_sections=library.total_sections,
        standard_ids=library.get_all_standard_ids(),
    )


@app.get("/api/domains", tags=["Configuration"])
async def list_domains() -> list[dict[str, str]]:
    """List all supported industry domains."""
    return [{"value": d.value, "label": d.value.replace("_", " ").title()} for d in IndustryDomain]


@app.post("/api/strategy/generate", response_model=GenerateResponse, tags=["Strategy"])
async def generate_strategy(request: GenerateRequest) -> GenerateResponse:
    """
    Generate a test strategy from a PRD.

    The pipeline runs: Profiler → Researcher → Architect → Critic.
    Returns either clarifying questions (if gaps detected) or a full strategy.
    """
    prd_text = parse_text(request.prd_text)

    # Build DomainConfig only if user provided explicit overrides
    has_user_config = (
        request.domain is not None
        or request.safety_level is not None
        or request.deployment_environment is not None
        or len(request.regulatory_frameworks) > 0
    )

    if has_user_config:
        domain_config = DomainConfig(
            domain=request.domain or IndustryDomain.GENERAL_SOFTWARE,
            safety_level=request.safety_level or SafetyLevel.NONE,
            regulatory_frameworks=request.regulatory_frameworks,
            deployment_jurisdictions=request.deployment_jurisdictions,
            hardware_constraints=request.hardware_constraints,
            deployment_environment=request.deployment_environment or "cloud",
        )
    else:
        # Let the Profiler infer everything from the PRD
        domain_config = None

    session = sessions.create(prd_text, domain_config or DomainConfig())

    try:
        result, validation, profile, standards = pipeline.generate(
            prd_text=prd_text,
            domain_config=domain_config,
        )

        session.profile = profile
        session.result = result
        session.validation = validation

        if isinstance(result, QuestionsResponse):
            session.status = "questions"
            sessions.update(session)
            return GenerateResponse(
                session_id=session.id,
                status="questions",
                questions=[q.model_dump() for q in result.questions],
                profile_summary=profile.summary if profile else None,
            )
        else:
            session.status = "complete"
            sessions.update(session)
            return GenerateResponse(
                session_id=session.id,
                status="strategy",
                strategy_markdown=result.strategy_markdown,
                validation=validation.model_dump() if validation else None,
                profile_summary=profile.summary if profile else None,
            )

    except Exception as e:
        session.status = "error"
        session.error_message = str(e)
        sessions.update(session)
        logger.error(f"Pipeline error: {traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=f"Pipeline error: {str(e)}")


@app.post("/api/strategy/answer", response_model=GenerateResponse, tags=["Strategy"])
async def answer_questions(request: AnswerRequest) -> GenerateResponse:
    """
    Answer clarifying questions and regenerate the strategy.

    Requires a session_id from a previous generate call that returned questions.
    """
    session = sessions.get(request.session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    session.answered_questions.update(request.answers)

    try:
        result, validation, profile, standards = pipeline.generate(
            prd_text=session.prd_text,
            domain_config=session.domain_config,
            answered_questions=session.answered_questions,
        )

        session.profile = profile
        session.result = result
        session.validation = validation

        if isinstance(result, QuestionsResponse):
            session.status = "questions"
            sessions.update(session)
            return GenerateResponse(
                session_id=session.id,
                status="questions",
                questions=[q.model_dump() for q in result.questions],
                profile_summary=profile.summary if profile else None,
            )
        else:
            session.status = "complete"
            sessions.update(session)
            return GenerateResponse(
                session_id=session.id,
                status="strategy",
                strategy_markdown=result.strategy_markdown,
                validation=validation.model_dump() if validation else None,
                profile_summary=profile.summary if profile else None,
            )

    except Exception as e:
        session.status = "error"
        session.error_message = str(e)
        sessions.update(session)
        logger.error(f"Pipeline error: {traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=f"Pipeline error: {str(e)}")


@app.get("/api/strategy/export/{session_id}", response_model=ExportResponse, tags=["Export"])
async def export_strategy(session_id: str) -> ExportResponse:
    """Export a generated strategy as Markdown."""
    session = sessions.get(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    if not session.result or not isinstance(session.result, StrategyResponse):
        raise HTTPException(status_code=400, detail="No strategy available for export")

    return ExportResponse(markdown=session.result.strategy_markdown)
