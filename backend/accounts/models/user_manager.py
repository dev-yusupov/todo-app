from django.contrib.auth.models import (
    BaseUserManager,
)
from django.core.exceptions import ValidationError

class UserManager(BaseUserManager):
    """Manager for User model."""
    def create_user(self, email, password=None, **extra_fields):
        """Create a new user."""
        if not email:
            raise ValueError("User must provide email")
        try:
            user = self.model(
                email=self.normalize_email(email),
                **extra_fields
            )
            user.set_password(password)
            user.save(using=self._db)
            return user
                
        except ValidationError as _:
            print(_)
            return {
                'error': 'There was an error creating a user.'
            }
    
    def create_superuser(self, email, password):
        """Create superuser"""
        try:
            user = self.create_user(email, password)
            user.is_staff = True
            user.is_superuser = True
            user.save(using=self._db)
            return user
        
        except ValidationError as _:
            print(_)