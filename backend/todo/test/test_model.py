from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

from todo.models.task.model import (
    Task,
)

def create_user(email='test@test.com', password='1234test'):
    return get_user_model().objects.create_user(email, password)

class TodoTests(TestCase):
    """Test cases for Task model."""
    def test_create_task(self):
        user = get_user_model().objects.create_user(
            email='test@test.com',
            password='1234test',
        )
        payload = {
            'title': 'Test todo',
            'description': 'Test description',
        }
        task = Task.objects.create_task(
            user = user,
            **payload
        )
        
        self.assertEqual(str(task), payload['title'])