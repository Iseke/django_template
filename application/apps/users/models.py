"""Users models."""

from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import FileExtensionValidator

from users.managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    confirm_email = models.BooleanField(default=False)
    try_login_count = models.IntegerField(default=0)
    deactivated_date = models.DateField(blank=True, null=True)
    last_activity = models.DateTimeField(null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return str(f"{self.first_name} {self.last_name} ({self.email})")

    @property
    def username(self):
        return str(f"{self.first_name} {self.last_name}")
