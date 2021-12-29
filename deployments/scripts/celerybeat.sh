#!/bin/bash
set -e

echo "===Start Celery Beat==="
celery -A portfolio_backend_django.celery beat -l info