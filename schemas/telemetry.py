from pydantic import BaseModel, field_validator, computed_field, ConfigDict


class TelemetryData(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    
    agent_name: str | None = None
    model_used: str | None = None
    total_request_time_ms: float = 0.0
    llm_response_time_ms: float = 0.0
    retry_count: int = 0
    hitl_status: str = "none"
    error: str | None = None
    token_count: int | None = None
    
    @field_validator('hitl_status')
    @classmethod
    def validate_hitl_status(cls, v: str) -> str:
        allowed = ["none", "triggered", "resolved"]
        if v not in allowed:
            return "none"
        return v
    
    @field_validator('retry_count')
    @classmethod
    def validate_retry_count(cls, v: int) -> int:
        return max(0, min(10, v))
    
    @computed_field
    @property
    def performance_tier(self) -> str:
        ms = self.total_request_time_ms
        if ms < 1000:
            return "fast"
        elif ms < 3000:
            return "normal"
        else:
            return "slow"
