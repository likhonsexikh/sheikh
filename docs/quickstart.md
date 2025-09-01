# Quick Start

This guide will get you up and running with Sheikh LLM in just a few minutes.

## 1. Using Docker

The fastest way to start is with Docker.

```bash
# Pull the image
docker pull ghcr.io/likhonsexikh/sheikh:latest

# Run the server
docker run -d -p 8080:8080 --name sheikh-llm ghcr.io/likhonsexikh/sheikh:latest

# Test the server
curl http://localhost:8080/health
```

## 2. Using the Python SDK

```python
# Install the SDK
pip install sheikh-sdk

# Use in your code
from sheikh_sdk import Sheikh

client = Sheikh(host="localhost", port=8080)
response = client.generate("Hello, world!")
print(response)
```

For more detailed instructions, see the [Deployment Guide](deployment_guide.md).
