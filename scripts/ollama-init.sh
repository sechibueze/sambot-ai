#!/bin/sh

set -e

echo "Waiting for Ollama..."

until ollama list; do
    echo "Ollama is not ready yet..."
    sleep 2
done

echo "Ollama is ready."

echo "Pulling tinyllama:1.1b..."
ollama pull tinyllama:1.1b

echo "Installed models:"
ollama list

echo "Ollama initialization complete."