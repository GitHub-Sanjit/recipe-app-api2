#!/bin/sh

set -e

./wait-for-db.sh $DJANGO_DB_HOST
python manage.py collectstatic --noinput
python manage.py migrate

uwsgi --socket :9000 --workers 4 --master --enable-threads --module app.wsgi