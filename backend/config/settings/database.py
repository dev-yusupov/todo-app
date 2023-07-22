"""
Database settings
"""

from config.settings.base import *


DATABASES = {
    # Master database
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'database/master.sqlite3',
    }
}
