"""
Strategy output models.

The pipeline produces either clarifying questions (gap detected)
or a full test strategy (sufficient context).
"""

from enum import Enum
from typing import Optional, Union
from pydantic import BaseModel, Field


class ClarifyingQuestion(BaseModel):
    """A single clarifying question tied to a specific standard gap."""
    standard: str = Field(description="Standard requiring the missing info (e.g., 'ISO 25010 - Performance Efficiency')")
    question: str = Field(description="The specific question for the Product Owner")
    example_answer: Optional[str] = Field(default=None, description="Example of a sufficient answer")


class QuestionsResponse(BaseModel):
    """Returned when the Architect detects gaps in the PRD."""
    response_type: str = Field(default="questions", description="Discriminator: always 'questions'")
    questions: list[ClarifyingQuestion] = Field(description="Clarifying questions to resolve gaps")
    gaps_summary: str = Field(default="", description="Brief summary of what information is missing")


class StrategyResponse(BaseModel):
    """Returned when the Architect generates a full test strategy."""
    response_type: str = Field(default="strategy", description="Discriminator: always 'strategy'")
    strategy_markdown: str = Field(description="Full test strategy in Markdown format")
    standards_cited: list[str] = Field(default_factory=list, description="List of standards cited in the strategy")
    domain_sections_included: list[str] = Field(default_factory=list, description="Domain-specific sections added to output")


class ValidationStatus(str, Enum):
    """Critic agent validation result."""
    PASSED = "passed"
    FAILED = "failed"


class ValidationIssue(BaseModel):
    """A single issue found by the Critic agent."""
    category: str = Field(description="Issue type: citation_invalid, hallucination, missing_section, risk_mismatch")
    description: str = Field(description="What the issue is")
    location: Optional[str] = Field(default=None, description="Where in the strategy the issue was found")
    severity: str = Field(default="medium", description="low, medium, high")


class ValidationResult(BaseModel):
    """Output of the Critic agent."""
    status: ValidationStatus
    issues: list[ValidationIssue] = Field(default_factory=list)
    citation_accuracy: float = Field(default=1.0, description="Fraction of citations verified (0.0-1.0)")
    structural_completeness: float = Field(default=1.0, description="Fraction of required sections present (0.0-1.0)")
    summary: str = Field(default="", description="Validation summary")


# Union type for pipeline output
PipelineResult = Union[QuestionsResponse, StrategyResponse]
