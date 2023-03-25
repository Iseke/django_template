"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include

# Register your views here.
v1patterns = [
    path("users/", include("users.api.v1.urls")),
    path("posts/", include("posts.api.v1.urls")),
]

apipatterns = [
    path("v1/", include(v1patterns)),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', include('health_check.urls')),
    # local path
    path('', include('config.core.urls')),
    # api
    path("api/", include(apipatterns)),
]

if settings.DEBUG:
    import debug_toolbar
    from django.views import debug

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
        path('', debug.default_urlconf),
    ]
