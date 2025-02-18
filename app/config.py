from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_env: str = "development"
    app_debug: bool = False
    app_secret_key: str
    db_url: str


def get_settings():
    return Settings()
