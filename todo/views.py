from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from todo.models import Todo, TodoList
from todo.serializers import TodoSerializer, TodoListSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ['due_date', 'favorite', 'completed']
    search_fields = ['title']


class TodoListViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    permission_classes = (IsAuthenticated,)
