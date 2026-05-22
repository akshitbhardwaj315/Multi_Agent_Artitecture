# Nexus AI: Multi-Agent RAG Platform

A sophisticated, localized multi-agent system built with **LangGraph**, **FastAPI**, and **Groq**. This platform implements Hybrid Retrieval (BM25 + ChromaDB) and Human-in-the-Loop (HITL) capabilities for complex workflow orchestration.

## 🚀 Key Features

- **Multi-Agent Orchestration**: A `master_agent` routes queries to specialized sub-agents (`rag`, `weather`, `chitchat`, `planner`, `validator`).
- **Hybrid Retrieval**: Combines semantic vector search (ChromaDB) with keyword-based search (BM25) using **Reciprocal Rank Fusion (RRF)**.
- **Human-in-the-Loop (HITL)**: Persists state to SQLite and pauses execution for human clarification when ambiguity is detected.
- **Real-time Streaming**: SSE-based streaming for natural conversation flow.
- **Enterprise Design**: Premium dark-mode UI with glassmorphism aesthetics.

## 🛠️ Architecture

1. **Frontend**: Vanilla JS + CSS (Modern Aesthetics).
2. **Backend**: FastAPI (Python 3.12+).
3. **Graph**: LangGraph with SQLite checkpointing.
4. **Mock API**: Local weather service simulation.

## 📦 Setup & Installation

### 1. Prerequisites
- Python 3.12 or higher.
- A Groq API Key.

### 2. Configure Environment
Copy `.env.example` to `.env` and fill in your details:
```bash
cp .env.example .env
# Edit .env with your GROQ_API_KEY
```

### 3. Run the Application
The consolidated scripts handle venv creation, dependency installation, indexing, and starting both servers:

**For Linux/macOS:**
```bash
chmod +x run.sh
./run.sh
```

**For Windows:**
```cmd
run.bat
```

## 🧪 Testing

To verify the system independently, a comprehensive test suite is provided:
```bash
source .venv/bin/activate
python tests/query_test.py
```
This script executes 20 queries spanning various intent categories and complexity levels.

## 📂 Project Structure

- `agents/`: Localized agent logic and prompts.
- `graph/`: LangGraph workflow and state definitions.
- `retrieval/`: Hybrid search logic and indexing scripts.
- `routes/`: FastAPI endpoints for chat and HITL.
- `utils/`: Centralized configuration, logging, and retry logic.
- `frontend/`: Web interface assets.
- `mock_weather_api/`: Standalone mock service.

## 🛡️ License
MIT
