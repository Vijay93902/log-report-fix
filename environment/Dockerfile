FROM python:3.11-slim@sha256:a8bd2b6e6f6d2d16d9b74d2a7df6c40f6f16f4d537d85b8f7f1e2f4d9c53e8d1

WORKDIR /workspace

RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    coreutils \
    jq \
    && rm -rf /var/lib/apt/lists/*

COPY access.log /workspace/access.log
COPY instruction.md /workspace/instruction.md
COPY tests /workspace/tests

WORKDIR /workspace

CMD ["/bin/bash"]
