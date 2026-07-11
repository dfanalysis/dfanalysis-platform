from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "DF Analysis IA"

    APP_ENV: str = "development"

    APP_HOST: str = "0.0.0.0"

    APP_PORT: int = 8000

    DATABASE_HOST: str

    DATABASE_PORT: int

    DATABASE_NAME: str

    DATABASE_USER: str

    DATABASE_PASSWORD: str

    JWT_SECRET: str = ""

    JWT_ALGORITHM: str = "HS256"

    OPENAI_API_KEY: str = ""

    REDIS_HOST: str = "redis"

    REDIS_PORT: int = 6379

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True
    )


settings = Settings()