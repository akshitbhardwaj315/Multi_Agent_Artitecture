from pydantic import BaseModel, Field
from uuid import uuid4

class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=2000)
    thread_id: str = Field(default_factory=lambda: str(uuid4()))
    stream: bool = True

class ChatResponse(BaseModel):
    thread_id: str
    answer: str
    intent: str
    confidence: float
    hitl_required: bool
    hitl_question: str | None = None
