"""
File to manage project in development section
"""

from config.settings.apps import *
from config.settings.base import *
from config.settings.database import *
from config.settings.internationalization import *

DEBUG = True

ALLOWED_HOSTS = []

CORS_ALLOWED_ORIGINS = [
    'http://localhost:4200'
]

STATIC_URL = '/static/'