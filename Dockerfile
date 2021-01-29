FROM python:3.8-alpine

RUN apk add --no-cache --virtual builds-deps build-base \
    && apk --no-cache --update add curl git libssl1.1 python3-dev \
                                   musl-dev libffi-dev libressl-dev openssl-dev \
    && pip install pip==19.1.1 \
    && pip install cython \
    && apk del builds-deps build-base \
    && addgroup -S appgroup && adduser -S appuser -G appgroup

ENV PYTHONPATH=/app

RUN apk --no-cache add --update --virtual builds-deps build-base && \
    pip install poetry && \
    apk del builds-deps build-base

COPY pyproject.toml poetry.lock /

RUN apk --no-cache add --update --virtual builds-deps build-base \
    && poetry config virtualenvs.create false \
    && poetry install \
    && apk del builds-deps build-base

COPY ./docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

USER appuser

COPY . /app
WORKDIR /app/

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["help"]
