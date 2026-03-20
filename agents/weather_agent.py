from agno.agent import Agent
from agno.models.groq import Groq
from tools.weather_tool import WeatherTools
from agents.base_agent import BaseAgent
from utils.config import Settings
from utils.telemetry import TelemetryCollector
from schemas.agent import AgentResponse
from utils.logger import get_logger

logger = get_logger(__name__)

MODEL_ID = "openai/gpt-oss-120b"

SYSTEM_PROMPT = """You have live weather tool access. Always call it — never guess or say you lack data.

When the tool returns "City not found" or if the requested city doesn't exist:
- Say clearly: "I couldn't find [city name] in my database."
- Suggest: "Did you mean [nearest major Indian city]? Or try another city like Delhi, Mumbai, Bangalore."

For successful lookups:
- Respond in one natural paragraph: temperature, conditions, humidity, practical advice
- Be conversational and helpful
- Add one relevant tip (umbrella, jacket, sunscreen, etc.)
- Keep it under 80 words unless asked for details

Never fabricate weather data. If unsure about a city name, ask for clarification."""


class WeatherAgent(BaseAgent):
    def __init__(self, settings: Settings):
        super().__init__(settings)
        self.agent = Agent(
            id="weather-agent",
            model=Groq(id=MODEL_ID),
            name="Weather Agent",
            instructions=SYSTEM_PROMPT,
            tools=[WeatherTools(
                api_key=settings.openweather_api_key,
                base_url=settings.openweather_base_url
            )],
            markdown=True,
        )
    
    def run(self, query: str, telemetry: TelemetryCollector, history: list[dict] = []) -> AgentResponse:
        telemetry.set_agent("WeatherAgent", MODEL_ID)
        
        context = self._build_context(query, history)
        
        response = self._time_llm_call(
            lambda: self.agent.run(context, stream=False),
            telemetry
        )
        
        answer = response.content if hasattr(response, 'content') else str(response)
        token_count = self._extract_tokens(response)
        telemetry.token_count = token_count
        
        logger.info(
            f"[WeatherAgent] LLM call completed in {telemetry.llm_response_time_ms:.0f}ms | "
            f"model={MODEL_ID} | tokens={token_count or 'N/A'}"
        )
        
        return AgentResponse(
            answer=answer,
            token_count=token_count,
            agent_name="WeatherAgent"
        )
