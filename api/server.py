import hashlib
import time
import math
import random
from fastapi import FastAPI, Query, HTTPException, Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI(title="OpenWeather Mock API")


# ─────────────────────────── LOGGING MIDDLEWARE ──────────────────────────────
class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start = time.perf_counter()
        response = await call_next(request)
        duration_ms = (time.perf_counter() - start) * 1000
        
        response.headers["X-Response-Time-Ms"] = f"{duration_ms:.2f}"
        
        # Mask API key in logs
        query_params = dict(request.query_params)
        if "appid" in query_params:
            query_params["appid"] = "***"
        
        query_str = "&".join(f"{k}={v}" for k, v in query_params.items())
        print(
            f"[MOCK-API] {request.method} {request.url.path}"
            f"{'?' + query_str if query_str else ''} → {response.status_code} in {duration_ms:.1f}ms"
        )
        
        return response


app.add_middleware(LoggingMiddleware)

# ─────────────────────────── API KEY MANAGEMENT ───────────────────────────
VALID_API_KEYS = {
    "mock_api_key_agno_2026",
    "d5f4e3c2b1a09876f5e4d3c2b1a09876",
}

def _verify_key(appid: str | None):
    if not appid or appid not in VALID_API_KEYS:
        raise HTTPException(
            status_code=401,
            detail={
                "cod": 401,
                "message": "Invalid API key. Please see https://openweathermap.org/faq#error401 for more info.",
            },
        )

# ─────────────────────────── CITY DATABASE ────────────────────────────────
# Each entry: (name, state, lat, lon, temp_base_C, humidity_base, description_pool_index)
# temp_base is the avg temp around which we oscillate; pool_index picks weather type
CITIES: dict[str, dict] = {}

_raw = [
    # ── Metros ──
    ("Mumbai", "Maharashtra", 19.076, 72.8777, 30, 78, 0),
    ("Delhi", "Delhi", 28.7041, 77.1025, 25, 55, 1),
    ("Bengaluru", "Karnataka", 12.9716, 77.5946, 27, 65, 2),
    ("Hyderabad", "Telangana", 17.385, 78.4867, 31, 58, 1),
    ("Chennai", "Tamil Nadu", 13.0827, 80.2707, 33, 72, 0),
    ("Kolkata", "West Bengal", 22.5726, 88.3639, 30, 75, 0),
    ("Ahmedabad", "Gujarat", 23.0225, 72.5714, 33, 40, 3),
    ("Pune", "Maharashtra", 18.5204, 73.8567, 28, 60, 2),
    # ── North India ──
    ("Jaipur", "Rajasthan", 26.9124, 75.7873, 30, 38, 3),
    ("Lucknow", "Uttar Pradesh", 26.8467, 80.9462, 28, 55, 1),
    ("Kanpur", "Uttar Pradesh", 26.4499, 80.3319, 28, 52, 1),
    ("Varanasi", "Uttar Pradesh", 25.3176, 82.9739, 29, 58, 1),
    ("Agra", "Uttar Pradesh", 27.1767, 78.0081, 29, 48, 3),
    ("Noida", "Uttar Pradesh", 28.5355, 77.391, 26, 54, 1),
    ("Ghaziabad", "Uttar Pradesh", 28.6692, 77.4538, 26, 53, 1),
    ("Meerut", "Uttar Pradesh", 28.9845, 77.7064, 27, 55, 1),
    ("Chandigarh", "Chandigarh", 30.7333, 76.7794, 25, 50, 2),
    ("Amritsar", "Punjab", 31.634, 74.8723, 25, 52, 1),
    ("Ludhiana", "Punjab", 30.901, 75.8573, 26, 50, 1),
    ("Shimla", "Himachal Pradesh", 31.1048, 77.1734, 15, 65, 2),
    ("Dehradun", "Uttarakhand", 30.3165, 78.0322, 23, 62, 2),
    ("Haridwar", "Uttarakhand", 29.9457, 78.1642, 24, 60, 2),
    ("Jammu", "Jammu & Kashmir", 32.7266, 74.857, 22, 55, 1),
    ("Srinagar", "Jammu & Kashmir", 34.0837, 74.7973, 14, 68, 2),
    # ── West India ──
    ("Surat", "Gujarat", 21.1702, 72.8311, 32, 62, 0),
    ("Vadodara", "Gujarat", 22.3072, 73.1812, 32, 50, 3),
    ("Rajkot", "Gujarat", 22.3039, 70.8022, 31, 45, 3),
    ("Nagpur", "Maharashtra", 21.1458, 79.0882, 31, 48, 3),
    ("Nashik", "Maharashtra", 19.9975, 73.7898, 28, 55, 2),
    ("Aurangabad", "Maharashtra", 19.8762, 75.3433, 30, 50, 1),
    ("Thane", "Maharashtra", 19.2183, 72.9781, 30, 76, 0),
    ("Navi Mumbai", "Maharashtra", 19.033, 73.0297, 30, 77, 0),
    ("Goa", "Goa", 15.2993, 74.124, 31, 75, 0),
    ("Udaipur", "Rajasthan", 24.5854, 73.7125, 29, 40, 3),
    ("Jodhpur", "Rajasthan", 26.2389, 73.0243, 32, 30, 3),
    ("Bikaner", "Rajasthan", 28.0229, 73.3119, 33, 25, 3),
    ("Kota", "Rajasthan", 25.2138, 75.8648, 30, 42, 3),
    # ── South India ──
    ("Coimbatore", "Tamil Nadu", 11.0168, 76.9558, 29, 60, 2),
    ("Madurai", "Tamil Nadu", 9.9252, 78.1198, 32, 65, 1),
    ("Tiruchirappalli", "Tamil Nadu", 10.7905, 78.7047, 31, 63, 1),
    ("Kochi", "Kerala", 9.9312, 76.2673, 29, 80, 0),
    ("Thiruvananthapuram", "Kerala", 8.5241, 76.9366, 30, 82, 0),
    ("Kozhikode", "Kerala", 11.2588, 75.7804, 29, 79, 0),
    ("Mysuru", "Karnataka", 12.2958, 76.6394, 27, 62, 2),
    ("Mangaluru", "Karnataka", 12.9141, 74.856, 29, 75, 0),
    ("Hubli", "Karnataka", 15.3647, 75.124, 28, 55, 1),
    ("Visakhapatnam", "Andhra Pradesh", 17.6868, 83.2185, 30, 72, 0),
    ("Vijayawada", "Andhra Pradesh", 16.5062, 80.648, 32, 68, 1),
    ("Tirupati", "Andhra Pradesh", 13.6288, 79.4192, 31, 60, 1),
    # ── East & Northeast India ──
    ("Patna", "Bihar", 25.6093, 85.1376, 29, 60, 1),
    ("Ranchi", "Jharkhand", 23.3441, 85.3096, 26, 58, 2),
    ("Jamshedpur", "Jharkhand", 22.8046, 86.2029, 27, 60, 2),
    ("Bhubaneswar", "Odisha", 20.2961, 85.8245, 30, 70, 0),
    ("Cuttack", "Odisha", 20.4625, 85.883, 30, 68, 1),
    ("Guwahati", "Assam", 26.1445, 91.7362, 25, 75, 0),
    ("Imphal", "Manipur", 24.817, 93.9368, 22, 72, 2),
    ("Shillong", "Meghalaya", 25.5788, 91.8933, 18, 78, 2),
    ("Agartala", "Tripura", 23.8315, 91.2868, 26, 76, 0),
    ("Gangtok", "Sikkim", 27.3389, 88.6065, 14, 80, 2),
    ("Itanagar", "Arunachal Pradesh", 27.0844, 93.6053, 20, 75, 2),
    ("Kohima", "Nagaland", 25.6751, 94.1086, 19, 74, 2),
    ("Aizawl", "Mizoram", 23.7271, 92.7176, 21, 76, 2),
    # ── Central India ──
    ("Bhopal", "Madhya Pradesh", 23.2599, 77.4126, 29, 50, 1),
    ("Indore", "Madhya Pradesh", 22.7196, 75.8577, 29, 48, 1),
    ("Gwalior", "Madhya Pradesh", 26.2183, 78.1828, 29, 45, 3),
    ("Jabalpur", "Madhya Pradesh", 23.1815, 79.9864, 28, 52, 1),
    ("Raipur", "Chhattisgarh", 21.2514, 81.6296, 30, 55, 1),
    ("Bilaspur", "Chhattisgarh", 22.0797, 82.1391, 29, 54, 1),
    # ── Union Territories & Others ──
    ("Pondicherry", "Puducherry", 11.9416, 79.8083, 31, 75, 0),
    ("Port Blair", "Andaman & Nicobar", 11.6234, 92.7265, 28, 85, 0),
    ("Leh", "Ladakh", 34.1526, 77.5771, 5, 30, 2),
    ("Panaji", "Goa", 15.4909, 73.8278, 31, 74, 0),
    ("Silvassa", "Dadra & Nagar Haveli", 20.2766, 73.0169, 30, 70, 0),
    ("Daman", "Daman & Diu", 20.397, 72.8328, 30, 72, 0),
    ("Kavaratti", "Lakshadweep", 10.5593, 72.6358, 29, 80, 0),
    ("Dharamshala", "Himachal Pradesh", 32.219, 76.3234, 18, 60, 2),
    ("Rishikesh", "Uttarakhand", 30.0869, 78.2676, 24, 58, 2),
    ("Allahabad", "Uttar Pradesh", 25.4358, 81.8463, 29, 55, 1),
    ("Mathura", "Uttar Pradesh", 27.4924, 77.6737, 28, 50, 1),
    ("Aligarh", "Uttar Pradesh", 27.8974, 78.088, 27, 52, 1),
    ("Bareilly", "Uttar Pradesh", 28.367, 79.4304, 27, 55, 1),
    ("Moradabad", "Uttar Pradesh", 28.8386, 78.7733, 27, 56, 1),
    ("Gorakhpur", "Uttar Pradesh", 26.7606, 83.3732, 28, 58, 1),
    ("Faridabad", "Haryana", 28.4089, 77.3178, 27, 52, 1),
    ("Gurugram", "Haryana", 28.4595, 77.0266, 27, 50, 1),
    ("Karnal", "Haryana", 29.6857, 76.9905, 26, 55, 1),
    ("Rohtak", "Haryana", 28.8955, 76.6066, 27, 48, 1),
    ("Panipat", "Haryana", 29.3909, 76.9635, 27, 52, 1),
    ("Jalandhar", "Punjab", 31.326, 75.5762, 25, 55, 1),
    ("Patiala", "Punjab", 30.34, 76.3869, 26, 53, 1),
    ("Bathinda", "Punjab", 30.211, 74.9455, 27, 42, 3),
    ("Siliguri", "West Bengal", 26.7271, 88.3953, 24, 72, 0),
    ("Durgapur", "West Bengal", 23.5204, 87.3119, 28, 65, 1),
    ("Asansol", "West Bengal", 23.6739, 86.9524, 28, 62, 1),
    ("Howrah", "West Bengal", 22.5958, 88.2636, 30, 74, 0),
    ("Nellore", "Andhra Pradesh", 14.4426, 79.9865, 32, 68, 1),
    ("Warangal", "Telangana", 17.9784, 79.5941, 30, 55, 1),
    ("Karimnagar", "Telangana", 18.4386, 79.1288, 30, 52, 1),
    ("Nizamabad", "Telangana", 18.6725, 78.0941, 30, 50, 1),
    ("Thrissur", "Kerala", 10.5276, 76.2144, 29, 78, 0),
    ("Kollam", "Kerala", 8.8932, 76.6141, 29, 80, 0),
    ("Salem", "Tamil Nadu", 11.6643, 78.146, 30, 58, 1),
    ("Erode", "Tamil Nadu", 11.341, 77.7172, 30, 56, 1),
    ("Tirunelveli", "Tamil Nadu", 8.7139, 77.7567, 31, 65, 1),
    ("Bellary", "Karnataka", 15.1394, 76.9214, 31, 45, 3),
    ("Belgaum", "Karnataka", 15.8497, 74.4977, 27, 60, 2),
    ("Gulbarga", "Karnataka", 17.3297, 76.8343, 31, 48, 1),
    ("Dhanbad", "Jharkhand", 23.7957, 86.4304, 27, 60, 2),
    ("Bokaro", "Jharkhand", 23.6693, 86.1511, 27, 58, 2),
    ("Muzaffarpur", "Bihar", 26.1209, 85.3647, 28, 62, 1),
    ("Gaya", "Bihar", 24.7955, 84.9994, 29, 55, 1),
    ("Bhagalpur", "Bihar", 25.2425, 86.9842, 28, 60, 1),
    ("Sambalpur", "Odisha", 21.4669, 83.9812, 29, 60, 1),
    ("Rourkela", "Odisha", 22.2604, 84.8536, 28, 58, 2),
    ("Dibrugarh", "Assam", 27.4728, 94.912, 24, 78, 0),
    ("Jorhat", "Assam", 26.7509, 94.2037, 24, 76, 0),
    ("Ujjain", "Madhya Pradesh", 23.1765, 75.7885, 29, 45, 1),
    ("Sagar", "Madhya Pradesh", 23.8388, 78.7378, 28, 50, 1),
    ("Ajmer", "Rajasthan", 26.4499, 74.6399, 30, 38, 3),
    ("Alwar", "Rajasthan", 27.5529, 76.6346, 29, 42, 3),
    ("Bhilwara", "Rajasthan", 25.3407, 74.6313, 30, 38, 3),
    ("Jhansi", "Uttar Pradesh", 25.4484, 78.5685, 29, 45, 1),
    ("Firozabad", "Uttar Pradesh", 27.1591, 78.3957, 28, 50, 1),
]

WEATHER_POOLS = [
    [
        {"id": 500, "main": "Rain", "description": "light rain", "icon": "10d"},
        {"id": 802, "main": "Clouds", "description": "scattered clouds", "icon": "03d"},
        {"id": 801, "main": "Clouds", "description": "few clouds", "icon": "02d"},
        {"id": 300, "main": "Drizzle", "description": "light intensity drizzle", "icon": "09d"},
    ],
    [
        {"id": 721, "main": "Haze", "description": "haze", "icon": "50d"},
        {"id": 800, "main": "Clear", "description": "clear sky", "icon": "01d"},
        {"id": 801, "main": "Clouds", "description": "few clouds", "icon": "02d"},
        {"id": 701, "main": "Mist", "description": "mist", "icon": "50d"},
    ],
    [
        {"id": 802, "main": "Clouds", "description": "scattered clouds", "icon": "03d"},
        {"id": 800, "main": "Clear", "description": "clear sky", "icon": "01d"},
        {"id": 803, "main": "Clouds", "description": "broken clouds", "icon": "04d"},
        {"id": 500, "main": "Rain", "description": "light rain", "icon": "10d"},
    ],
    [
        {"id": 800, "main": "Clear", "description": "clear sky", "icon": "01d"},
        {"id": 801, "main": "Clouds", "description": "few clouds", "icon": "02d"},
        {"id": 721, "main": "Haze", "description": "haze", "icon": "50d"},
    ],
]

def _build_city_db():
    for name, state, lat, lon, temp_base, hum_base, pool_idx in _raw:
        key = name.lower()
        CITIES[key] = {
            "name": name,
            "state": state,
            "country": "IN",
            "lat": lat,
            "lon": lon,
            "temp_base": temp_base,
            "humidity_base": hum_base,
            "pool_idx": pool_idx,
        }
        alt = f"{name.lower()}, {state.lower()}"
        CITIES[alt] = CITIES[key]
        full = f"{name.lower()}, {state.lower()}, in"
        CITIES[full] = CITIES[key]

_build_city_db()

# ─────────────────────────── WEATHER GENERATION ───────────────────────────

def _deterministic_seed(city_name: str) -> int:
    day_stamp = int(time.time()) // 3600
    return int(hashlib.md5(f"{city_name}{day_stamp}".encode()).hexdigest()[:8], 16)

def _generate_weather(city: dict) -> dict:
    seed = _deterministic_seed(city["name"])
    rng = random.Random(seed)

    temp_c = city["temp_base"] + rng.uniform(-3, 3)
    feels_like_c = temp_c + rng.uniform(-2, 2)
    temp_min_c = temp_c - rng.uniform(1, 4)
    temp_max_c = temp_c + rng.uniform(1, 4)

    humidity = max(10, min(100, city["humidity_base"] + rng.randint(-10, 10)))
    pressure = rng.randint(1005, 1020)
    visibility = rng.randint(4000, 10000)
    wind_speed = round(rng.uniform(1.5, 8.5), 2)
    wind_deg = rng.randint(0, 360)
    clouds = rng.randint(5, 95)

    pool = WEATHER_POOLS[city["pool_idx"]]
    weather_cond = rng.choice(pool)

    def c_to_k(c):
        return round(c + 273.15, 2)

    now = int(time.time())
    sunrise_offset = rng.randint(5 * 3600 + 30 * 60, 6 * 3600 + 15 * 60)
    sunset_offset = sunrise_offset + rng.randint(11 * 3600, 12 * 3600 + 30 * 60)

    return {
        "coord": {"lon": city["lon"], "lat": city["lat"]},
        "weather": [weather_cond],
        "base": "stations",
        "main": {
            "temp": c_to_k(temp_c),
            "feels_like": c_to_k(feels_like_c),
            "temp_min": c_to_k(temp_min_c),
            "temp_max": c_to_k(temp_max_c),
            "pressure": pressure,
            "humidity": humidity,
            "sea_level": pressure + rng.randint(-2, 2),
            "grnd_level": pressure - rng.randint(5, 30),
        },
        "visibility": visibility,
        "wind": {"speed": wind_speed, "deg": wind_deg, "gust": round(wind_speed + rng.uniform(1, 4), 2)},
        "clouds": {"all": clouds},
        "dt": now,
        "sys": {
            "type": 2,
            "id": rng.randint(2000000, 9999999),
            "country": "IN",
            "sunrise": now - (now % 86400) + sunrise_offset,
            "sunset": now - (now % 86400) + sunset_offset,
        },
        "timezone": 19800,
        "id": int(hashlib.md5(city["name"].encode()).hexdigest()[:7], 16),
        "name": city["name"],
        "cod": 200,
    }

def _convert_units(data: dict, units: str) -> dict:
    if units == "metric":
        data["main"]["temp"] = round(data["main"]["temp"] - 273.15, 2)
        data["main"]["feels_like"] = round(data["main"]["feels_like"] - 273.15, 2)
        data["main"]["temp_min"] = round(data["main"]["temp_min"] - 273.15, 2)
        data["main"]["temp_max"] = round(data["main"]["temp_max"] - 273.15, 2)
    elif units == "imperial":
        for k in ("temp", "feels_like", "temp_min", "temp_max"):
            data["main"][k] = round((data["main"][k] - 273.15) * 9 / 5 + 32, 2)
        data["wind"]["speed"] = round(data["wind"]["speed"] * 2.237, 2)
    return data

# ─────────────────────────── API ENDPOINTS ────────────────────────────────

def _find_city(q: str | None = None, lat: float | None = None, lon: float | None = None) -> dict | None:
    if q:
        lookup = q.strip().lower()
        city = CITIES.get(lookup)
        if not city:
            parts = [p.strip() for p in lookup.split(",")]
            city = CITIES.get(parts[0])
        return city
    if lat is not None and lon is not None:
        best, best_dist = None, float("inf")
        for c in {id(v): v for v in CITIES.values()}.values():
            d = math.hypot(c["lat"] - lat, c["lon"] - lon)
            if d < best_dist:
                best_dist, best = d, c
        if best_dist < 2.0:
            return best
    return None


# ── Geocoding (used by agno's OpenWeatherTools before every call) ─────────

@app.get("/geo/1.0/direct")
def geocode(
    q: str = Query(..., description="City name"),
    limit: int = Query(1),
    appid: str | None = Query(None),
):
    _verify_key(appid)
    city = _find_city(q=q)
    if not city:
        return JSONResponse(content=[])
    return JSONResponse(content=[{
        "name": city["name"],
        "local_names": {"en": city["name"]},
        "lat": city["lat"],
        "lon": city["lon"],
        "country": "IN",
        "state": city["state"],
    }])


# ── Current Weather ───────────────────────────────────────────────────────

@app.get("/data/2.5/weather")
def get_weather(
    q: str | None = Query(None, description="City name, e.g. 'Mumbai' or 'Delhi,IN'"),
    lat: float | None = Query(None),
    lon: float | None = Query(None),
    appid: str | None = Query(None, description="API key"),
    units: str = Query("standard", description="standard | metric | imperial"),
):
    _verify_key(appid)
    city = _find_city(q=q, lat=lat, lon=lon)
    if not city:
        raise HTTPException(status_code=404, detail={"cod": "404", "message": "city not found"})

    data = _generate_weather(city)
    data = _convert_units(data, units)
    return JSONResponse(content=data)


@app.get("/data/2.5/forecast")
def get_forecast(
    q: str | None = Query(None),
    lat: float | None = Query(None),
    lon: float | None = Query(None),
    appid: str | None = Query(None),
    units: str = Query("standard"),
    cnt: int = Query(8, description="Number of 3-hour forecast entries"),
):
    _verify_key(appid)
    city = _find_city(q=q, lat=lat, lon=lon)
    if not city:
        raise HTTPException(status_code=404, detail={"cod": "404", "message": "city not found"})

    now = int(time.time())
    forecasts = []
    for i in range(min(cnt, 40)):
        future_ts = now + i * 10800
        seed = int(hashlib.md5(f"{city['name']}{future_ts // 3600}".encode()).hexdigest()[:8], 16)
        rng = random.Random(seed)
        temp_c = city["temp_base"] + rng.uniform(-4, 4)
        pool = WEATHER_POOLS[city["pool_idx"]]
        weather_cond = rng.choice(pool)
        entry = {
            "dt": future_ts,
            "main": {
                "temp": round(temp_c + 273.15, 2),
                "feels_like": round(temp_c + rng.uniform(-2, 2) + 273.15, 2),
                "temp_min": round(temp_c - rng.uniform(1, 3) + 273.15, 2),
                "temp_max": round(temp_c + rng.uniform(1, 3) + 273.15, 2),
                "pressure": rng.randint(1005, 1020),
                "humidity": max(10, min(100, city["humidity_base"] + rng.randint(-10, 10))),
            },
            "weather": [weather_cond],
            "clouds": {"all": rng.randint(5, 95)},
            "wind": {"speed": round(rng.uniform(1.5, 8.5), 2), "deg": rng.randint(0, 360)},
            "visibility": rng.randint(4000, 10000),
            "dt_txt": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(future_ts)),
        }
        if units == "metric":
            entry["main"]["temp"] = round(entry["main"]["temp"] - 273.15, 2)
            entry["main"]["feels_like"] = round(entry["main"]["feels_like"] - 273.15, 2)
            entry["main"]["temp_min"] = round(entry["main"]["temp_min"] - 273.15, 2)
            entry["main"]["temp_max"] = round(entry["main"]["temp_max"] - 273.15, 2)
        forecasts.append(entry)

    return JSONResponse(content={
        "cod": "200",
        "message": 0,
        "cnt": len(forecasts),
        "list": forecasts,
        "city": {
            "id": int(hashlib.md5(city["name"].encode()).hexdigest()[:7], 16),
            "name": city["name"],
            "coord": {"lat": city["lat"], "lon": city["lon"]},
            "country": "IN",
            "timezone": 19800,
            "sunrise": now - (now % 86400) + 21600,
            "sunset": now - (now % 86400) + 64800,
        },
    })


# ── Air Pollution ─────────────────────────────────────────────────────────

@app.get("/data/2.5/air_pollution")
def get_air_pollution(
    lat: float = Query(...),
    lon: float = Query(...),
    appid: str | None = Query(None),
):
    _verify_key(appid)
    city = _find_city(lat=lat, lon=lon)
    if not city:
        raise HTTPException(status_code=404, detail={"cod": "404", "message": "city not found"})

    seed = int(hashlib.md5(f"{city['name']}{int(time.time()) // 3600}".encode()).hexdigest()[:8], 16)
    rng = random.Random(seed)

    humidity = city["humidity_base"]
    if humidity > 70:
        aqi = rng.randint(3, 5)
    elif humidity > 50:
        aqi = rng.randint(2, 4)
    else:
        aqi = rng.randint(1, 3)

    return JSONResponse(content={
        "coord": {"lon": lon, "lat": lat},
        "list": [{
            "main": {"aqi": aqi},
            "components": {
                "co": round(rng.uniform(200, 500), 2),
                "no": round(rng.uniform(0.5, 10), 2),
                "no2": round(rng.uniform(5, 60), 2),
                "o3": round(rng.uniform(20, 120), 2),
                "so2": round(rng.uniform(1, 30), 2),
                "pm2_5": round(rng.uniform(5, 80), 2),
                "pm10": round(rng.uniform(10, 150), 2),
                "nh3": round(rng.uniform(0.5, 15), 2),
            },
            "dt": int(time.time()),
        }],
    })


@app.get("/data/2.5/uvi")
def get_uvi(
    lat: float = Query(...),
    lon: float = Query(...),
    appid: str | None = Query(None),
):
    _verify_key(appid)
    city = _find_city(lat=lat, lon=lon)
    if not city:
        raise HTTPException(status_code=404, detail={"cod": "404", "message": "location not found"})
    
    seed = int(hashlib.md5(f"{city['name']}{int(time.time()) // 3600}".encode()).hexdigest()[:8], 16)
    rng = random.Random(seed)
    
    # UV index based on temperature and time
    temp_base = city["temp_base"]
    uv_base = max(0, min(11, (temp_base - 15) / 3))
    uv = round(uv_base + rng.uniform(-1.5, 1.5), 1)
    
    return JSONResponse(content={
        "lat": lat,
        "lon": lon,
        "date_iso": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "date": int(time.time()),
        "value": max(0, min(11, uv)),
    })


@app.get("/data/2.5/onecall")
def get_onecall(
    lat: float = Query(...),
    lon: float = Query(...),
    appid: str | None = Query(None),
    units: str = Query("standard"),
    exclude: str = Query(""),
):
    _verify_key(appid)
    city = _find_city(lat=lat, lon=lon)
    if not city:
        raise HTTPException(status_code=404, detail={"cod": "404", "message": "location not found"})
    
    now = int(time.time())
    seed = _deterministic_seed(city["name"])
    rng = random.Random(seed)
    
    current = _generate_weather(city)
    current = _convert_units(current, units)
    
    # 48-hour hourly forecast
    hourly = []
    for i in range(48):
        future_ts = now + i * 3600
        hr_seed = int(hashlib.md5(f"{city['name']}{future_ts // 3600}".encode()).hexdigest()[:8], 16)
        hr_rng = random.Random(hr_seed)
        temp_c = city["temp_base"] + hr_rng.uniform(-4, 4)
        pool = WEATHER_POOLS[city["pool_idx"]]
        hourly.append({
            "dt": future_ts,
            "temp": round(temp_c + 273.15 if units == "standard" else temp_c, 2),
            "feels_like": round(temp_c + hr_rng.uniform(-2, 2) + (273.15 if units == "standard" else 0), 2),
            "humidity": max(10, min(100, city["humidity_base"] + hr_rng.randint(-10, 10))),
            "weather": [hr_rng.choice(pool)],
        })
    
    # 7-day daily forecast
    daily = []
    for i in range(7):
        day_ts = now + i * 86400
        day_seed = int(hashlib.md5(f"{city['name']}{day_ts // 86400}".encode()).hexdigest()[:8], 16)
        day_rng = random.Random(day_seed)
        temp_c = city["temp_base"] + day_rng.uniform(-3, 3)
        pool = WEATHER_POOLS[city["pool_idx"]]
        daily.append({
            "dt": day_ts,
            "temp": {
                "day": round(temp_c + (273.15 if units == "standard" else 0), 2),
                "min": round(temp_c - 3 + (273.15 if units == "standard" else 0), 2),
                "max": round(temp_c + 3 + (273.15 if units == "standard" else 0), 2),
                "night": round(temp_c - 5 + (273.15 if units == "standard" else 0), 2),
            },
            "humidity": max(10, min(100, city["humidity_base"] + day_rng.randint(-10, 10))),
            "weather": [day_rng.choice(pool)],
        })
    
    return JSONResponse(content={
        "lat": city["lat"],
        "lon": city["lon"],
        "timezone": "Asia/Kolkata",
        "timezone_offset": 19800,
        "current": current,
        "hourly": hourly if "hourly" not in exclude else [],
        "daily": daily if "daily" not in exclude else [],
    })


@app.get("/api/cities")
def get_cities():
    unique_cities = {v["name"]: v for v in CITIES.values()}.values()
    return JSONResponse(content=[c["name"] for c in sorted(unique_cities, key=lambda x: x["name"])])


@app.get("/")
def root():
    return {
        "service": "OpenWeather Mock API",
        "version": "2.5",
        "endpoints": [
            "/data/2.5/weather?q={city}&appid={key}&units=metric",
            "/data/2.5/forecast?q={city}&appid={key}&units=metric",
            "/data/2.5/uvi?lat={lat}&lon={lon}&appid={key}",
            "/data/2.5/onecall?lat={lat}&lon={lon}&appid={key}&units=metric",
            "/api/cities",
        ],
        "valid_api_keys": ["mock_api_key_agno_2026"],
        "total_cities": len({id(v): v for v in CITIES.values()}),
    }
