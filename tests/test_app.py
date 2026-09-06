from sambot.chat import create_message


def test_create_user_message() -> None:
    message = create_message(
        "user",
        "Hello Sambot",
    )

    assert message == {
        "role": "user",
        "content": "Hello Sambot",
    }


def test_create_assistant_message() -> None:
    message = create_message(
        "assistant",
        "Hello! How can I help?",
    )

    assert message["role"] == "assistant"
    assert message["content"] == "Hello! How can I help?"