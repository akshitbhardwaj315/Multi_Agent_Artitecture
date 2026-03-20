import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    def __init__(self):
        self.groq_api_key = os.getenv("GROQ_API_KEY")
        self.openweather_api_key = os.getenv("OPENWEATHER_API_KEY", "mock_api_key_agno_2026")
        self.openweather_base_url = os.getenv("OPENWEATHER_BASE_URL", "http://localhost:8001")
        self.main_port = int(os.getenv("MAIN_PORT", "8000"))
        self.mock_port = int(os.getenv("MOCK_PORT", "8001"))
        self.max_history = int(os.getenv("MAX_HISTORY", "10"))
        self.max_retries = int(os.getenv("MAX_RETRIES", "3"))
        self.news_cache_ttl = int(os.getenv("NEWS_CACHE_TTL", "300"))
        
        if not self.groq_api_key:
            raise ValueError(
                "GROQ_API_KEY is required but not found in environment. "
                "Please set it in your .env file."
            )


settings = Settings()
