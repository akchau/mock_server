import os
from pathlib import Path

from pydantic import BaseSettings

BASE_DIR = Path(__file__).resolve().parent


class Settings(BaseSettings):

    # Режим работы
    APP_PORT: int
    EXTERNAL_PORT: int
    RESPONSE_CODE: int
    READ_DELAY: int
    FILE: bool
    REMOVE_CONTENT_TYPE: bool

    class Config:
        env_file = os.path.join(BASE_DIR, '.env')


settings = Settings()
