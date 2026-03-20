# Multi-Agent System

A production-quality multi-agent system built with Agno framework, featuring WeatherAgent, HackerNewsAgent, and ChitChatAgent orchestrated by a MasterAgent with retry logic, telemetry, and human-in-the-loop (HITL) support.

## Architecture

```
Frontend (Chat UI)
      │
      ▼
   app.py (FastAPI)
      │
      ▼
  MasterAgent (Router)
      │
      ├── WeatherAgent (openai/gpt-oss-120b)
      ├── HackerNewsAgent (llama-3.3-70b-versatile)
      └── ChitChatAgent (llama-3.1-8b-instant)
```

## Features

- **Smart Routing**: Keyword-based query routing to appropriate agents
- **Retry Logic**: Exponential backoff with 3 retries
- **Telemetry**: Full request/response metrics (timing, tokens, retries)
- **HITL**: Human-in-the-loop for failed requests
- **SSE Streaming**: Real-time streaming responses
- **Mock API**: Self-contained OpenWeatherMap mock server (120 Indian cities)

## Quick Start

### 1. Setup Environment

```bash
# Copy environment template
cp .env.example .env

# Add your Groq API key to .env
GROQ_API_KEY=your_key_here
```

### 2. Install Dependencies

```bash
# Activate virtual environment
.\.venv\Scripts\Activate.ps1  # Windows
source .venv/bin/activate      # Unix

# Install packages
pip install -r requirements.txt
```

### 3. Start Servers

**Option A: Using startup script (Windows)**
```bash
.\start.bat
```

**Option B: Manual startup**
```bash
# Terminal 1: Mock Weather API
uvicorn api.server:app --port 8001 --reload

# Terminal 2: Main Application
uvicorn app:app --port 8000 --reload
```

### 4. Access the UI

Open your browser to:
- **Chat UI**: http://localhost:8000/frontend/index.html
- **API Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

## Project Structure

```
Agno/
├── agents/              # Agent implementations
│   ├── base_agent.py    # Abstract base class
│   ├── weather_agent.py # Weather queries
│   ├── hackernews_agent.py
│   ├── chitchat_agent.py
│   └── master_agent.py  # Router + retry logic
├── routes/              # FastAPI routes
│   ├── chat.py          # Chat endpoints
│   ├── hitl.py          # Human-in-the-loop
│   └── health.py        # Health check
├── schemas/             # Pydantic models
│   ├── agent.py
│   ├── chat.py
│   ├── hitl.py
│   └── telemetry.py
├── utils/               # Shared utilities
│   ├── config.py        # Environment config
│   ├── logger.py        # Logging setup
│   ├── retry.py         # Retry logic
│   └── telemetry.py     # Metrics collection
├── api/                 # Mock Weather API
│   └── server.py
├── frontend/            # Chat UI
│   ├── index.html
│   ├── style.css
│   └── app.js
├── app.py               # FastAPI entry point
└── weather_tool.py      # Agno Weather toolkit
```

## API Endpoints

### Chat

**POST /chat**
```json
{
  "query": "What's the weather in Mumbai?",
  "session_id": "optional-session-id"
}
```

**GET /chat/stream**
```
?query=...&session_id=...
```
Returns SSE stream with `message` and `telemetry` events.

### HITL

**POST /hitl/respond**
```json
{
  "session_id": "...",
  "action": "confirm" | "correct",
  "correction": "optional correction text"
}
```

### Health

**GET /health**
```json
{
  "status": "ok",
  "agents": ["WeatherAgent", "HackerNewsAgent", "ChitChatAgent"],
  "mock_api": "http://localhost:8001"
}
```

## Testing

### Test Configuration
```bash
python -c "from utils.config import settings; print(settings.groq_api_key[:20])"
```

### Test Chat API
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"query": "What is the weather in Delhi?"}'
```

### Test Mock Weather API
```bash
curl "http://localhost:8001/data/2.5/weather?q=Mumbai&appid=mock_api_key_agno_2026&units=metric"
```

## Agents & Models

| Agent | Model | Use Case |
|---|---|---|
| WeatherAgent | openai/gpt-oss-120b | Weather queries |
| HackerNewsAgent | llama-3.3-70b-versatile | Tech news |
| ChitChatAgent | llama-3.1-8b-instant | General conversation |

## Telemetry Fields

- `agent_name`: Which agent handled the request
- `model_used`: LLM model ID
- `total_request_time_ms`: End-to-end request time
- `llm_response_time_ms`: LLM inference time
- `retry_count`: Number of retries attempted
- `hitl_status`: "none" | "triggered" | "resolved"
- `token_count`: Total tokens used (if available)
- `error`: Error message (if any)

## Development

### Code Standards

- Max 30 lines per function
- Max 120 lines per file
- One class per file
- All env vars via `utils/config.py`
- Use `utils/logger.py` (no `print()`)

### Adding a New Agent

1. Create `agents/new_agent.py` extending `BaseAgent`
2. Implement `run(query, telemetry)` method
3. Add to `MasterAgent.__init__()` and routing logic
4. Update frontend badge colors in `style.css`

## Mock API

The mock Weather API includes:
- 120 Indian cities
- Deterministic weather generation
- `/data/2.5/weather` - Current weather
- `/data/2.5/forecast` - 3-hour forecast
- `/data/2.5/uvi` - UV index
- `/data/2.5/onecall` - Complete weather data
- `/api/cities` - List of all cities

## Troubleshooting

**Import errors**: Make sure virtual environment is activated
**API key errors**: Check `.env` file has `GROQ_API_KEY` set
**Port conflicts**: Change ports in `start.bat` or use different ports
**CORS errors**: Check frontend is accessed via same origin or through `/frontend` path

## Next Phase: RAG Agent

Phase 2 will add:
- RAGAgent with ChromaDB vector store
- Document upload and ingestion
- CRAG-style retrieval grading
- Retrieval timing in telemetry
