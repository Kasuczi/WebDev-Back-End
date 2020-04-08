from django.contrib.auth.models import User


class MyAuthBackend:
    def authenticate(self, request, username=None, password=None):
        print(username, password)
        try:
            user = User.objects.get(email=username)
            return user if user.check_password(password) else None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

