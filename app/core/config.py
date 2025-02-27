from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_URL: str
    DB_ECHO: bool = False

    model_config = SettingsConfigDict(
        env_file="app/core/.env",  # Укажите правильный путь к .env файлу
        env_file_encoding="utf-8",
        extra="ignore"
    )

# Создаем экземпляр настроек
settings = Settings()

if not settings.DB_URL:
    raise ValueError("DB_URL is not set in the environment variables.")