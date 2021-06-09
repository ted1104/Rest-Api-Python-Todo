from django.db import models


# Create your models here.
class Todo(models.Model):
    """class pour la liste todo"""
    title = models.CharField(max_length=255)
    due_date = models.DateField()
    completed = models.BooleanField()
    favorite = models.BooleanField()
    id_list = models.ForeignKey('TodoList', null=False, on_delete=models.CASCADE)


class TodoList(models.Model):
    """Liste de toDo"""
    name = models.CharField(max_length=255)

