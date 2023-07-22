from django.test import TestCase
from django.contrib.auth import get_user_model

from accounts.models.user_model import User

class UserTests(TestCase):
    """Test cases for User model."""

    def test_user_create_with_email_successful(self):
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

    def test_new_user_normalized_email(self):
        """Test normalizes user email."""
        sample_emails = [
            ["test1@EXAMPLE.com", "test1@example.com"],
            ["Test2@Example.com", "Test2@example.com"],
            ["TEST3@EXAMPLE.com", "TEST3@example.com"],
            ["test4@example.COM", "test4@example.com"],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email=email, password='1234test')
            self.assertEqual(user.email, expected)
    
    def test_create_user_without_email_raise_error(self):
        """Test raises error if user does not provide email."""
        with self.assertRaises(ValueError):
            user = get_user_model().objects.create_user("", "1234test")
    
    def test_create_superuser(self):
        """Test creates superuser"""
        user = get_user_model().objects.create_superuser(
            "test@admin.com",
            "1234test",
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)