#!/bin/bash
set -e
echo "===Initiating Celery==="
exec celery -A portfolio_backend_django.celery worker -l info

echo "===Start Celery Beat==="
exec celery -A portfolio_backend_django.celery beat -l info