import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

LLM_PROVIDER = os.getenv("LLM_PROVIDER", "ollama")

OLLAMA_BASE_URL = os.getenv(
    "OLLAMA_BASE_URL",
    "http://localhost:11434/v1"
)

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "llama3.2"
)

OPENAI_MODEL = os.getenv(
    "OPENAI_MODEL",
    "gpt-4o-mini"
)


def ask_ai(messages: list[dict]) -> str:
    if LLM_PROVIDER == "ollama":
        return _ask_ollama(messages)

    if LLM_PROVIDER == "openai":
        return _ask_openai(messages)

    raise ValueError(
        f"Unsupported LLM provider: {LLM_PROVIDER}"
    )


def _ask_ollama(messages: list[dict]) -> str:
    client = OpenAI(
        base_url=OLLAMA_BASE_URL,
        api_key="ollama"
    )

    response = client.chat.completions.create(
        model=OLLAMA_MODEL,
        messages=messages,
    )

    return response.choices[0].message.content


def _ask_openai(messages: list[dict]) -> str:
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY")
    )

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=messages,
    )

    return response.choices[0].message.content