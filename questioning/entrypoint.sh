#!/bin/bash

until python manage.py inspectdb > /dev/null 2>&1;
do
	echo 'waiting for db ...'
	sleep 3
done

python manage.py migrate
python manage.py collectstatic --noinput
exec uwsgi --socket=0.0.0.0:8000 --protocol=http --touch-reload=touch-reload -w questioning.wsgi:application
