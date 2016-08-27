FROM python:alpine
ENV PYTHONUNBUFFERED 1
ENV LIBRARY_PATH=/lib:/usr/lib
ARG USER
ARG UID

COPY requirements.txt /app/
RUN env
RUN apk update && \
    apk add --no-cache sudo vim mc build-base py-pip postgresql-dev zlib-dev jpeg-dev gcc python3-dev && \
    addgroup -g $UID $USER && \
    adduser -D -S -s /bin/sh -G $USER -u $UID $USER && \
    pip install --no-cache-dir -U pip virtualenv distribute && \
    pip install --no-cache-dir -r /app/requirements.txt

USER ${USER}
WORKDIR /app
ENTRYPOINT ["/app/docker/app/run.sh"]
