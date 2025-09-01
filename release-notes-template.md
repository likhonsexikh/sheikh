# Sheikh LLM Release vX.X.X

## ✨ Highlights

-   **Feature 1**: A brief description of the main feature in this release.
-   **Improvement 2**: A summary of a key improvement.
-   **Fix 3**: A note on a critical bug fix.

---

## 🚀 Features

-   **New Feature A**: Detailed description of what this feature does and why it's useful.
-   **New Feature B**: Detailed description of another new capability.
-   **Performance Improvements**: Notes on speed, memory, or efficiency gains.

---

## 📦 Binaries

You can download the pre-compiled binaries for your platform below. The download links are placeholders and will be populated by the release workflow.

| Platform      | Architecture | Download Link                                       |
|---------------|--------------|-----------------------------------------------------|
| Linux         | x86_64       | [sheikh-vX.X.X-linux-amd64.tar.gz](DOWNLOAD_URL_PLACEHOLDER) |
| macOS (Apple) | arm64        | [sheikh-vX.X.X-macos-arm64.tar.gz](DOWNLOAD_URL_PLACEHOLDER) |
| macOS (Intel) | x86_64       | [sheikh-vX.X.X-macos-amd64.tar.gz](DOWNLOAD_URL_PLACEHOLDER) |
| Windows       | x86_64       | [sheikh-vX.X.X-windows-amd64.zip](DOWNLOAD_URL_PLACEHOLDER) |

---

## 🐳 Docker Image

You can pull the latest Docker image from GitHub Packages:

```bash
docker pull ghcr.io/likhonsexikh/sheikh:vX.X.X
```

To run the container:

```bash
docker run -it --rm -v $(pwd)/model:/app/model ghcr.io/likhonsexikh/sheikh:vX.X.X ./sheikh --prompt "Your prompt here"
```

---

## 🛠️ SDK Installation

### Python

```bash
pip install sheikh-sdk --upgrade
```

### Node.js

```bash
npm install sheikh-sdk@latest
```

---

## ⬆️ Upgrade Notes

-   **Breaking Changes**: List any breaking changes that users need to be aware of.
-   **Deprecations**: Mention any features or functions that are now deprecated.
-   **Migration Steps**: Provide instructions for users upgrading from a previous version.

---

Thank you for using Sheikh LLM!
