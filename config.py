# config.py
# Loads env vars from .env file
from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    DATABASE_URL: str

    class Config:
        env_file = ".env"

# Create a single instance to import elsewhere
settings = Settings()

