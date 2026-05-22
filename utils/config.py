"""
Configuration module. Pure setup from .env via pydantic-settings.
"""
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    groq_api_key: str
    
    server_host: str = "0.0.0.0"
    main_port: int = 8000
    mock_port: int = 8001
    
    # Dynamic URL based on settings
    @property
    def mock_weather_url(self) -> str:
        return f"http://localhost:{self.mock_port}"

    validator_confidence_threshold: float = 0.4
    llm_fast_model: str = "llama-3.1-8b-instant"
    llm_smart_model: str = "llama-3.3-70b-versatile"
    
    chroma_path: str = "data/chroma"
    chroma_collection: str = "documents"
    bm25_index_path: str = "data/bm25_index.pkl"
    checkpoint_db_path: str = "data/checkpoints.db"
    hitl_db_path: str = "data/hitl.db"
    environment: str = "development"

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
