
from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    def __init__(
        self,
        POSTGRES_USER: str,
        POSTGRES_PASSWORD: str,
        POSTGRES_PORT: str,
        POSTGRES_HOST: str,
        POSTGRES_DB: str,
        URL_PREFIX: str,
        FASTAPI_PORT: str,
        FASTAPI_HOST: str,
        FASTAPI_DB_HOST: str
    ):
        self.POSTGRES_PORT = POSTGRES_PORT
        self.POSTGRES_HOST = POSTGRES_HOST
        self.POSTGRES_DB = POSTGRES_DB
        self.POSTGRES_USER = POSTGRES_USER
        self.POSTGRES_PASSWORD = POSTGRES_PASSWORD
        self.DATABASE_URL_ASYNC=f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{FASTAPI_DB_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
        self.DATABASE_URL_SYNC=f"postgresql+psycopg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{FASTAPI_DB_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
        self.URL_PREFIX = URL_PREFIX
        self.FASTAPI_PORT = FASTAPI_PORT
        self.FASTAPI_HOST = FASTAPI_HOST
        self.FASTAPI_DB_HOST = FASTAPI_DB_HOST



config = Config(
    POSTGRES_USER=os.getenv("POSTGRES_USER"),
    POSTGRES_PASSWORD=os.getenv("POSTGRES_PASSWORD"),
    POSTGRES_PORT=os.getenv("POSTGRES_PORT"),
    POSTGRES_HOST=os.getenv("POSTGRES_HOST"),
    POSTGRES_DB=os.getenv("POSTGRES_DB"),
    URL_PREFIX="/balance-api",
    FASTAPI_HOST=os.getenv("FASTAPI_HOST"),
    FASTAPI_PORT=os.getenv("FASTAPI_PORT"),
    FASTAPI_DB_HOST=os.getenv("FASTAPI_DB_HOST")
)