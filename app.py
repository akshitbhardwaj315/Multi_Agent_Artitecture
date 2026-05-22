"""
Main FastAPI entrypoint for the localized multi-agent stack.
"""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os

from routes.chat import router as chat_router
from routes.hitl import router as hitl_router
from utils.config import settings

from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Ensure directories exist
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(settings.bm25_index_path):
        print("⚠  RAG indices not found. Run indexing script if needed.")
    yield
    # Shutdown: Clean up resources if any

app = FastAPI(
    title="Multi-Agent RAG", 
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── API routes
app.include_router(chat_router)
app.include_router(hitl_router)

@app.get("/health")
def health_check():
    return {"status": "ok", "environment": settings.environment}

# ── Static files LAST
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")