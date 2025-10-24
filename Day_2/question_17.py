"""
### Q17

**Question:** Build a Pydantic model `AgentResponse` with fields for tool_calls (list of dicts), final_answer (string), reasoning_steps (list), and confidence_score (0-1 float with validator).

**Input:** `{"tool_calls": [{"name": "search", "args": {...}}], "final_answer": "The answer is...", "reasoning_steps": ["step1", "step2"], "confidence_score": 0.85}`

**Expected Output:** Validated AgentResponse object

**Usage:** Structured output parsing from LLM agents in agentic AI workflows.
"""

from pydantic import BaseModel, Field, validator
from typing import List, Dict

class AgentResponse(BaseModel):
    """Structured output from LLM agents"""
    tool_calls: List[Dict] = Field(default_factory=list)
    final_answer: str
    reasoning_steps: List[str] = Field(default_factory=list)
    confidence_score: float = Field(..., ge=0.0, le=1.0)
    
    @validator('confidence_score')
    def validate_confidence(cls, v):
        """Ensure confidence is between 0 and 1"""
        if not 0 <= v <= 1:
            raise ValueError('Confidence score must be between 0 and 1')
        return v
    
    @validator('tool_calls')
    def validate_tool_calls(cls, v):
        """Ensure tool calls have required fields"""
        for call in v:
            if 'name' not in call or 'args' not in call:
                raise ValueError('Each tool call must have name and args')
        return v

# Usage
response = AgentResponse(
    tool_calls=[{"name": "search", "args": {"query": "test"}}],
    final_answer="The answer is...",
    reasoning_steps=["step1", "step2"],
    confidence_score=0.85
)
