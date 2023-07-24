from uuid import uuid4

from django.db import models
from django.conf import settings

from .manager import (
    TaskManager
)

class Task(models.Model):
    """Model for tasks."""
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    objects = TaskManager()

    def __str__(self) -> str:
        return self.title