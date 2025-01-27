from django.test import TestCase

from rest_framework.test import APITestCase
from rest_framework import status
from .models import Task

class TaskAPITestCase(APITestCase):
    def test_create_task(self):
        data = {
            "title": "Test Task",
            "description": "This is a test",
            "status": "pending",
            "due_date": "2025-01-15",
        }
        response = self.client.post('/api/tasks/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
