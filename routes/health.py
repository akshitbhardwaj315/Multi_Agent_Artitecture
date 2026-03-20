from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health():
    return {
        "status": "ok",
        "agents": ["WeatherAgent", "HackerNewsAgent", "ChitChatAgent"],
        "mock_api": "http://localhost:8001"
    }
