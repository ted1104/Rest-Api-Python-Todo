from datetime import datetime

from django.test import TestCase
from todo.models import Todo, TodoList


# Create your tests here.
class TodoTestCase(TestCase):
    DUMMY_NAME = 'Teddy'

    def setUp(self):
        self.todoList = TodoList()
        self.todoList.name = 'Test new to do list'
        self.todoList.save()

        self.todo = Todo()
        self.todo.title = self.DUMMY_NAME
        self.todo.due_date = datetime.today()
        self.todo.favorite = True
        self.todo.completed = False
        self.todo.id_list = self.todoList
        self.todo.save()

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

        self.assertTrue(nbr_of_todo_after_add == nbr_of_todo_before_add + 1)

    def test_update_to_list(self):
        """update liste"""
        self.assertEqual(self.todo.title, self.DUMMY_NAME)
        self.todo.title = "new title"
        self.todo.save()

        elementChaned = Todo.objects.get(pk=self.todo.pk)

        self.assertEqual(elementChaned.title, 'new title')

    def test_delete_todo(self):
        nbr_to_do_before_delete = Todo.objects.count()
        self.todo.delete()
        nbr_to_do_after_delete = Todo.objects.count()
        self.assertTrue(nbr_to_do_after_delete == nbr_to_do_before_delete - 1)
