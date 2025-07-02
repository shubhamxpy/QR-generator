"""
WSGI config for qr_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from pathlib import Path
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qr_project.settings')

# This application object is used by the development server
# as well as any WSGI server configured to use this file.
application = get_wsgi_application()

# Use WhiteNoise to serve static files
application = WhiteNoise(
    application,
    root=os.path.join(Path(__file__).resolve().parent.parent, 'staticfiles'),
    prefix='static/',
)

# Add media files
application.add_files(
    os.path.join(Path(__file__).resolve().parent.parent, 'media'),
    prefix='media/'
)
