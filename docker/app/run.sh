#!/bin/sh

./manage.py makemigrations
./manage.py collectstatic --noinput
./manage.py migrate --noinput
./manage.py runserver 0.0.0.0:8000
