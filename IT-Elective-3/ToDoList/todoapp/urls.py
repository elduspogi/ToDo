from django.urls import path
from .views import *

urlpatterns = [
    path('todo-list/<int:pk>/', DetailTodo.as_view()),
    path('todo-list/', ListTodo.as_view()),
    path('todo-list/create/', CreateTodo.as_view()),
    path('todo-list/delete/<int:pk>/', DeleteTodo.as_view()),
]