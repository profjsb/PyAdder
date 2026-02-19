FROM python:3.13-alpine

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN apk add --update gcc g++ \
    && rm -rf /var/cache/apk/*

COPY . /app
WORKDIR /app

RUN uv pip install --system .

CMD tail -f /dev/null
