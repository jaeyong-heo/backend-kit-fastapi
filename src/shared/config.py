from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parents[2]  # backend-kit-fastapi

class Settings(BaseSettings):
    # 기본 앱 설정
    APP_NAME: str = "fastapi-app"
    APP_ENV: str = "local"

    # DB 개별 값
    DB_HOST: str
    DB_PORT: int = 3306
    DB_USER: str
    DB_PASSWORD: str
    DB_DATABASE: str

    

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


settings = Settings()