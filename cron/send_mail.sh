#!/bin/sh

WORKON_HOME=/home/sitcomyk
PROJECT_ROOT=/home/sitcomyk/sitco
# activate virtual environment
. $WORKON_HOME/virtual/bin/activate

cd $PROJECT_ROOT
python server_manage.py send_mail
