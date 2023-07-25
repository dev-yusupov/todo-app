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
def create_user(**params):
    return get_user_model().objects.create_user(**params)

def detail_url(task_id):
    return reverse('todo:task-detail', args=[task_id])

"""Create and return a task"""
def create_task(user, **params):
    payload = {
        'title': 'Test1',
        'description': 'Test description',
    }

    payload.update(**params)
    task = Task.objects.create(user=user, **payload)
    return task

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
        self.user = create_user(email='test1@test.com', password='1234test')
        self.client = APIClient()
        self.client.force_authenticate(self.user)
    
    def test_retrieve_tasks(self):
        """Test retrieves list of tasks."""
        create_task(user=self.user, title='Test1')
        create_task(user=self.user, title='Task2')

        response = self.client.get(TASK_URL)

        tasks = Task.objects.order_by('-id')
        serializer = TaskSerializer(tasks, many=True)
        # print(response.data)
        # print(serializer.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
    
    def test_task_list_limited_to_users(self):
        """Test """
        other_user = create_user(
            email="other@test.com",
            password="other1234",
        )
        create_task(user=other_user, title="Test1")
        create_task(user=self.user, title="Test2")

        response = self.client.get(TASK_URL)

        tasks = Task.objects.filter(user=self.user)
        serializer = TaskSerializer(tasks, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
    
    def test_get_task_detail(self):
        """Test retrieves details of task."""
        task = create_task(user=self.user)

        url = detail_url(task.id)
        response = self.client.get(url)

        serializer = TaskSerializer(response)

        print(response.data)
        print(serializer.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data, serializer.data)