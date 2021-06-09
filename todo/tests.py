from datetime import datetime

from django.test import TestCase
from todo.models import Todo, TodoList


# Create your tests here.
class TodoTestCase(TestCase):
    def setUp(self):
        self.todoList = TodoList()
        self.todoList.name = 'Test new to do list'
        self.todoList.save()


    def test_create_todo(self):
        # voir combien sont presents dans la db#
        # ajouter un objet dans notre DB#
        # Ajouter un object dans notre DB
        # Valider que le nombre d'object dans notre db a ete incremente de 1

        nbr_of_todo_before_add = Todo.objects.count()
        new_todo = Todo()
        new_todo.title = "Acheter un stylo"
        new_todo.due_date = datetime.today()
        new_todo.favorite = True
        new_todo.completed = True
        new_todo.id_list = self.todoList

        new_todo.save()

        nbr_of_todo_after_add = Todo.objects.count()

        self.assertTrue(nbr_of_todo_after_add == nbr_of_todo_before_add+1)

