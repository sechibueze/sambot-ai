from sambot.chat import (
    add_message,
    create_conversation,
    create_message,
    get_user_messages,
)


def test_create_message() -> None:
    message = create_message(
        "user",
        "Hello Sambot",
    )

    assert message == {
        "role": "user",
        "content": "Hello Sambot",
    }


def test_create_conversation() -> None:
    conversation = create_conversation()

    assert conversation == []


def test_add_message() -> None:
    conversation = create_conversation()

    add_message(
        conversation,
        "user",
        "Hello",
    )

    assert len(conversation) == 1
    assert conversation[0]["role"] == "user"
    assert conversation[0]["content"] == "Hello"


def test_get_user_messages() -> None:
    conversation = [
        {
            "role": "user",
            "content": "Hello",
        },
        {
            "role": "assistant",
            "content": "Hi!",
        },
        {
            "role": "user",
            "content": "How are you?",
        },
    ]

    user_messages = get_user_messages(conversation)

    assert len(user_messages) == 2
    assert user_messages[0]["content"] == "Hello"
    assert user_messages[1]["content"] == "How are you?"