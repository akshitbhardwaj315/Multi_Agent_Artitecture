#!/usr/bin/env bash
set -e

# Load settings from .env if it exists
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

SERVER_HOST=${SERVER_HOST:-"0.0.0.0"}
MAIN_PORT=${MAIN_PORT:-8000}
MOCK_PORT=${MOCK_PORT:-8001}

echo "🚀 Starting Multi-Agent Architecture..."

# 1. Ensure Python 3.12+
if ! command -v python3 &> /dev/null; then
  echo "❌ Error: python3 is not installed."
  exit 1
fi

# 2. Virtual Environment Setup
if [ ! -d ".venv" ] || [ ! -f ".venv/bin/pip" ]; then
  echo "📦 Creating virtual environment..."
  rm -rf .venv
  python3 -m venv .venv
fi

# Use explicit paths to binaries within the venv to avoid PEP 668 issues
PIP=".venv/bin/pip"
PYTHON=".venv/bin/python3"
UVICORN=".venv/bin/uvicorn"

# 3. Dependency Installation
echo "📥 Installing dependencies..."
$PIP install --upgrade pip
$PIP install -r requirements.txt

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