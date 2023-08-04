import os

from pydantic import BaseSettings
from dotenv import load_dotenv


load_dotenv(verbose=True, encoding='utf8')


class Settings(BaseSettings):

    SECRET_KEY: str = os.getenv('SECRET_KEY')
    HASH_ALGORITHM: str = os.getenv('HASH_ALGORITHM')

    POSTGRES_SERVER: str = os.getenv('POSTGRES_SERVER')
    POSTGRES_USER: str = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_DB: str = os.getenv('POSTGRES_DB')

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    
settings = Settings()
