from time import time
from fastapi import APIRouter
from utils.config import settings
from utils.telemetry import TelemetryCollector
from utils.logger import get_logger
from schemas.chat import ChatRequest, ChatResponse
from schemas.telemetry import TelemetryData
from agents.master_agent import MasterAgent
from sse_starlette.sse import EventSourceResponse
import json

logger = get_logger(__name__)
router = APIRouter()
master_agent = MasterAgent(settings)

_sessions: dict[str, list[dict]] = {}
_news_cache: dict[str, dict] = {}

FOLLOWUP_PATTERNS = [
    "2nd", "3rd", "4th", "5th", "second", "third", "fourth", "fifth",
    "next", "another", "what about", "and the", "show more"
]


def _is_news_followup(query: str, sid: str) -> bool:
    q = query.lower()
    cached = _news_cache.get(sid)
    if not cached or (time() - cached["ts"]) > settings.news_cache_ttl:
        return False
    return any(p in q for p in FOLLOWUP_PATTERNS)


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    telemetry = TelemetryCollector()
    telemetry.start()
    
    logger.info(f"[chat] Request received | query=\"{request.query[:50]}...\" | session={request.session_id}")
    
    # Cache disabled - was returning same answer for all followup queries
    # TODO: Implement per-story cache if needed
    # if _is_news_followup(request.query, request.session_id):
    #     cached = _news_cache[request.session_id]
    #     telemetry.set_agent("CacheHit", "none")
    #     telemetry.stop()
    #     logger.info(f"[chat] Cache hit | session={request.session_id} | total={telemetry.total_request_time_ms:.0f}ms")
    #     return ChatResponse(
    #         answer=cached["stories"],
    #         agent_name="CacheHit",
    #         telemetry=TelemetryData(**telemetry.to_dict())
    #     )
    
    history = _sessions.get(request.session_id, [])
    history.append({"role": "user", "content": request.query})
    
    response = master_agent.run(request.query, telemetry, history)
    
    history.append({"role": "assistant", "content": response.answer})
    _sessions[request.session_id] = history[-settings.max_history:]
    
    # Cache news responses
    if telemetry.agent_name == "HackerNewsAgent":
        _news_cache[request.session_id] = {"stories": response.answer, "ts": time()}
    
    telemetry.stop()
    
    logger.info(
        f"[chat] Request complete | agent={telemetry.agent_name} | "
        f"total={telemetry.total_request_time_ms:.0f}ms | "
        f"llm={telemetry.llm_response_time_ms:.0f}ms | retries={telemetry.retry_count}"
    )
    
    return ChatResponse(
        answer=response.answer,
        agent_name=telemetry.agent_name or "Unknown",
        telemetry=TelemetryData(**telemetry.to_dict())
    )


@router.get("/chat/stream")
async def chat_stream(query: str, session_id: str = ""):
    async def event_generator():
        telemetry = TelemetryCollector()
        telemetry.start()
        
        try:
            logger.info(f"[chat/stream] SSE request | query=\"{query[:50]}...\" | session={session_id}")
            
            # Cache disabled - was returning same answer for all followup queries
            # if _is_news_followup(query, session_id):
            #     cached = _news_cache[session_id]
            #     telemetry.set_agent("CacheHit", "none")
            #     for char in cached["stories"]:
            #         yield {"event": "message", "data": char}
            #     telemetry.stop()
            #     yield {
            #         "event": "telemetry",
            #         "data": json.dumps({
            #             "agent_name": "CacheHit",
            #             "telemetry": telemetry.to_dict(),
            #             "hitl_required": False
            #         })
            #     }
            #     return
            
            history = _sessions.get(session_id, [])
            history.append({"role": "user", "content": query})
            
            response = master_agent.run(query, telemetry, history)
            
            history.append({"role": "assistant", "content": response.answer})
            _sessions[session_id] = history[-settings.max_history:]
            
            # Cache news responses
            if telemetry.agent_name == "HackerNewsAgent":
                _news_cache[session_id] = {"stories": response.answer, "ts": time()}
            
            for char in response.answer:
                yield {"event": "message", "data": char}
            
            telemetry.stop()
            
            yield {
                "event": "telemetry",
                "data": json.dumps({
                    "agent_name": telemetry.agent_name,
                    "telemetry": telemetry.to_dict(),
                    "hitl_required": response.hitl_required
                })
            }
            
        except Exception as e:
            logger.error(f"[chat/stream] Error | error={str(e)}")
            yield {"event": "error", "data": str(e)}
    
    return EventSourceResponse(event_generator())
