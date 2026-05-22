"""
Chat routing and SSE streaming endpoint.
"""
from fastapi import APIRouter
from sse_starlette.sse import EventSourceResponse
import json
import asyncio
import re
from graph.workflow import get_graph
from schemas.chat import ChatRequest, ChatResponse
from utils.hitl_store import save_hitl_session
from langchain_core.messages import HumanMessage

router = APIRouter()


@router.post("/chat/stream")
async def chat_stream(request: ChatRequest):
    """Invoke the agent graph and stream the response as SSE tokens."""
    initial_state = {
        "messages": [HumanMessage(content=request.message)],
        "query": request.message,
    }
    config = {"configurable": {"thread_id": request.thread_id}}

    graph = await get_graph()
    final_state = await graph.ainvoke(initial_state, config)

    if request.stream:
        async def event_generator():
            answer = final_state.get("answer", "")

            # Split into words while preserving spaces so tokens
            # render correctly in the frontend without merging together
            tokens = re.findall(r'\S+|\s+', answer)
            for token in tokens:
                yield {"event": "token", "data": json.dumps(token)}
                await asyncio.sleep(0.015)

            meta_data = {
                "intent": final_state.get("intent", ""),
                "confidence": final_state.get("confidence", 0.0),
                "hitl_required": final_state.get("hitl_required", False),
                "sources": final_state.get("retrieved_docs", [])
            }
            yield {"event": "meta", "data": json.dumps(meta_data)}

            if final_state.get("hitl_required"):
                save_hitl_session(
                    request.thread_id,
                    final_state.get("hitl_question"),
                    final_state,
                )
                yield {"event": "hitl", "data": final_state.get("hitl_question")}

            yield {"event": "done", "data": "[DONE]"}

        return EventSourceResponse(event_generator())

    return ChatResponse(
        thread_id=request.thread_id,
        answer=final_state.get("answer", ""),
        intent=final_state.get("intent", ""),
        confidence=final_state.get("confidence", 0.0),
        hitl_required=final_state.get("hitl_required", False),
        hitl_question=final_state.get("hitl_question"),
    )