"""
USER model
"""
from uuid import uuid4
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)

from accounts.models.user_behavior import *
from accounts.models.user_manager import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    """User model."""
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    username = models.CharField(max_length=100)
    email = models.EmailField(blank=False, null=False, unique=True)
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    @property
    def get_email(self):
        return self.email
    
    @property
    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
