from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import *

router = routers.DefaultRouter()
router.register(r'users', HomeViewSet)
router.register(r'todo', ToDoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', AddTodoView.as_view(), name="add-todo"),
    path("todolist/<int:url>/", TodoAPIView.as_view(), name="todo-api"),
    path("todolist/add/<int:url>/", AddTodoToListView.as_view(), name="add-todo-to-list"),
    path("todolist/<int:url>/set_code/", ToDoListSetPasswordView.as_view(), name="todolist-set-password"),
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += router.urls