from django.test import TestCase

# Create your tests here.
from .models import Todo


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(title="First Todo", body="my body")

    def test_model_content(self):
        self.assertEqual(self.todo.title, "First Todo")
        self.assertEqual(self.todo.body, "my body")
        self.assertEqual(str(self.todo), "First Todo")
