import logging
from sambot.llm import LLMProvider

from sambot.chat import Message
from sambot.config import settings
from sambot.llm_providers import FakeProvider

logger = logging.getLogger(__name__)

def get_provider() -> LLMProvider:
    """Return the configured LLM provider."""

    if settings.llm_provider == "fake":
        return FakeProvider()

    raise ValueError(
        f"Unsupported LLM provider: {settings.llm_provider}"
    )


def ask_ai(messages: list[Message]) -> str:
    """Send messages to the configured LLM provider."""
    logger.info(
        "Sending request to LLM provider: %s",
        settings.llm_provider,
    )
    provider = get_provider()

    return provider.ask(messages)