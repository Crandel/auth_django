FROM python:2.7-wheezy
ENV PYTHONUNBUFFERED 1

RUN mkdir /opt/code && mkdir /opt/env && \
    apt-get update && \
    apt-get install -y apt-utils && \
    apt-get install -y openssh-server sudo && \
    echo 'root:root' |chpasswd && \
    useradd -m -G sudo,users -s /bin/bash -u 1000 -U crandel && \
    usermod -p "" crandel && \
    mkdir -p /var/run/sshd && \
    apt-get autoclean && apt-get -y autoremove && \
    pip install --no-cache-dir -U pip && \
    pip install --no-cache-dir -U virtualenv && \
    pip install --no-cache-dir -U distribute && \
    echo "source /opt/env/bin/activate\nalias ll='ls -la'" | tee -a /home/crandel/.profile \
          /root/.profile /root/.bashrc /home/crandel/.bashrc && \
    chown -R crandel:crandel /opt

USER crandel

WORKDIR /opt/code
