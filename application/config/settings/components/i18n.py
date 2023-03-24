# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = environ.get('DJANGO_LANGUAGE', 'en')

LANGUAGES = [
    ('en', 'English'),
    ('ru', 'Russian'),
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [
    PROJECT_ROOT / 'locale',
]

MIDDLEWARE = [y for i, x in enumerate(MIDDLEWARE) for y in (
    ('django.middleware.locale.LocaleMiddleware', x) if MIDDLEWARE[i-1] == \
    'django.contrib.sessions.middleware.SessionMiddleware' else (x, ))]
