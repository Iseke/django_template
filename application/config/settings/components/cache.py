# Caching
# https://docs.djangoproject.com/en/3.1/topics/cache/

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
}

# Django-axes
# https://django-axes.readthedocs.io/en/latest/4_configuration.html#configuring-caches

AXES_CACHE = 'default'
