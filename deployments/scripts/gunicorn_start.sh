#!/bin/bash

NAME="portfolio.backend.django"                   # Name of the application
DJANGODIR=/app                                    # Django project directory
USER=root                                         # the user to run as TODO: change to www-user
GROUP=root                                        # the group to run as
NUM_WORKERS="2"                                   # how many worker processes should Gunicorn spawn
export PYTHONUNBUFFERED="True"                    # Disable stdin/stdout buffering.

echo "Starting $NAME as `whoami`"

cd $DJANGODIR
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn portfolio_backend_django.wsgi:application \
    --bind=0.0.0.0:8000 \
    --user=$USER --group=$GROUP --name=$NAME \
    --workers=$NUM_WORKERS \
    --log-level=info \
    --log-file=/dev/stdout --timeout 30
