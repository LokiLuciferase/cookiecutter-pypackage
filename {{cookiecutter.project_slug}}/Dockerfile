FROM ubuntu:jammy

LABEL maintainer="{{cookiecutter.full_name}} <{{cookiecutter.email}}>"
LABEL description="A Docker image for {{cookiecutter.project_name}}"

SHELL ["/bin/bash", "-c"]
ARG DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN --mount=type=cache,target=/var/cache/apt \
    apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-venv \
    make \
    && rm -rf /var/lib/apt/lists/*

# Create a virtual environment
RUN python3 -m venv /opt/venv

# Install Python dependencies
ADD . /opt/{{cookiecutter.project_slug}}
RUN cd /opt/{{cookiecutter.project_slug}} \
    && source /opt/venv/bin/activate \
    && make install
