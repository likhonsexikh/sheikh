#  Sheikh LLM – Lightweight AI for Structured Documents

**Sheikh** is a compact, high-performance language model designed for on-device inference, optimized for structured documents like XML, MDX, and Markdown. With a footprint under 300MB, it's ideal for edge devices and local development environments.

---

## 🔧 Features

- **Compact Model**: Under 300MB, optimized for ARM and x86 architectures.
- **Structured Document Understanding**: Specializes in XML, MDX, and Markdown.
- **Fast Inference**: Sub-200ms latency per token on mid-tier ARM CPUs.
- **Local Development**: No internet dependency; runs entirely offline.
- **Cross-Platform Support**: Compatible with Linux, macOS, and Windows.

---

## 🚀 Capabilities

Sheikh is designed to handle a variety of tasks related to structured documents.

- Generate XML sitemaps, tables, and structured templates
- Generate MDX content for documentation, blogs, and components
- Convert Markdown to structured XML/MDX formats
- Summarize structured documents
- Extract key-value pairs or data from XML/MDX
- Validate syntax and structure of XML/MDX
- Assist in creating structured documentation workflows
- Provide suggestions for formatting, optimization, and compliance
- **Prototype Intelligence**: Supports multi-step reasoning over small contexts (256–512 tokens), includes sliding window context, syntax-aware validation, and lightweight retrieval augmentation.
- Perform single-turn Q&A on structured documents
- Generate instructional prompts for MDX/XML automation
- Assist in creating reusable templates for structured data
- Provide guidance for versioning and structured document lifecycle
- Integration support for databases, APIs, and retrieval systems
- Security and access control recommendations for structured content
- Deployment guidance for edge devices and local development

## 🧠 Logic Flow

Sheikh agent follows a structured multi-step logic for generating and validating content while remaining fast and memory-efficient for edge devices.

1.  **Receive Input**:
    -   **Type**: structured instruction or XML/MDX prompt
    -   **Example**: "Generate a blog component in MDX with metadata for SEO"
2.  **Preprocessing**:
    -   Tokenize input into ≤512 token window
    -   Validate basic syntax if XML/MDX detected
3.  **Prototype Reasoning**:
    -   Apply sliding window reasoning for multi-step instructions
    -   Use context cache to handle multi-turn logic
    -   Apply lightweight retrieval augmentation if local vector store exists
4.  **Model Inference**:
    -   Load Sheikh GGUF 4-bit model
    -   Run inference via `llama.cpp` or ONNX Runtime
    -   Generate structured output
5.  **Post-processing**:
    -   Validate XML/MDX syntax
    -   Check token limits and trim if necessary
    -   Apply heuristics for style, formatting, and template conformity
6.  **Output**:
    -   Return structured document, completion, or recommendation
    -   Include error/warning metadata if syntax issues detected
7.  **Optional Feedback Loop**:
    -   Accept developer corrections or overrides
    -   Update local context cache for next inference
    -   Prepare instruction tuning samples for micro updates

## ⚙️ Deployment

Sheikh is designed for ultra-lightweight edge deployment.

-   **Edge Devices**:
    -   Raspberry Pi 4 / 8GB
    -   ARM laptops
    -   Apple Silicon M1/M2
    -   Intel/AMD x86 laptops
-   **Memory Requirements**: 500MB peak
-   **Latency Target**: <200ms per token

## 💻 Local Development

Sheikh is fully local dev friendly with Python/Node SDKs.

### Python SDK

```python
# import: "from sheikh_sdk import Sheikh"
# usage:
model = Sheikh.load("model/sheikh.gguf")
response = model.generate("Create XML sitemap for blog")
```

### Node SDK

```javascript
// import: "const { Sheikh } = require('sheikh-sdk')"
// usage:
const model = new Sheikh("model/sheikh.gguf")
const response = await model.generate("Generate MDX table")
```

### Docker Support

```bash
# image: likhonsexikh/sheikh:latest
# usage:
docker run -it --rm -v $(pwd)/model:/app/model likhonsexikh/sheikh ./sheikh --prompt "Generate MDX snippet"
```

---
## Notes
- Designed for ultra-lightweight edge deployment
- Fully local dev friendly with Python/Node SDKs
- Supports CI/CD integration with GitHub Actions for docs and demos
- Extendable for retrieval-augmented reasoning and template generation
