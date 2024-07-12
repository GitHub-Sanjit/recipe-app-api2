#!/bin/sh

set -e

python manage.py wait_for_db    #.sh $DJANGO_DB_HOST
python manage.py collectstatic --noinput
python manage.py migrate

uwsgi --socket :9000 --workers 4 --master --enable-threads --module app.wsgi