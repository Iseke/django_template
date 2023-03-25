from django.urls import path, include

from rest_framework import routers

from .views import PostViewSet, PostAnalyticsView

router = routers.SimpleRouter()

router.register('', PostViewSet, basename='posts')

urlpatterns = [
    path('analytics/', PostAnalyticsView.as_view()),
    path('', include(router.urls)),
]

