from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import *
from .models import *

# Create your views here.
#GET
class ListTodo(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
#PUT
class DetailTodo(generics.RetrieveUpdateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
#POST
class CreateTodo(generics.ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
#DELETE
class DeleteTodo(generics.DestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
