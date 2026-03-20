from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.hackernews import HackerNewsTools
from agents.base_agent import BaseAgent
from utils.config import Settings
from utils.telemetry import TelemetryCollector
from schemas.agent import AgentResponse
from utils.logger import get_logger

logger = get_logger(__name__)

MODEL_ID = "llama-3.3-70b-versatile"

SYSTEM_PROMPT = """You have live HackerNews tool access. Fetch once, answer from those results only.
Never fabricate stories. For headline requests: numbered list, title + one-line context.
Apply topic filters from the fetched results. Be direct, no filler phrases.
One tool call maximum per request."""


class HackerNewsAgent(BaseAgent):
    def __init__(self, settings: Settings):
        super().__init__(settings)
        self.agent = Agent(
            id="hackernews-agent",
            model=Groq(id=MODEL_ID),
            name="HackerNews Agent",
            tools=[HackerNewsTools()],
            instructions=SYSTEM_PROMPT,
            markdown=True,
        )
    
    def run(self, query: str, telemetry: TelemetryCollector, history: list[dict] = []) -> AgentResponse:
        telemetry.set_agent("HackerNewsAgent", MODEL_ID)
        
        context = self._build_context(query, history)
        
        response = self._time_llm_call(
            lambda: self.agent.run(context, stream=False),
            telemetry
        )
        
        answer = response.content if hasattr(response, 'content') else str(response)
        token_count = self._extract_tokens(response)
        telemetry.token_count = token_count
        
        logger.info(
            f"[HackerNewsAgent] LLM call completed in {telemetry.llm_response_time_ms:.0f}ms | "
            f"model={MODEL_ID} | tokens={token_count or 'N/A'}"
        )
        
        return AgentResponse(
            answer=answer,
            token_count=token_count,
            agent_name="HackerNewsAgent"
        )
