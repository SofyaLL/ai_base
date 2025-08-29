from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / ".env"


class Settings(BaseSettings):
    app_name: str = "Awesome API"
    openai_api_key: str = None
    model_config = SettingsConfigDict(env_file=ENV_FILE)


settings = Settings()
