import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Application configuration."""

    llm_provider: str = os.getenv(
        "LLM_PROVIDER",
        "fake",
    )

    ollama_base_url: str = os.getenv(
        "OLLAMA_BASE_URL",
        "http://localhost:11434/v1",
    )

    ollama_model: str = os.getenv(
        "OLLAMA_MODEL",
        "llama3.2",
    )

    openai_api_key: str | None = os.getenv(
        "OPENAI_API_KEY"
    )

    openai_model: str = os.getenv(
        "OPENAI_MODEL",
        "gpt-4o-mini",
    )


settings = Settings()