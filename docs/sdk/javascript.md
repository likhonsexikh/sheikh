# JavaScript (Browser) SDK Documentation

This page provides documentation for using Sheikh LLM directly in the browser.

*(Note: This is a placeholder. A browser-specific SDK build would be required.)*

## Integration

To use Sheikh LLM in a web application, you would typically include the browser build of the SDK and then interact with the Sheikh API running on your server.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Sheikh LLM Browser Example</title>
    <script src="path/to/sheikh-sdk.browser.js"></script>
</head>
<body>
    <h1>Sheikh LLM Browser Demo</h1>
    <button id="generateBtn">Generate Text</button>
    <pre id="output"></pre>

    <script>
        const client = new Sheikh.Client({ host: 'http://localhost:8080' });

        document.getElementById('generateBtn').addEventListener('click', async () => {
            const outputElement = document.getElementById('output');
            outputElement.textContent = 'Generating...';

            try {
                const response = await client.generate({
                    prompt: "Explain the benefits of edge computing in 50 words."
                });
                outputElement.textContent = response.text;
            } catch (error) {
                outputElement.textContent = 'Error: ' + error.message;
            }
        });
    </script>
</body>
</html>
```

## Source Code

The source code for the JavaScript SDK can be found in the [`/sdk/javascript`](../../sdk/javascript/) directory of the repository.
