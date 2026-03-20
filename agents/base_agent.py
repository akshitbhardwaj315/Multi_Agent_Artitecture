from abc import ABC, abstractmethod
from typing import Callable, Any
import time
from utils.config import Settings
from utils.telemetry import TelemetryCollector
from schemas.agent import AgentResponse


class BaseAgent(ABC):
    def __init__(self, settings: Settings):
        self.settings = settings
    
    @abstractmethod
    def run(self, query: str, telemetry: TelemetryCollector, history: list[dict] = []) -> AgentResponse:
        pass
    
    def _time_llm_call(self, fn: Callable, telemetry: TelemetryCollector) -> Any:
        start = time.perf_counter()
        result = fn()
        elapsed_ms = (time.perf_counter() - start) * 1000
        telemetry.set_llm_time(elapsed_ms)
        return result
    
    def _build_context(self, query: str, history: list[dict]) -> str:
        if not history:
            return query
        recent = history[-6:]
        lines = [f"{'User' if m['role']=='user' else 'Assistant'}: {m['content']}" 
                 for m in recent]
        return "CONVERSATION SO FAR:\n" + "\n".join(lines) + "\n\nNEW QUERY: " + query
    
    def _extract_tokens(self, response) -> int | None:
        try:
            if hasattr(response, 'metrics') and isinstance(response.metrics, dict):
                it = response.metrics.get('input_tokens', 0)
                ot = response.metrics.get('output_tokens', 0)
                it = it[0] if isinstance(it, list) else it
                ot = ot[0] if isinstance(ot, list) else ot
                if (it + ot) > 0:
                    return it + ot
            if hasattr(response, 'usage') and response.usage:
                return getattr(response.usage, 'total_tokens', None)
            if hasattr(response, 'messages') and response.messages:
                for msg in reversed(response.messages):
                    m = getattr(msg, 'metrics', None)
                    if m:
                        it = m.get('input_tokens', 0)
                        ot = m.get('output_tokens', 0)
                        it = it[0] if isinstance(it, list) else it
                        ot = ot[0] if isinstance(ot, list) else ot
                        if (it + ot) > 0:
                            return it + ot
        except Exception:
            pass
        return None
