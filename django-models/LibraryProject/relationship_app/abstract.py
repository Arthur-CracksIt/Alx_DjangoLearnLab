from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

class CustomUser(AbstractBaseUser, AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    bio = models.TextField(blank=True)

class EmailBackend(BaseBackend):
    def authenticate(self, request, username = None, password = None, **kwargs):
        UserModel = get_user_model()
        email = username or kwargs.get('email')
        try:
            user = UserModel.objects.get(email=email)
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None
        return None
        # return super().authenticate(request, username, password, **kwargs)
    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
