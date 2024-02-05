FROM python:3.10.0a6-slim-buster

ENV PYTHONUNBUFFERED 1

# Set working directory

WORKDIR /app

# Install dependencies

RUN apk