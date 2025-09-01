# Sheikh LLM Release Notes – Version {{VERSION}}

## Highlights
- Compact LLM (<300MB) optimized for edge devices and local development
- Supports XML, MDX, Markdown structured documents
- Fast inference: <200ms per token on ARM/x86/Apple Silicon
- Docker image and SDKs included for rapid deployment

## Features
- Generate structured XML/MDX content
- Convert Markdown to XML/MDX templates
- Syntax validation and formatting checks
- Prototype intelligence with sliding-window reasoning
- Python and Node SDKs for local development
- CI/CD friendly with GitHub Actions integration

## Binaries
- [Model Binary – sheikh.gguf](#)
- [Compiled Runtime – runtime/sheikh](#)
- [Docker Image](#)

## SDK Installation
### Python
```bash
pip install sheikh-sdk
```
### Node
```bash
npm install sheikh-sdk
```

## Upgrade Notes
- Verify SDK compatibility when upgrading
- Check templates/workflows for updates

## Edge & Local Notes
- Supported platforms: ARM, x86, Apple Silicon
- Peak memory usage: ~500MB
- Offline/local inference supported

---

Thank you for using Sheikh LLM! For issues or feature requests, please visit the project's GitHub repository.
