from agents.base_agent import BaseAgent
from utils.config import Settings
from utils.telemetry import TelemetryCollector
from schemas.agent import AgentResponse

ERROR_MESSAGES = {
    "tool_call_failed": "Hmm, I had a hiccup fetching that data. Try asking again — it usually works on the second go.",
    "rate_limited": "I'm getting a lot of requests right now. Give it a second and try again.",
    "no_results": "Couldn't find anything on that. Try rephrasing or being more specific.",
    "city_not_found": "That city isn't in my weather database. Try a nearby major city.",
    "context_lost": "I lost track of our conversation context. Could you repeat your question with a bit more detail?",
    "model_unavailable": "The AI model I usually use is temporarily unavailable. Falling back to basics — please try again.",
    "timeout": "That took too long and I had to stop. Try a simpler version of your question.",
    "validation_error": "Something about that request didn't look right. Could you rephrase it?",
    "unknown": "Something went wrong on my end. It's not you — please try again.",
}


class ErrorAgent(BaseAgent):
    def run(self, query: str, telemetry: TelemetryCollector, history: list[dict] = [], error_code: str = "unknown") -> AgentResponse:
        msg = ERROR_MESSAGES.get(error_code, ERROR_MESSAGES["unknown"])
        telemetry.set_agent("ErrorAgent", "none")
        return AgentResponse(
            answer=msg,
            agent_name="ErrorAgent",
            error_code=error_code,
            confidence=0.0
        )
