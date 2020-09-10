from django.contrib import admin
from .models import *

@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ["text", "created", "todo_list"]


admin.site.register(ToDoList)

