from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import UserViewSet

router = routers.SimpleRouter()

router.register('', UserViewSet, basename='users')

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='user-login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='user-login-refresh'),
    path('', include(router.urls)),
]




