#!/bin/bash
# examples/docker_deploy.sh

# This script demonstrates how to pull the Sheikh LLM Docker image
# and run it as a detached container.

set -e

IMAGE_NAME="ghcr.io/likhonsexikh/sheikh:latest"
CONTAINER_NAME="sheikh-llm-container"

echo "--- Pulling latest Sheikh LLM Docker image ---"
docker pull "$IMAGE_NAME"

# Check if a container with the same name is already running
if [ "$(docker ps -q -f name=$CONTAINER_NAME)" ]; then
    echo "--- Stopping and removing existing container: $CONTAINER_NAME ---"
    docker stop "$CONTAINER_NAME"
    docker rm "$CONTAINER_NAME"
fi

echo "--- Starting new Sheikh LLM container in detached mode ---"
docker run -d \
    --name "$CONTAINER_NAME" \
    -p 8080:8080 \
    -v "$(pwd)/../model":/app/model:ro \
    --restart unless-stopped \
    "$IMAGE_NAME"

echo ""
echo "✅ Sheikh LLM container started successfully!"
echo "API server should be available at http://localhost:8080"
echo "To see logs, run: docker logs $CONTAINER_NAME"
echo "To stop the container, run: docker stop $CONTAINER_NAME"
