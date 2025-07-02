#!/bin/bash

# Exit on error
set -o errexit

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate --noinput

# Start Gunicorn
exec gunicorn qr_project.wsgi:application \
    --bind 0.0.0.0:${PORT:-8000} \
    --workers 2 \
    --threads 4 \
    --worker-class gthread \
    --timeout 120 \
    --log-level=info \
    --log-file=-

# Note: The PORT environment variable is provided by Railway
