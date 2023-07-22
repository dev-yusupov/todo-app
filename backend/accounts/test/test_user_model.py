from django.test import TestCase

from accounts.models.user_model import User

class UserTests(TestCase):
    """Test cases for User model."""

    def test_user_create(self):
        """Test creates a new user"""
        user = User.objects.create_user(
            email="test1@test.com",
            first_name="Test",
            last_name="Testov",
            password="1234test",
            )
        
        self.assertEqual(user.email, 'test1@test.com')
        self.assertEqual(user.first_name, 'Test')
        self.assertEqual(user.last_name, 'Testov')
        self.assertTrue(user.check_password('1234test'))

