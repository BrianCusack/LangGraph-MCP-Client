from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    DB_NAME: str = Field(..., env="DB_NAME")
    DB_USER: str = Field(..., env="DB_USER")
    DB_PASSWORD: str = Field(..., env="DB_PASSWORD")
    DB_HOST: str = Field(..., env="DB_HOST")
    DB_PORT: str = Field(..., env="DB_PORT")
    DB_SSLMODE: str = Field(..., env="DB_SSLMODE")
    ANTHROPIC_API_KEY: str = Field(..., env="ANTHROPIC_API_KEY")

    CLAUDE_MODEL: str = Field(..., env="CLAUDE_MODEL")

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
