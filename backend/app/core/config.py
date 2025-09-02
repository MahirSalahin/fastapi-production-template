from pydantic_settings import BaseSettings
from pydantic import AnyUrl, BeforeValidator, PostgresDsn
from functools import lru_cache
from dotenv import load_dotenv
from typing import Any, Annotated

load_dotenv()


def parse_cors(v: Any) -> list[str] | str:
    if isinstance(v, str) and not v.startswith("["):
        return [i.strip() for i in v.split(",")]
    elif isinstance(v, list | str):
        return v
    raise ValueError(v)


class Settings(BaseSettings):
    FRONTEND_URL: str
    BACKEND_API_URL: str
    DATABASE_URL: str
    BACKEND_CORS_ORIGINS: Annotated[list[AnyUrl] | str, BeforeValidator(parse_cors)] = (
        []
    )

    @property
    def POSTGRES_DATABASE_URL(self) -> PostgresDsn:
        return self.DATABASE_URL

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "allow"


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
