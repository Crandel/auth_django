#!/bin/bash

sudo /usr/sbin/sshd
# virtualenv /opt/env
. /opt/env/bin/activate
# pip install --no-cache-dir -r requirements.txt
./manage.py migrate
./manage.py runserver 0.0.0.0:8000
