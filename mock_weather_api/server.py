"""
Standalone FastAPI for testing weather agent logic locally.
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from mock_weather_api.data import WEATHER_DATA

app = FastAPI(title="Mock Weather API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/weather")
def get_weather(city: str):
    """Return weather data or 404."""
    city_key = city.lower().strip()
    if city_key in WEATHER_DATA:
        return WEATHER_DATA[city_key]
    raise HTTPException(status_code=404, detail="City not found")

@app.get("/health")
def health():
    """Health check endpoint."""
    return {"status": "ok", "service": "mock-weather"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
