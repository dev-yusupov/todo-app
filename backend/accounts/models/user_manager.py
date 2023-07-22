from django.contrib.auth.models import (
    BaseUserManager,
)

class UserManager(BaseUserManager):
    """Manager for User model."""
    def create_user(self, email, password=None, **extra_fields):
        """Create a new user."""
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user