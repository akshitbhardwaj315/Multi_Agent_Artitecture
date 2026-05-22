"""
HITL resume endpoint logic.
"""
from fastapi import APIRouter, HTTPException
from sse_starlette.sse import EventSourceResponse
import json
import asyncio
from graph.workflow import get_graph
from schemas.hitl import HITLResumeRequest
from utils.hitl_store import load_hitl_session, delete_hitl_session, save_hitl_session
from langchain_core.messages import HumanMessage

router = APIRouter()

@router.post("/hitl/resume")
async def hitl_resume(request: HITLResumeRequest):
    session = load_hitl_session(request.thread_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found or expired")
        
    state = session
    
    state["query"] = request.user_clarification
    state["hitl_required"] = False
    state["messages"] = [HumanMessage(content=request.user_clarification)]
    
    config = {"configurable": {"thread_id": request.thread_id}}
    
    graph = await get_graph()
    final_state = await graph.ainvoke(state, config)
    
    delete_hitl_session(request.thread_id)
    
    async def event_generator():
        answer = final_state.get("answer", "")
        # Split into words while preserving spaces so tokens
        # render correctly in the frontend without merging together
        import re
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
                final_state
            )
            yield {"event": "hitl", "data": final_state.get("hitl_question")}
            
        yield {"event": "done", "data": "[DONE]"}
        
    return EventSourceResponse(event_generator())
