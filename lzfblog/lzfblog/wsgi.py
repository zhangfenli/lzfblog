"""
WSGI config for lzfblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

profile = os.environ.get('TYPE_PROFILE', 'develop')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lzfblog.settings.%s' % profile)

application = get_wsgi_application()
