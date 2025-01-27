#!/bin/bash

# Use the DOCKERHUB_USERNAME environment variable
DOCKERHUB_USERNAME="${DOCKERHUB_USERNAME}"  # No need to replace; it uses the environment variable
APP_NAME="oc_lettings_site"  # Replace with your Docker image name
TAG="latest"  # Use "latest" or specify a commit hash

# Check if DOCKERHUB_USERNAME is set
if [ -z "$DOCKERHUB_USERNAME" ]; then
    echo "ERROR: The DOCKERHUB_USERNAME environment variable is not set."
    exit 1
fi

# Pull the Docker image from Docker Hub
echo "Pulling the Docker image..."
docker pull $DOCKERHUB_USERNAME/$APP_NAME:$TAG

export PORT=8000

# Run the Docker container
echo "Running the Docker container..."
docker run -e PORT=8000 -p 8000:8000 $DOCKERHUB_USERNAME/$APP_NAME:$TAG
