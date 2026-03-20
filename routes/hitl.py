from fastapi import APIRouter, HTTPException
from schemas.hitl import HITLRequest, HITLResponse
from schemas.telemetry import TelemetryData
from utils.config import settings
from utils.telemetry import TelemetryCollector
from utils.logger import get_logger
from agents.master_agent import MasterAgent

logger = get_logger(__name__)
router = APIRouter()
master_agent = MasterAgent(settings)

_hitl_sessions: dict[str, dict] = {}


@router.post("/hitl/respond", response_model=HITLResponse)
async def hitl_respond(request: HITLRequest):
    if request.session_id not in _hitl_sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    
    session = _hitl_sessions[request.session_id]
    original_query = session.get("query", "")
    
    telemetry = TelemetryCollector()
    telemetry.start()
    telemetry.resolve_hitl()
    
    if request.action == "correct" and request.correction:
        corrected_query = f"User correction: {request.correction}. Original query: {original_query}"
        response = master_agent.run(corrected_query, telemetry)
    else:
        response = master_agent.run(original_query, telemetry)
    
    telemetry.stop()
    
    del _hitl_sessions[request.session_id]
    
    return HITLResponse(
        answer=response.answer,
        telemetry=TelemetryData(**telemetry.to_dict())
    )
