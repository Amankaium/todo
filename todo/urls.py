from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import *

router = routers.DefaultRouter()
router.register(r'users', HomeViewSet)
router.register(r'todo', ToDoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('add/', AddTodoView.as_view(), name="add-todo")
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += router.urls