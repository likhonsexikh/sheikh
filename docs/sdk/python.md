# Python SDK Documentation

This page provides documentation for the `sheikh-sdk` Python package.

For a detailed, auto-generated API reference, please see the [API Reference](../api_reference.md#python-sdk) page.

## Installation

```bash
pip install sheikh-sdk
```

## Basic Usage

```python
from sheikh_sdk import Sheikh

# Connect to a running Sheikh server
client = Sheikh(host="localhost", port=8080)

# Generate text
response = client.generate(
    prompt="Generate a Python function to calculate Fibonacci numbers.",
    max_tokens=150
)

print(response)
```

## Source Code

The source code for the Python SDK can be found in the [`/sdk/python`](../../sdk/python/) directory of the repository.
