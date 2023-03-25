from django.contrib.auth import get_user, get_user_model
from django.utils.deprecation import MiddlewareMixin
from django.utils.functional import SimpleLazyObject
from django.utils.timezone import now
from rest_framework_simplejwt import authentication

User = get_user_model()


class ActivityMiddleware(MiddlewareMixin):
    def process_request(self, request):
        try:
            user = authentication.JWTAuthentication().authenticate(request)
            if user is None:
                user = SimpleLazyObject(lambda: get_user(request))
            else:
                user = user[0]
            User.objects.filter(id=user.id).update(last_activity=now())
            request.user = user
        except Exception:
            pass
