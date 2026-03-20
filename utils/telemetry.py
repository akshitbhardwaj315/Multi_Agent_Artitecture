import time


class TelemetryCollector:
    def __init__(self):
        self.agent_name: str | None = None
        self.model_used: str | None = None
        self.total_request_time_ms: float = 0.0
        self.llm_response_time_ms: float = 0.0
        self.retry_count: int = 0
        self.hitl_status: str = "none"
        self.error: str | None = None
        self.token_count: int | None = None
        self._start_time: float | None = None
    
    def start(self):
        self._start_time = time.perf_counter()
    
    def stop(self):
        if self._start_time:
            elapsed = time.perf_counter() - self._start_time
            self.total_request_time_ms = round(elapsed * 1000, 2)
    
    def set_llm_time(self, ms: float):
        self.llm_response_time_ms = round(ms, 2)
    
    def set_agent(self, name: str, model: str):
        self.agent_name = name
        self.model_used = model
    
    def add_retry(self):
        self.retry_count += 1
    
    def trigger_hitl(self):
        self.hitl_status = "triggered"
    
    def resolve_hitl(self):
        self.hitl_status = "resolved"
    
    def to_dict(self) -> dict:
        return {
            "agent_name": self.agent_name,
            "model_used": self.model_used,
            "total_request_time_ms": self.total_request_time_ms,
            "llm_response_time_ms": self.llm_response_time_ms,
            "retry_count": self.retry_count,
            "hitl_status": self.hitl_status,
            "error": self.error,
            "token_count": self.token_count,
        }
