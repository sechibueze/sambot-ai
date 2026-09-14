from sambot.chat import Message
from sambot.llm import LLMProvider
import os
import requests

class FakeProvider(LLMProvider):
    """Fake LLM provider for development and testing."""

    def ask(self, messages: list[Message]) -> str:
        """Return a fake response."""
        last_message = messages[-1]["content"]

        return f"You said: {last_message}"

class OllamaProvider(LLMProvider):
    """Ollama LLM provider."""

    def ask(self, messages: list[Message]) -> str:
        """Return an Ollama response."""

        url = os.getenv(
            "OLLAMA_BASE_URL",
            "http://localhost:11434/api",
        )
        model = os.getenv(
            "OLLAMA_MODEL",
            "qwen3.8:latest",
        )
        payload = {
            "model": model,
            "messages": messages,
            "stream": False,
        }

        response = requests.post(
            f"{url}/chat",
            json=payload,
        )

        response.raise_for_status()

        data = response.json()
        # print("Ollama response data:", data)  # Debugging line

        return data["message"]["content"]