#!/bin/sh

echo'Waiting for postgres...'
python manage.py collectstatic --noinput --settings=vehiculares.settings.production



echo 'Migrating...'
python manage.py wait_for_db --settings=vehiculares.settings.production
python manage.py migrate --settings=vehiculares.settings.production

echo 'Running server...'
gunicorn --env DJANGO_SETTINGS_MODULE=vehiculares.settings.production vehiculares.wsgi:application --bind 0.0.0.0:8000



