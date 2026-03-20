#!/bin/bash
echo "Starting Mock Weather API on :8001..."
uvicorn api.server:app --port 8001 --reload &
MOCK_PID=$!
echo "Starting Main App on :8000..."
uvicorn app:app --port 8000 --reload
kill $MOCK_PID
