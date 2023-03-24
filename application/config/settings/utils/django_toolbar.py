from django.conf import settings

# Django debug toolbar
# https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html#show-toolbar-callback

def _custom_show_toolbar(request):
    """Only show the debug toolbar to users with the superuser flag."""
    return settings.DEBUG and request.user.is_superuser
