from django.views.generic import TemplateView

# Create your views here.


class HumanView(TemplateView):
    template_name = 'txt/humans.txt'
    content_type = 'text/plain'


class RobotView(TemplateView):
    template_name = 'txt/robots.txt'
    content_type = 'text/plain'
