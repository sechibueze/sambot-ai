FROM python:3.12-slim

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Install dependencies first for better Docker layer caching
COPY pyproject.toml uv.lock README.md ./

RUN uv sync --frozen --no-dev

# Copy application source
COPY src ./src

# Runtime environment
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

EXPOSE 8501

CMD ["uv", "run", "streamlit", "run", "src/sambot/app.py", "--server.address=0.0.0.0", "--server.port=8501"]