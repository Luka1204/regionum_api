from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "Tango563#43"
    DB_NAME: str = "regionum"

    class Config:
        env_file = ".env"

settings = Settings()