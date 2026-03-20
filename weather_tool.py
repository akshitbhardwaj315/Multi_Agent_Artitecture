import requests
from agno.tools import Toolkit


class WeatherTools(Toolkit):
    def __init__(self, api_key: str = "mock_api_key_agno_2026", base_url: str = "http://localhost:8001"):
        super().__init__(name="weather_tools")
        self.api_key = api_key
        self.base_url = base_url
        self.register(self.get_weather)

    def get_weather(self, city: str) -> str:
        """Get current weather for a city in India.

        Args:
            city: City name like 'Mumbai', 'Delhi', 'Bengaluru'.
        """
        r = requests.get(f"{self.base_url}/data/2.5/weather", params={"q": city, "appid": self.api_key, "units": "metric"})
        d = r.json()
        if r.status_code != 200:
            return f"City '{city}' not found."
        return f"{d['name']}: {d['main']['temp']}°C, {d['weather'][0]['description']}, humidity {d['main']['humidity']}%"
