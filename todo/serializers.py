from rest_framework import serializers
from todo.models import Todo, TodoList


class TodoSerializer(serializers.ModelSerializer):
    """"Serializer pour change les objects du model en json et vise versa"""

    class Meta:
        model = Todo
        fields = '__all__'


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = '__all__'

