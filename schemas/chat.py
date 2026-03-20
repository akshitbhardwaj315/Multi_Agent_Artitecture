import uuid
from pydantic import BaseModel, field_validator
from schemas.telemetry import TelemetryData


class ChatRequest(BaseModel):
    query: str
    session_id: str = ""
    
    @field_validator('query')
    @classmethod
    def validate_query(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("Query cannot be empty")
        if len(v) > 500:
            raise ValueError("Query too long (max 500 characters)")
        return v
    
    @field_validator('session_id')
    @classmethod
    def validate_session_id(cls, v: str) -> str:
        if not v:
            return str(uuid.uuid4())
        try:
            uuid.UUID(v)
            return v
        except ValueError:
            return str(uuid.uuid4())


class ChatResponse(BaseModel):
    answer: str
    agent_name: str
    telemetry: TelemetryData
