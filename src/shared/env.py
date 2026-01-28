from typing import Optional
from pydantic_settings import BaseSettings


# Setting config load
class GlobalSettings(BaseSettings):
    APP_ENV: str
    TOKEN_URL: str
    PUBLIC_KEY_PATH: str
    JWT_ALGORITHM: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DB_DATABASE: str
    SECRET_URL: str
    CLIENT_ID: str
    CLIENT_SECRET: str
    ONLYOFFICE_TOKEN_KEY: str

    LINK_CONSULTATION: Optional[str] = None
    LINK_DEFAULT: Optional[str] = None
    
    CONFIRMER_EMAIL: Optional[str] = None
    CONFIRMER_NAME: Optional[str] = None

    SMTP_HOST: Optional[str] = None
    SMTP_PORT: Optional[str] = None
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    FROM_EMAIL: Optional[str] = None
    EMAIL_SUPPORT: Optional[str] = None

    RENEWAL_DATE: Optional[str] = None

    DEV_PUBLIC_KEY_PATH: Optional[str] = None
    DEV_SECRET_KEY_PATH: Optional[str] = None
    DEV_EXPIRE_DAY: Optional[float] = None
    
    ITALKBIZ_API_URL: Optional[str] = None
    ITALKBIZ_API_URL_MULTI: Optional[str] = None
    ITALKBIZ_API_KEY: Optional[str] = None
    ITALKBIZ_SENDER_KEY: Optional[str] = None
    ITALKBIZ_TAMPLATE_DAY: Optional[str] = None
    ITALKBIZ_TAMPLATE_WEEK: Optional[str] = None

    AES_SECRET_KEY: Optional[str] = None
    
    def get(self, key: str, default=None):
        return getattr(self, key, default)

    class Config:
        env_file = ".env"


class DevSettings(GlobalSettings):
    # 권한 변경을 위한 암호키
    DEV_PUBLIC_KEY_PATH: Optional[str] = None
    DEV_SECRET_KEY_PATH: Optional[str] = None
    DEV_EXPIRE_DAY: Optional[float] = None

    class Config:
        env_file = "dev.env"


class LocalSettings(DevSettings):
    class Config:
        env_file = "local.env"


class StagingSettings(GlobalSettings):
    class Config:
        env_file = "staging.env"


class ProdSettings(GlobalSettings):
    class Config:
        env_file = "prod.env"


class FactorySettings:
    @staticmethod
    def load():
        app_env = GlobalSettings().APP_ENV
        match app_env:
            case 'dev':
                return DevSettings()
            case 'local':
                return LocalSettings()
            case 'staging':
                return StagingSettings()
            case 'prod':
                return ProdSettings()


settings = FactorySettings.load()
