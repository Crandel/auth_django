FROM python
ENV PYTHONUNBUFFERED 1

ADD . /opt

WORKDIR /opt

RUN apt-get update && \
    apt-get install -y apt-utils && \
    apt-get install -y sudo vim && \
    echo 'root:root' |chpasswd && \
    apt-get autoclean && apt-get -y autoremove && \
    pip install --no-cache-dir -U pip && \
    pip install --no-cache-dir -r requirements.txt
