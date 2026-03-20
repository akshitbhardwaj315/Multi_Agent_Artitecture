from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
from routes import chat, hitl, health
from utils.logger import get_logger
import uvicorn

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("🚀 Multi-Agent System started")
    yield


app = FastAPI(title="Multi-Agent System API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router, tags=["Chat"])
app.include_router(hitl.router, tags=["HITL"])
app.include_router(health.router, tags=["Health"])

app.mount("/frontend", StaticFiles(directory="frontend", html=True), name="frontend")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
