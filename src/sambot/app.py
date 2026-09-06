import logging

import streamlit as st

from sambot.chat import (
    add_message,
    create_conversation,
    get_user_messages,
)
from sambot.llm_service import ask_ai
from sambot.logging import setup_logging


setup_logging()

logger = logging.getLogger(__name__)


st.set_page_config(
    page_title="Sambot",
    page_icon="🤖",
    layout="centered",
)


def initialize_session() -> None:
    """Initialize the Streamlit chat session."""
    if "messages" not in st.session_state:
        st.session_state.messages = create_conversation()


def render_sidebar() -> None:
    """Render the application sidebar."""
    with st.sidebar:
        st.header("🤖 Sambot")

        if st.button("New conversation"):
            st.session_state.messages = create_conversation()
            st.rerun()

        st.divider()

        st.subheader("Conversation")

        user_messages = get_user_messages(
            st.session_state.messages
        )

        if not user_messages:
            st.caption("No messages yet.")
            return

        for message in user_messages:
            st.write(message["content"][:50])


def render_chat() -> None:
    """Render existing chat messages."""
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])


def handle_user_input() -> None:
    """Process new user input."""
    prompt = st.chat_input("Ask Sambot anything...")

    if not prompt:
        return

    logger.info("User sent a message")

    add_message(
        st.session_state.messages,
        "user",
        prompt,
    )

    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = ask_ai(
                st.session_state.messages
            )

        st.write(response)

    add_message(
        st.session_state.messages,
        "assistant",
        response,
    )


def main() -> None:
    """Run Sambot."""
    logger.info("Starting Sambot")

    st.title("🤖 Sambot")
    st.caption("Your personal AI assistant")

    initialize_session()
    render_sidebar()
    render_chat()
    handle_user_input()


if __name__ == "__main__":
    main()