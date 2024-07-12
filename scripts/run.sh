#!/bin/sh

set -e

python manage.py wait_for_db    #.sh $DJANGO_DB_HOST
python manage.py collectstatic --noinput
python manage.py migrate

uwsgi --ini uwsgi.ini