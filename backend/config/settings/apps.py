"""
Main installed apps in django
"""
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

"""
Third-party apps
"""
INSTALLED_APPS += [
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders'
]

"""
Project Apps
"""
INSTALLED_APPS += [
    'accounts',
    'todo',
]