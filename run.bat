@echo off
setlocal

echo 🚀 Starting Multi-Agent Architecture for Windows...

:: 1. Check for Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Error: python is not installed or not in PATH.
    exit /b 1
)

:: 2. Virtual Environment Setup
if not exist .venv\Scripts\pip.exe (
    echo 📦 Creating virtual environment...
    python -m venv .venv
)

:: Define paths
set PIP=.venv\Scripts\pip.exe
set PYTHON=.venv\Scripts\python.exe
set UVICORN=.venv\Scripts\uvicorn.exe

:: 3. Dependency Installation
echo 📥 Installing dependencies...
%PIP% install --upgrade pip
%PIP% install -r requirements.txt

:: 4. Data Initialization
if not exist data mkdir data
if not exist data\bm25_index.pkl (
    echo 🔍 Seeding RAG indices...
    %PYTHON% retrieval\indexer.py
)

:: 5. Read ports from .env if it exists (very basic parser)
set MOCK_PORT=8001
set MAIN_PORT=8000
set SERVER_HOST=0.0.0.0

if exist .env (
    for /f "tokens=1,2 delims==" %%a in (.env) do (
        if "%%a"=="MOCK_PORT" set MOCK_PORT=%%b
        if "%%a"=="MAIN_PORT" set MAIN_PORT=%%b
        if "%%a"=="SERVER_HOST" set SERVER_HOST=%%b
    )
)

:: 6. Start Mock Weather API in a new background window
echo ☁️ Starting Mock Weather API on port %MOCK_PORT%...
start /B "Mock Weather API" %UVICORN% mock_weather_api.server:app --host %SERVER_HOST% --port %MOCK_PORT% --log-level warning

:: 7. Start Main App in current window
echo ✨ Starting Main App on http://localhost:%MAIN_PORT%
%UVICORN% app:app --host %SERVER_HOST% --port %MAIN_PORT% --reload

pause
