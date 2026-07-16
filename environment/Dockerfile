FROM python:3.11-slim@sha256:baf89808ec37adeaab83cec287adb4a2afa4a11c1d51e961c7ec737877e61af6

RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

WORKDIR /app

COPY access.log /app/access.log
COPY tests /app/tests

RUN mkdir -p /app/verifier
RUN chmod +x /app/tests/test.sh


# FROM python:3.11-slim@sha256:baf89808ec37adeaab83cec287adb4a2afa4a11c1d51e961c7ec737877e61af6

# RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

# WORKDIR /app

# COPY access.log /app/access.log

# RUN mkdir -p /app/verifier


# FROM python:3.11-slim

# RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

# WORKDIR /app

# COPY access.log /app/access.log



# FROM python:3.11-slim

# RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

# WORKDIR /app

# COPY environment/access.log /app/access.log

# RUN mkdir -p /app/verifier