from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Todo"
    DATABASE_URL: str

    class Config:
        env_file = ".env"
        env_file_enconding = "utf-8"


settings = Settings()