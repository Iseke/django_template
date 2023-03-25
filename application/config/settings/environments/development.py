import datetime

from config.settings.components.common import DEFAULT_APPS, MIDDLEWARE, SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "*",
]

# Application definition

EXTRA_APPS = [
    'rest_framework',
    'rest_framework_simplejwt',
    'debug_toolbar',
    'django_extensions',
    'django_migration_linter',
]

LOCAL_APPS = [
    'users',
    'posts',
]

INSTALLED_APPS = DEFAULT_APPS + EXTRA_APPS + LOCAL_APPS

# Development tools

# Django debug toolbar
# https://django-debug-toolbar.readthedocs.io

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'config.settings.utils.django_toolbar._custom_show_toolbar',
}

MIDDLEWARE = [y for i, x in enumerate(MIDDLEWARE) for y in (
    ('debug_toolbar.middleware.DebugToolbarMiddleware', x) if MIDDLEWARE[i-1] == \
    'django.contrib.auth.middleware.AuthenticationMiddleware' else (x, ))]

CORS_ALLOW_ALL_ORIGINS = True

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DATETIME_FORMAT': "%Y-%m-%dT%H:%M",
    'TIME_FORMAT': "%H:%M",
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20,
}

# JWT settings
JWT_AUTH = {
    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=60 * 60 * 24 * 30),
}

REST_USE_JWT = True

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=7),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=7),
    'UPDATE_LAST_LOGIN': True,
    'AUTH_HEADER_TYPES': ('JWT', 'jwt'),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
}
