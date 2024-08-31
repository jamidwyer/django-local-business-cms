#!/bin/sh

set -e

echo "Waiting 5s for postgres"

sleep 5

echo "PostgreSQL probably started"

python manage.py collectstatic --noinput
# python manage.py flush --no-input
python manage.py makemigrations
python manage.py migrate
python manage.py spectacular
gunicorn --config gunicorn_config.py cms.wsgi:application

exec "$@"
