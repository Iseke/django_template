from django.urls import path, include

# Register your views here.

from .views import HumanView, RobotView

app_name = 'core'

urlpatterns = [
    path('robots.txt', RobotView.as_view(), name='robots_txt'),
    path('humans.txt', HumanView.as_view(), name='humans_txt'),
]
