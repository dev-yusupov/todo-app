"""
Server manager file in production
"""

from config.settings.apps import *
from config.settings.base import *
from config.settings.database import *
from config.settings.internationalization import *

DEBUG = False

ALLOWED_HOSTS = [
    '127.0.0.1'
]

STATIC_URL = '/static/'