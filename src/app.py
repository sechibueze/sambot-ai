import streamlit as st

st.set_page_config(
    page_title="Sambot",
    page_icon="🤖",
    layout="centered",
)


def main() -> None:
    """Run the Sambot Streamlit application."""
    st.title("🤖 Sambot")
    st.caption("Your personal AI assistant")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    with st.sidebar:
        st.header("Sambot")

        if st.button("New conversation"):
            st.session_state.messages = []
            st.rerun()

        st.divider()

        st.subheader("Conversation")

        user_messages = [
            message
            for message in st.session_state.messages
            if message["role"] == "user"
        ]

        if not user_messages:
            st.caption("No messages yet.")
        else:
            for message in user_messages:
                st.write(message["content"][:50])

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if prompt := st.chat_input("Ask Sambot anything..."):
        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt,
            }
        )

        with st.chat_message("user"):
            st.write(prompt)

        # Temporary response.
        # We will replace this with ask_ai() later.
        response = f"You said: {prompt}"

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response,
            }
        )

        with st.chat_message("assistant"):
            st.write(response)


if __name__ == "__main__":
    main()