from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend, ModelBackend
from django.contrib.auth.models import User


class EmailBackend(ModelBackend):

    def authenticate(self, request, email=None, password=None, *kwargs):
        try:
            user = User.objects.get(email=email)
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        user_model = get_user_model()
        try:
            return user_model.objects.get(pk=user_id)
        except user_model.DoesNotExist:
            return None
