from random import randint
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, generics, views, status
from rest_framework.response import Response
from .serializers import *
from .models import *


class HomeViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoCreateSerializer


class AddTodoView(generics.CreateAPIView):
    serializer_class = ToDoCreateSerializer

    def post(self, request, *args, **kwargs):
        # generate url and create todolist
        url = randint(1, 10 ** 6)
        while ToDoList.objects.filter(url=url).exists():
            url = randint(1, 10 ** 6)
        todo_list = ToDoList(url=url)
        todo_list.save()

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        todo = serializer.save()
        headers = self.get_success_headers(serializer.data)
        todo.todo_list = todo_list
        todo.save()
        d = serializer.data
        d["url"] = url

        # json response with todolist object
        
        # return super(AddTodoView, self).post(request, *args, **kwargs)
        return Response(d, status=status.HTTP_201_CREATED, headers=headers)

    

class SetTodoListCodeView:
    pass


class TodoAPIView(generics.ListAPIView):
    serializer_class = ToDoSerializer

    def get_queryset(self):
        url = self.kwargs["url"]
        lst = ToDo.objects.filter(todo_list__url=url)
        return lst


class AddTodoToListView(generics.CreateAPIView):
    serializer_class = ToDoCreateSerializer

    def post(self, request, *args, **kwargs):
        url = self.kwargs["url"]
        todo_list = ToDoList.objects.get(url=url)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        todo = serializer.save()
        headers = self.get_success_headers(serializer.data)
        todo.todo_list = todo_list
        todo.save()
        d = serializer.data
        d["url"] = url
        return Response(d, status=status.HTTP_201_CREATED, headers=headers)





