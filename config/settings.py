"""Project settings (placeholders)."""
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    openai_api_key: str
    generational_model_id: str
    provider: str = "google"

    tavily_api_key: str | None = None

    langsmith_api_key: str | None = None
    langsmith_tracing: bool = False
    langsmith_endpoint: str | None = None
    langsmith_project: str | None = None
    language: str = "en"
    timezone: str = "Africa/Cairo"  # add this




    class Config():
        env_file =".env"


def get_settings(): 
    return Settings()