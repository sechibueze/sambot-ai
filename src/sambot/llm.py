from abc import ABC, abstractmethod

from sambot.chat import Message


class LLMProvider(ABC):
    """Interface for an LLM provider."""

    @abstractmethod
    def ask(self, messages: list[Message]) -> str:
        """Send messages to the LLM and return its response."""
        raise NotImplementedError