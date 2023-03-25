# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

MEDIA_ROOT = PROJECT_ROOT / 'run' / 'media'
MEDIA_URL = '/media/'

STATIC_ROOT = PROJECT_ROOT / 'run' / 'static'
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    PROJECT_ROOT / 'static',
]

# S3 Storage
# https://django-storages.readthedocs.io
#
# AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')
#
# AWS_LOCATION = environ.get('AWS_LOCATION')
# AWS_STORAGE_BUCKET_NAME = environ.get('AWS_STORAGE_BUCKET_NAME')
#
# AWS_S3_ENDPOINT_URL = environ.get('AWS_S3_ENDPOINT_URL')
# AWS_S3_OBJECT_PARAMETERS = {
#     'CacheControl': 'max-age=86400',
# }
#
# AWS_STATIC_LOCATION = f'{AWS_LOCATION}/static'
# STATICFILES_STORAGE = 'config.core.backends.StaticStorage'
#
# AWS_MEDIA_LOCATION = f'{AWS_LOCATION}/media'
# DEFAULT_FILE_STORAGE = 'config.core.backends.MediaStorage'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': environ.get('DJANGO_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': environ.get('DJANGO_NAME', PROJECT_ROOT / 'run' / 'db.sqlite3'),
        'USER': environ.get('DJANGO_USER', 'db_user'),
        'PASSWORD': environ.get('DJANGO_PASSWORD', 'db_password'),
        'HOST': environ.get('DJANGO_HOST', 'localhost'),
        'PORT': environ.get('DJANGO_PORT', 5432),
        'OPTIONS': json.loads(environ.get('DJANGO_OPTIONS', '{}')),
    }
}
