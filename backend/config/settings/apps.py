"""
Main installed apps in django
"""
from datetime import timedelta

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
    'corsheaders',
    'allauth',
    'allauth.account',
    'dj_rest_auth.registration',
    'drf_spectacular',
]

"""
Project Apps
"""
INSTALLED_APPS += [
    'accounts',
    'todo',
]

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'UPDATE_LAST_LOGIN': True,
}


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

REST_AUTH = {
    'USE_JWT': True,
    'JWT_AUTH_COOKIE': 'auth-cookie',
    'JWT_AUTH_REFRESH_COOKIE': 'auth-cookie-refresh',
}
SITE_ID = 1

CORS_ALLOW_ORIGINS = [
    'http://localhost:4200'
]

CORS_ORIGIN_WHITELIST = (
    'http://localhost:4200',
    'http://localhost:3000',
    'http://localhost'
)

CORS_ALLOW_CREDENTIALS = True