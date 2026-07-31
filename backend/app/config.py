from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    # FastAPI
    APP_NAME: str = "KlashAI"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = False

    # Database
    DATABASE_URL: str = "postgresql+asyncpg://klashai:klashai@localhost:5432/klashai"

    # Redis
    REDIS_URL: str = "redis://localhost:6379"

    # CORS
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",  # Frontend dev server
        "http://localhost:80",   # Frontend via Nginx
    ]

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
