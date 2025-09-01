# API Reference

This section provides a detailed reference for the Sheikh LLM APIs and SDKs.

## Runtime API

The Sheikh runtime can be exposed as an HTTP server. This section documents the available endpoints.

### `POST /generate`

Generates text based on a given prompt.

-   **Method**: `POST`
-   **Endpoint**: `/generate`
-   **Request Body**:
    ```json
    {
      "prompt": "Your prompt here",
      "max_tokens": 100,
      "stream": false
    }
    ```
-   **Success Response (stream=false)**:
    ```json
    {
      "response": "The generated text."
    }
    ```
-   **Success Response (stream=true)**: A stream of Server-Sent Events (SSE).

### `GET /health`

Checks the health of the server.

-   **Method**: `GET`
-   **Endpoint**: `/health`
-   **Success Response**:
    ```json
    {
      "status": "ok"
    }
    ```

## Python SDK

Documentation for the Python SDK (`sheikh-sdk`).

### `Sheikh.load(model_path)`

Loads a local model.

### `model.generate(prompt, max_tokens)`

Generates text.

*(More detailed Python SDK documentation would be auto-generated here by a tool like Sphinx or pdoc.)*

## Node.js SDK

Documentation for the Node.js SDK (`sheikh-sdk`).

### `new Sheikh({ host, port })`

Creates a new client instance.

### `sheikh.generateStream(prompt, options)`

Generates a stream of text.

*(More detailed Node.js SDK documentation would be auto-generated here by a tool like TypeDoc.)*
