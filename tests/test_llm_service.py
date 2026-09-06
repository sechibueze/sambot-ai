from sambot.chat import create_message
from sambot.llm_service import ask_ai, get_provider
from sambot.providers import FakeProvider


def test_fake_provider_is_used() -> None:
    provider = get_provider()

    assert isinstance(provider, FakeProvider)


def test_ask_ai_returns_response() -> None:
    messages = [
        create_message(
            "user",
            "What is Docker?",
        )
    ]

    response = ask_ai(messages)

    assert response == "You said: What is Docker?"

def test_invalid_provider() -> None:
    original_provider = settings.llm_provider

    settings.llm_provider = "invalid"

    try:
        with pytest.raises(ValueError):
            get_provider()
    finally:
        settings.llm_provider = original_provider