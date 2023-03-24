from config.settings.components.common import DEFAULT_APPS

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    environ.get('DOMAIN_NAME'),
    'localhost',
]

# Application definition

EXTRA_APPS = []

LOCALE_APPS = []

INSTALLED_APPS = DEFAULT_APPS + EXTRA_APPS + LOCALE_APPS
