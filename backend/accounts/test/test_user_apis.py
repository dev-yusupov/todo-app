import jwt

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient
from rest_framework import status

from .utils import create_jwt_token

TOKEN_URL = reverse('accounts:login')

class PublicUserTests(TestCase):
    """Test cases for unauthenticated."""
    def setUp(self):
        self.client = APIClient()
    
    def test_user_token(self):
        user = get_user_model().objects.create_user(email="test@test.com", password="12345test")

        payload = {
            'email': 'test@test.com',
            'password': '12345test',
        }

        response = self.client.post(TOKEN_URL, payload)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('refresh', response.data)
        self.assertIn('access', response.data)