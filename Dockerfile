FROM python:2.7-wheezy
ENV PYTHONUNBUFFERED 1
RUN mkdir /opt/code 
RUN apt-get update && apt-get install -y openssh-server
RUN echo 'root:root' |chpasswd
RUN mkdir -p /var/run/sshd
WORKDIR /opt/code
