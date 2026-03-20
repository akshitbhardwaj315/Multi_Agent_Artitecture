from agno.agent import Agent
from agno.models.groq import Groq
from agents.base_agent import BaseAgent
from utils.config import Settings
from utils.telemetry import TelemetryCollector
from schemas.agent import AgentResponse
from utils.logger import get_logger

logger = get_logger(__name__)

MODEL_ID = "llama-3.1-8b-instant"

SYSTEM_PROMPT = """You are a warm, friendly, and helpful assistant. Be conversational and natural.

Key behaviors:
- Greetings: Respond warmly. "hey wassup" → "Hey! Not much, just here to help. What's on your mind?"
- Random text: Respond playfully. "hullululu" → "Haha, I like the energy! What can I help you with?"
- Casual questions: Be friendly and brief. "how are you" → "Doing great, thanks for asking! How about you?"
- Unclear requests: Ask kindly. "I didn't quite catch that — what would you like to know?"
- Use conversation history to remember what was discussed earlier
- Keep responses under 50 words for greetings/casual chat, longer for real questions
- Match the user's vibe — casual if they're casual, helpful if they need something"""


class ChitChatAgent(BaseAgent):
    def __init__(self, settings: Settings):
        super().__init__(settings)
        self.agent = Agent(
            id="chitchat-agent",
            model=Groq(id=MODEL_ID),
            name="ChitChat Agent",
            instructions=SYSTEM_PROMPT,
            markdown=True,
        )
    
    def run(self, query: str, telemetry: TelemetryCollector, history: list[dict] = []) -> AgentResponse:
        telemetry.set_agent("ChitChatAgent", MODEL_ID)
        
        context = self._build_context(query, history)
        
        response = self._time_llm_call(
            lambda: self.agent.run(context, stream=False),
            telemetry
        )
        
        answer = response.content if hasattr(response, 'content') else str(response)
        token_count = self._extract_tokens(response)
        telemetry.token_count = token_count
        
        logger.info(
            f"[ChitChatAgent] LLM call completed in {telemetry.llm_response_time_ms:.0f}ms | "
            f"model={MODEL_ID} | tokens={token_count or 'N/A'}"
        )
        
        return AgentResponse(
            answer=answer,
            token_count=token_count,
            agent_name="ChitChatAgent"
        )
