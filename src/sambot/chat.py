from typing import TypedDict


class Message(TypedDict):
    role: str
    content: str


def create_message(role: str, content: str) -> Message:
    """Create a chat message."""
    return {
        "role": role,
        "content": content,
    }


def create_conversation() -> list[Message]:
    """Create an empty conversation."""
    return []


def add_message(
    messages: list[Message],
    role: str,
    content: str,
) -> None:
    """Add a message to a conversation."""
    messages.append(create_message(role, content))


def get_user_messages(
    messages: list[Message],
) -> list[Message]:
    """Return only user messages from a conversation."""
    return [
        message
        for message in messages
        if message["role"] == "user"
    ]