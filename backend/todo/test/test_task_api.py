from django.test import TestCase
from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from todo.models.task.model import Task
from todo.serializers.task.serializer import TaskSerializer

TASK_URL = reverse('todo:task-list')

"""Create custom user for test."""
def create_user(email, password, **extra_fields):
    return get_user_model().objects.create_user(email, password, **extra_fields)

"""Create and return a task"""
def create_task(title, **extra_fields):
    return Task.objects.create_task(title, **extra_fields)

class PublicTaskAPITests(TestCase):
    """Test cases for unauthorized users."""
    def setUp(self) -> None:
        self.client = APIClient()
    
    def test_retrieve_task_unavailable_for_unaothorized_user(self):
        """Test retrieves list of tasks but returns 401 unAuthorized status code."""
        response = self.client.get(TASK_URL)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    

class PrivateTasksAPITests(TestCase):
    """Test cases for authenticated users."""
    def setUp(self):
        self.user = create_user(email='test@test.com', password='1234test')
        self.client = APIClient
        self.client.force_authenticate(self.user)
    
    def test_retrieve_tasks(self):
        """Test retrieves list of tasks."""
        create_task('Task1', user=self.user)
        create_task('Task2', user=self.user)

        response = self.client.get(TASK_URL)

        tasks = Task.objects.order_by('-user')
        serializer = TaskSerializer(tasks, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
    
    def test_task_list_limited_to_users(self):
        """Test """
        other_user = create_user(
            email="other@test.com",
            password="other1234",
        )
        create_task(user=other_user)
        create_task(user=self.user)

        response = self.client.get(TASK_URL)

        recipes = Task.objects.filter(user=self.user)
        serializer = TaskSerializer(recipes, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)