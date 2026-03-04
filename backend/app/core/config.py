from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENVIRONMENT: str = "local"
    DATABASE_URL: str
    REDIS_URL: str
    SECRET_KEY: str
    
    LLM_PROVIDER: str = "openai"
    LLM_MODEL: str = "gpt-4o-mini"
    OPENROUTER_API_KEY: str | None = None

    class Config:
        env_file = ".env"


settings = Settings()