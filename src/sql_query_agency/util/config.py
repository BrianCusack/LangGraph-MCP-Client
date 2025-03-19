from pydantic_settings import BaseSettings
from pydantic import Field, ConfigDict


class Settings(BaseSettings):
    DB_NAME: str = Field(..., json_schema_extra={"env":"DB_NAME"})
    DB_USER: str = Field(..., json_schema_extra={"env":"DB_USER"})
    DB_PASSWORD: str = Field(..., json_schema_extra={"env":"DB_PASSWORD"})
    DB_HOST: str = Field(..., json_schema_extra={"env":"DB_HOST"})
    DB_PORT: str = Field(..., json_schema_extra={"env":"DB_PORT"})
    DB_SSLMODE: str = Field(..., json_schema_extra={"env":"DB_SSLMODE"})
    ANTHROPIC_API_KEY: str = Field(..., json_schema_extra={"env":"ANTHROPIC_API_KEY"})
    CLAUDE_MODEL: str = Field("claude-3-7-sonnet-latest", json_schema_extra={"env":"CLAUDE_MODEL"})
    LANGSMITH_TRACING: bool = Field(False, json_schema_extra={"env":"LANGSMITH_TRACING"})
    LANGSMITH_ENDPOINT: str = Field("https://api.langsmith.com", json_schema_extra={"env":"LANGSMITH_ENDPOINT"})
    LANGSMITH_API_KEY: str = Field("", json_schema_extra={"env":"LANGSMITH_API_KEY"})
    LANGSMITH_PROJECT: str = Field("", json_schema_extra={"env":"LANGSMITH_PROJECT"})

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = ConfigDict(populate_by_name=True)
