# Sheikh LLM Release Notes

## Version vX.Y.Z (Placeholder – update your version here)

### 🏆 Highlights
- **Sliding-Window Reasoning**: Enhanced ability to reason over incrementally processed data streams on edge/local devices.
- **Edge Optimization**: Sheikh LLM’s <300MB model ensures efficient performance on resource-constrained environments.
- **Multi-SDK Support**: Official support for both Python and Node.js SDKs for seamless integration into your applications.
- **Dockerized Deployment**: Run Sheikh LLM with a fully featured Docker container for immediate integration.

---

### 🚀 Features
- Lightweight runtime with support for **llama.cpp** backend.
- Pre-trained **GGUF** model included for high-performance inference.
- Cross-platform deployment (Linux/macOS).
- Easy integration with Python and Node.js SDKs.

---

### 📦 Downloads
- **Binary Model File**: [Download Sheikh GGUF Model](PLACEHOLDER-BINARY-LINK)
- **Runtime Executable**: [Download Sheikh Runtime](PLACEHOLDER-RUNTIME-LINK)
- **Docker Image**: [Docker Image on GitHub Container Registry](PLACEHOLDER-DOCKER-IMAGE-LINK)

---

### 🔧 SDK Installation
#### Python SDK
Install via pip:
```bash
pip install sheikh-llm
```

#### Node.js SDK
Install via npm:
```bash
npm install sheikh-llm
```

---

### ⚙️ Upgrade Notes
- For seamless upgrades, ensure compatibility between model files (`.gguf`) and runtime versions.
- If deploying via Docker, pull the latest image using:
  ```bash
  docker pull PLACEHOLDER-DOCKER-IMAGE-LINK
  ```

---

### 🌍 Notes for Edge/Local Devices
- The <300MB model is optimized for low-power devices.
- Ensure at least **4GB** free memory for inference on small devices.
- When running locally, use the `runtime/sheikh` executable for lighter setups:
  ```bash
  ./runtime/sheikh -m ./model/sheikh.gguf
  ```

---

Thank you for using Sheikh LLM! For issues or feature requests, please visit [GitHub Issues](https://github.com/likhonsexikh/sheikh/issues).
