FROM python:3.5
ENV PYTHONUNBUFFERED 1
ARG USER
ARG UID

COPY requirements/ /app/requirements

RUN apt-get update && \
    apt-get install -y sudo vim mc postgresql-client python-lxml \
    python-cffi libcairo2 libpango1.0-0 libgdk-pixbuf2.0-0 shared-mime-info && \
    groupadd -g $UID $USER && \
    useradd -m -G sudo,users -s /bin/bash -u $UID -g $USER $USER && \
    usermod -p "" $USER && \
    apt-get autoclean && apt-get -y autoremove && \
    pip install --no-cache-dir -U pip virtualenv distribute && \
    pip install --no-cache-dir -r /app/requirements/local.txt

USER ${USER}
WORKDIR /app
ENTRYPOINT ["/app/docker/app/run.sh"]
