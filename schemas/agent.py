from pydantic import BaseModel, field_validator


class AgentResponse(BaseModel):
    answer: str
    token_count: int | None = None
    hitl_required: bool = False
    agent_name: str = ""
    confidence: float = 1.0
    error_code: str | None = None
    
    @field_validator('answer')
    @classmethod
    def validate_answer(cls, v: str) -> str:
        v = v.strip()
        if not v:
            return "I couldn't generate a response."
        return v
    
    @field_validator('confidence')
    @classmethod
    def validate_confidence(cls, v: float) -> float:
        return max(0.0, min(1.0, v))
