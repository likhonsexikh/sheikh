# Node.js SDK Documentation

This page provides documentation for the `sheikh-sdk` NPM package.

For a detailed, auto-generated API reference, please see the [API Reference](../api_reference.md#nodejs-sdk) page.

## Installation

```bash
npm install sheikh-sdk
```

## Basic Usage

```javascript
const { Sheikh } = require('sheikh-sdk');

async function main() {
    // Connect to a running Sheikh server
    const client = new Sheikh({ host: 'localhost', port: 8080 });

    // Generate text
    const response = await client.generate({
        prompt: "Generate a JavaScript function to check for a palindrome.",
        maxTokens: 150
    });

    console.log(response);
}

main();
```

## Source Code

The source code for the Node.js SDK can be found in the [`/sdk/node`](../../sdk/node/) directory of the repository.
