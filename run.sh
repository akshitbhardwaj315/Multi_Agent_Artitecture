#!/usr/bin/env bash
set -e

# Load settings from .env if it exists
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

SERVER_HOST=${SERVER_HOST:-"0.0.0.0"}
MAIN_PORT=${MAIN_PORT:-8000}
MOCK_PORT=${MOCK_PORT:-8001}

echo "🚀 Starting Multi-Agent Architecture (UV + Python 3.12)..."

# 1. Install uv if missing (checks local bin too)
export PATH="$HOME/.local/bin:$PATH"
if ! command -v uv &> /dev/null; then
  echo "📥 uv not found. Installing uv..."
  curl -LsSf https://astral.sh/uv/install.sh | sh
fi

# 2. Virtual Environment Setup with UV
if [ ! -d ".venv" ]; then
  echo "📦 Creating virtual environment (Python 3.12)..."
  uv venv --python 3.12
fi

# Use explicit paths to binaries inside the venv
PYTHON=".venv/bin/python3"
UVICORN=".venv/bin/uvicorn"

# 3. Dependency Installation with UV
echo "📥 Installing dependencies with uv..."
uv pip install -r requirements.txt

# 4. Data Initialization
mkdir -p data
if [ ! -f "data/bm25_index.pkl" ]; then
  echo "🔍 Seeding RAG indices..."
  $PYTHON retrieval/indexer.py
fi

# 5. Start Mock Weather API
echo "☁️ Starting Mock Weather API on port $MOCK_PORT..."
$UVICORN mock_weather_api.server:app --host $SERVER_HOST --port $MOCK_PORT --log-level warning &
WEATHER_PID=$!

# Cleanup on exit
cleanup() {
  echo "🛑 Stopping services..."
  kill $WEATHER_PID 2>/dev/null || true
}
trap cleanup EXIT INT TERM

# 6. Start Main App
echo "✨ Starting Main App on http://localhost:$MAIN_PORT"
$UVICORN app:app --host $SERVER_HOST --port $MAIN_PORT --reload