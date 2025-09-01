# Sheikh GitHub App

This GitHub App uses the Sheikh language model to automatically review pull requests that modify structured documents (`.md`, `.xml`, `.mdx`).

## Setup

1.  **Install Dependencies:**
    ```bash
    npm install
    ```

2.  **Configure Environment Variables:**
    Create a `.env` file in this directory and add the following variables. See `.env.example` for details.
    ```
    APP_ID=<your_app_id>
    WEBHOOK_SECRET=<your_webhook_secret>
    PRIVATE_KEY_PATH=./private-key.pem
    SHEIKH_MODEL_ENDPOINT=<your_sheikh_model_endpoint>
    SHEIKH_API_KEY=<your_sheikh_api_key>
    ```

3.  **Register the GitHub App:**
    - Go to your organization or user settings on GitHub and register a new app.
    - Set the webhook URL to `http://<your_domain>:<port>/api/github/webhooks`.
    - Grant the following permissions:
        - `Pull requests`: Read & write
        - `Contents`: Read-only
    - Subscribe to the `pull_request` event.
    - Generate a private key and save it as `private-key.pem` in this directory.

## Running the App

To run the app, use the following command:

```bash
npx probot run ./index.js
```

This will start a server that listens for webhooks from GitHub.
