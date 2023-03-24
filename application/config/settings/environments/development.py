from config.settings.components.common import DEFAULT_APPS, MIDDLEWARE

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    environ.get('DOMAIN_NAME'),
    'localhost',
    '127.0.0.1',
]

# Application definition

EXTRA_APPS = [
    'debug_toolbar',
    'django_extensions',
    'django_migration_linter',
]

LOCALE_APPS = []

INSTALLED_APPS = DEFAULT_APPS + EXTRA_APPS + LOCALE_APPS

# Development tools

# Django debug toolbar
# https://django-debug-toolbar.readthedocs.io

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'config.settings.utils.django_toolbar._custom_show_toolbar',
}

MIDDLEWARE = [y for i, x in enumerate(MIDDLEWARE) for y in (
    ('debug_toolbar.middleware.DebugToolbarMiddleware', x) if MIDDLEWARE[i-1] == \
    'django.contrib.auth.middleware.AuthenticationMiddleware' else (x, ))]
