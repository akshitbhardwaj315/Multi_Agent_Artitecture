from pydantic import BaseModel
from schemas.telemetry import TelemetryData


class HITLRequest(BaseModel):
    session_id: str
    action: str
    correction: str | None = None


class HITLResponse(BaseModel):
    answer: str
    telemetry: TelemetryData
