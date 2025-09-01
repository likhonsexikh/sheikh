# Build stage
FROM ubuntu:22.04 AS builder

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /build
COPY runtime/ ./runtime/
RUN cd runtime && make build

# Runtime stage
FROM ubuntu:22.04 AS runtime

RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/* \
    && useradd -m -s /bin/bash sheikh

WORKDIR /app

# Copy model and runtime
COPY model/sheikh.gguf ./
COPY model/tokenizer.json ./
COPY model/metadata.json ./
COPY --from=builder /build/runtime/sheikh ./

# Copy examples
COPY examples/ ./examples/

RUN chown -R sheikh:sheikh /app
USER sheikh

EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8080/health || exit 1

CMD ["./sheikh", "--model", "sheikh.gguf", "--server", "--host", "0.0.0.0", "--port", "8080"]
