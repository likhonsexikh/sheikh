# Deployment Guide

This guide provides instructions for deploying Sheikh LLM in various environments.

## Using Docker (Recommended)

Docker is the recommended way to deploy Sheikh LLM as it encapsulates all dependencies.

### Prerequisites

-   Docker installed on your system.

### Running the Container

1.  **Pull the Image**:
    Pull the latest image from the GitHub Container Registry.
    ```bash
    docker pull ghcr.io/likhonsexikh/sheikh:latest
    ```

2.  **Run the Container**:
    Start the container in detached mode and map the port.
    ```bash
    docker run -d -p 8080:8080 --name sheikh-llm ghcr.io/likhonsexikh/sheikh:latest
    ```

3.  **Verify**:
    Check that the container is running and healthy.
    ```bash
    docker ps
    curl http://localhost:8080/health
    ```

## As a Standalone Binary

You can also run the compiled runtime binary directly on your machine.

### Prerequisites

-   A compatible operating system (Linux, macOS).
-   The model file (`sheikh.gguf`) downloaded.

### Running the Binary

1.  **Download Release**:
    Download the latest release archive from the [GitHub Releases page](https://github.com/likhonsexikh/sheikh/releases).

2.  **Extract the Archive**:
    ```bash
    tar -xzf sheikh-vX.X.X-linux-amd64.tar.gz
    ```

3.  **Make Executable**:
    ```bash
    chmod +x sheikh-linux-x64
    ```

4.  **Run the Server**:
    ```bash
    ./sheikh-linux-x64 --model sheikh.gguf --server --host 0.0.0.0 --port 8080
    ```

## Building from Source

If you need to build the runtime from source, refer to the instructions in the `runtime/` directory of the repository.

---

## Publishing to Hugging Face Hub

The CI/CD pipeline is configured to automatically upload the model files (`sheikh.gguf`, `tokenizer.json`, `metadata.json`) to the Hugging Face Hub when a new version tag is pushed.

This is handled by the `publish-to-hf` job in the workflow.

## Repository Secrets Configuration

For the automation to work correctly, you must configure the following secrets in your GitHub repository's settings (`Settings > Secrets and variables > Actions`):

-   `PYPI_API_TOKEN`: Your API token for publishing the Python SDK to PyPI.
-   `NPM_TOKEN`: Your authentication token for publishing the Node.js SDK to NPM.
-   `HF_TOKEN`: Your Hugging Face Hub token with `write` permissions to the target repository.

These secrets are used by the `publish-sdks` and `publish-to-hf` jobs.

---

## Programmatic Endpoint Management

This repository includes a powerful Python script to manage your Inference Endpoints programmatically using the `huggingface_hub` library.

### `scripts/manage_endpoints.py`

This script is a command-line tool that allows you to create, list, inspect, pause, resume, and delete endpoints.

**Usage:**

```bash
# Get help
python scripts/manage_endpoints.py --help

# List all your endpoints
python scripts/manage_endpoints.py list

# Create a new endpoint
python scripts/manage_endpoints.py create my-new-endpoint --repo "gpt2"

# Delete an endpoint
python scripts/manage_endpoints.py delete my-new-endpoint
```

### Automated Deployment in CI/CD

The main CI/CD workflow (`.github/workflows/ci-cd.yml`) includes a `deploy-to-endpoint` job. When a new version tag is pushed, this job automatically runs the `manage_endpoints.py create` command to deploy the new model version to a dedicated Inference Endpoint.

This creates a seamless "GitOps" workflow for your model deployments.
