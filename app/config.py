from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    redis_url: str
    google_maps_api_key: str
    api_key_secret: str
    environment: str = "development"

    class Config:
        env_file = ".env"

settings = Settings()