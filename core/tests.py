from django.test import TestCase
from django.urls import reverse
from .models import ToDoList


class AddNewTodoTestCase(TestCase):
    def test_add_todo_success(self):
        data = {"text": "Покормить кота"}
        url = reverse("add-todo")
        response = self.client.post(path=url, data=data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertIn("text", response.json())
        self.assertEqual(response.json().get("text"), "Покормить кота")
        self.assertIn("url", response.json())
        self.assertTrue(response.json()["url"] > 0)
        
    
    def test_add_todo_fail(self):
        data = {"blabla": "Покормить кота"}
        url = reverse("add-todo")
        response = self.client.post(path=url, data=data, format="json")
        self.assertEqual(response.status_code, 400)
        


class AddToDoToListTestCase(TestCase):
    # def setUp(self):
    #     todo_list = ToDoList.objects.last()
    #     url = todo_list.url
    #     self.data = {"text": "Прочитать 3 книги"}
    #     self.url = reverse("add-todo-to-list", kwagrs={"url": url})
    #     self.response = self.client.post(
    #         path=self.url,
    #         data=self.data,
    #         format="json"
    #     )

    def test_add_todo_to_list_success(self):
        data = {"text": "Покормить кота"}
        url = reverse("add-todo")
        response = self.client.post(path=url, data=data, format="json")
        todo_list_url = response.json()["url"]

        self.data = {"text": "Прочитать 3 книги"}
        self.url = reverse("add-todo-to-list", kwargs={"url": todo_list_url})
        self.response = self.client.post(
            path=self.url,
            data=self.data,
            format="json"
        )

        self.assertEqual(self.response.status_code, 201)
        self.assertEqual(self.response.json()["text"], "Прочитать 3 книги")
    
    # def test_add_todo_to_list_fail(self):
