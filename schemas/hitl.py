from pydantic import BaseModel, Field

class HITLResumeRequest(BaseModel):
    thread_id: str
    user_clarification: str = Field(..., min_length=1)
