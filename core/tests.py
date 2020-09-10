from django.test import TestCase
from django.urls import reverse


class AddTodoTestCase(TestCase):
    def test_add_todo_success(self):
        data = {"text": "Покормить кота"}
        url = reverse("add-todo")
        response = self.client.post(path=url, data=data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), data)
        print(response)
    
    def test_add_todo_fail(self):
        data = {"blabla": "Покормить кота"}
        url = reverse("add-todo")
        response = self.client.post(path=url, data=data, format="json")
        self.assertEqual(response.status_code, 400)
        print(response)
