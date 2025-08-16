FROM python:3.13-slim

ARG FASTAPI_HOST
ARG FASTAPI_PORT

ENV FASTAPI_HOST=${FASTAPI_HOST}
ENV FASTAPI_PORT=${FASTAPI_PORT}

RUN pip install --no-cache-dir poetry

WORKDIR /app

COPY pyproject.toml poetry.lock README.md /app/

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY . /app

CMD uvicorn app.src.main:app --host ${FASTAPI_HOST} --port ${FASTAPI_PORT}