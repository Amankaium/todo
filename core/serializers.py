from django.contrib.auth.models import User
from rest_framework import serializers
from .models import ToDo


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            "url","username", "email", "first_name",
            "last_name", "is_staff"
        ]


class ToDoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['text']