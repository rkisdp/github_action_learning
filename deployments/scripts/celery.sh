#!/bin/bash
set -e
echo "===Initiating Celery==="
celery -A portfolio_backend_django.celery worker -l info

echo "===Start Celery Beat==="
celery -A portfolio_backend_django.celery beat -l info