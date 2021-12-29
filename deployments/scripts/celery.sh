#!/bin/bash
set -e
echo "===Initiating Celery==="
celery -A portfolio_backend_django.celery worker -l info
