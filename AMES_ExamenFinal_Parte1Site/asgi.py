"""
ASGI config for AMES_ExamenFinal_Parte1Site project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AMES_ExamenFinal_Parte1Site.settings')

application = get_asgi_application()
