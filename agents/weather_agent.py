"""
Weather agent — extracts city from query, calls mock weather API,
returns a rich natural language answer.
"""
import httpx
from graph.state import AgentState
from utils.config import settings
from mock_weather_api.data import WEATHER_DATA

async def get_weather_data(city: str) -> dict:
    """Hit the mock weather API and return raw data or an error dict."""
    async with httpx.AsyncClient(timeout=5.0) as client:
        try:
            response = await client.get(
                f"{settings.mock_weather_url}/weather",
                params={"city": city},
            )
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                return {"_error": 404}
        except httpx.RequestError:
            return {"_error": "network"}
    return {"_error": "unknown"}


def _extract_city(query: str) -> str:
    """Pull city name from natural language query using string matching against known locations."""
    q_lower = query.lower()
    
    # Try exact match from our known database
    for loc in WEATHER_DATA.keys():
        if loc in q_lower:
            return loc
            
    # Fallback heuristic: Try to find a word after 'in' or 'for' without regex
    words = [w.strip("?,.! ") for w in q_lower.split()]
    for preposition in ["in", "for", "at"]:
        if preposition in words:
            try:
                idx = words.index(preposition)
                if idx + 1 < len(words):
                    candidate = words[idx + 1]
                    if candidate not in ["today", "now", "currently", "tomorrow"]:
                        return candidate
            except ValueError:
                pass
                
    return "mumbai"  # default


def _build_answer(city: str, data: dict) -> str:
    """Format weather data into a very friendly, talkative natural language response mimicking OpenWeatherMap schemas."""
    # Parse OpenWeatherMap schema
    weather_desc = data["weather"][0]["description"] if "weather" in data and len(data["weather"]) > 0 else "unknown"
    main_weather = data["weather"][0]["main"] if "weather" in data and len(data["weather"]) > 0 else "Unknown"
    
    # Using correct format from real API simulation
    temp_k = data["main"]["temp"]
    temp_c = round(temp_k - 273.15, 1)
    temp_f = round((temp_c * 9/5) + 32, 1)
    
    humidity = data["main"]["humidity"]
    wind_mps = data["wind"]["speed"]
    wind_kph = round(wind_mps * 3.6, 1)
    
    country = data["sys"].get("country", "IN")
    real_name = data.get("name", city.title())
    
    # Pick a casual, talky opening line based on condition
    cond_lower = main_weather.lower()
    
    if "clear" in cond_lower:
        opener = f"It's a beautiful, clear day out there in {real_name}, {country}! Perfect weather for a stroll."
    elif "rain" in cond_lower or "drizzle" in cond_lower:
        opener = f"Looks like you'll need an umbrella in {real_name}, {country}. It's currently experiencing {weather_desc}."
    elif "cloud" in cond_lower or "overcast" in cond_lower:
        opener = f"It's quite cloudy over in {real_name}, {country} right now. A bit overcast, but generally mild!"
    elif "thunder" in cond_lower:
        opener = f"Stay indoors! There's a thunderstorm brewing in {real_name}, {country}. Be safe!"
    elif "smoke" in cond_lower or "haze" in cond_lower:
        opener = f"The air quality might not be the best today in {real_name}, {country} due to {weather_desc}. Consider wearing a mask if you're sensitive!"
    else:
        opener = f"Here is the weather update for {real_name}, {country}. Expect {weather_desc}."

    return (
        f"{opener}\n\n"
        f"🌡 **Temperature:** {temp_c}°C (which is about {temp_f}°F)\n"
        f"🌤 **Current Condition:** {weather_desc.capitalize()}\n"
        f"💧 **Humidity:** {humidity}% — {'Pretty muggy! 😅' if humidity > 70 else 'Quite comfortable.'}\n"
        f"💨 **Wind Speed:** {wind_kph} km/h"
    )


async def weather_agent(state: AgentState) -> dict:
    """Extract city, fetch weather from mock API, return rich answer."""
    query = state.get("query", "")
    city = _extract_city(query)
    data = await get_weather_data(city)

    if "_error" in data:
        if data["_error"] == 404:
            return {
                "answer": "",
                "hitl_required": True,
                "hitl_question": f"I couldn't find a location matching '{city.title()}'. Could you clarify the exact state or major city in India you meant?",
                "confidence": 0.0
            }
        else:
            answer = (
                "Oops! The weather service seems to be having some technical difficulties and is offline right now. "
                "Please ensure the mock weather API is running. You can check the configuration in your settings."
            )
            return {"answer": answer, "hitl_required": False, "confidence": 1.0}
    else:
        answer = _build_answer(city, data)

    return {"answer": answer, "hitl_required": False, "confidence": 1.0}