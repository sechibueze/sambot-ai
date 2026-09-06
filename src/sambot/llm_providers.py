from sambot.chat import Message
from sambot.llm import LLMProvider


class FakeProvider(LLMProvider):
    """Fake LLM provider for development and testing."""

    def ask(self, messages: list[Message]) -> str:
        """Return a fake response."""
        last_message = messages[-1]["content"]

        return f"You said: {last_message}"