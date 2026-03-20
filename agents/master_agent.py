from agno.agent import Agent
from agno.models.groq import Groq
from utils.config import Settings
from utils.telemetry import TelemetryCollector
from utils.retry import retry_with_backoff
from utils.logger import get_logger
from schemas.agent import AgentResponse
from agents.weather_agent import WeatherAgent
from agents.hackernews_agent import HackerNewsAgent
from agents.chitchat_agent import ChitChatAgent
from agents.error_agent import ErrorAgent

logger = get_logger(__name__)

ROUTER_MODEL = "llama-3.1-8b-instant"
WEATHER_KEYWORDS = ["weather", "temperature", "forecast", "rain", "humidity", "wind", "uv", "aqi"]
HACKERNEWS_KEYWORDS = ["hackernews", "hacker news", "hn", "tech news"]


class MasterAgent:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.weather_agent = WeatherAgent(settings)
        self.hackernews_agent = HackerNewsAgent(settings)
        self.chitchat_agent = ChitChatAgent(settings)
        self.error_agent = ErrorAgent(settings)
        self.router_llm = Agent(
            model=Groq(id=ROUTER_MODEL),
            instructions=(
                'You are a query router. Classify the user\'s query into exactly one of these categories:\n'
                '"weather" — anything about weather, temperature, climate, forecast, rain, UV index\n'
                '"hackernews" — anything about tech news, AI news, programming news, startup news, '
                'developer news, trending tech, latest news, top stories, headlines\n'
                '"chitchat" — everything else (greetings, general questions, personal questions, time, opinions)\n'
                'Reply with ONLY one word: weather, hackernews, or chitchat. No explanation.'
            )
        )
    
    def _route(self, query: str, history: list[dict] = []) -> str:
        query_lower = query.lower()
        
        if any(kw in query_lower for kw in WEATHER_KEYWORDS):
            logger.info(f"[MasterAgent] Layer1 hit → weather")
            return "weather"
        
        if any(kw in query_lower for kw in HACKERNEWS_KEYWORDS):
            logger.info(f"[MasterAgent] Layer1 hit → hackernews")
            return "hackernews"
        
        try:
            # Build context for router with recent history
            context = query
            if history:
                recent = history[-4:]  # Last 4 messages
                context_lines = [f"{'User' if m['role']=='user' else 'Assistant'}: {m['content'][:100]}" 
                                for m in recent]
                context = "Recent conversation:\n" + "\n".join(context_lines) + "\n\nCurrent query: " + query
            
            response = self.router_llm.run(context, stream=False)
            classification = response.content.strip().lower() if hasattr(response, 'content') else str(response).strip().lower()
            
            if "weather" in classification:
                result = "weather"
            elif "hackernews" in classification:
                result = "hackernews"
            else:
                result = "chitchat"
            
            logger.info(f'[MasterAgent] Layer1 miss → LLM classified "{query[:40]}..." → {result}')
            return result
        except Exception as e:
            logger.warning(f"[MasterAgent] LLM router failed, defaulting to chitchat | error={str(e)}")
            return "chitchat"
    
    def _classify_error(self, e: Exception) -> str:
        msg = str(e).lower()
        if "tool call" in msg or "tool_use_failed" in msg:
            return "tool_call_failed"
        if "rate limit" in msg or "429" in msg:
            return "rate_limited"
        if "timeout" in msg or "timed out" in msg:
            return "timeout"
        if "city" in msg or "not found" in msg:
            return "city_not_found"
        if "model" in msg or "unavailable" in msg:
            return "model_unavailable"
        return "unknown"
    
    def run(self, query: str, telemetry: TelemetryCollector, history: list[dict] = []) -> AgentResponse:
        agent_name = self._route(query, history)
        
        agent_map = {
            "weather": self.weather_agent,
            "hackernews": self.hackernews_agent,
            "chitchat": self.chitchat_agent,
        }
        
        selected_agent = agent_map[agent_name]
        
        try:
            response = retry_with_backoff(
                fn=lambda: selected_agent.run(query, telemetry, history),
                telemetry=telemetry,
                max_retries=self.settings.max_retries
            )
            return response
        except Exception as e:
            logger.error(f"[MasterAgent] All retries exhausted | error={str(e)}")
            error_code = self._classify_error(e)
            telemetry.trigger_hitl()
            telemetry.error = str(e)
            return self.error_agent.run(query, telemetry, history, error_code)
