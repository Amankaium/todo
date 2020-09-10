from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, generics, views
from .serializers import *


class HomeViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoCreateSerializer


class AddTodoView(generics.CreateAPIView):
    serializer_class = ToDoCreateSerializer

    # def post(self, request):
        # super post
        # generate url and create todolist
        # json response with todolist object
    

class SetTodoListCodeView:
    pass



