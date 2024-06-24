import os
from pathlib import Path

from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent


class Settings(BaseSettings):

    # Режим работы
    APP_PORT: int
    EXTERNAL_PORT: int

    class Config:
        env_file = os.path.join(BASE_DIR, '.env')


settings = Settings()
