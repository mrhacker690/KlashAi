from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    # General
    environment: str = "development"
    secret_key: str
    allowed_origins: list[str] = ["http://localhost:3000"]

    # Database
    database_url: str

    # Redis
    redis_url: str

    class Config:
        env_file = ".env"


settings = Settings()
