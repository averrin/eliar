"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from django_any import any_model
from dev_tools.models import ToDo

class TodoTest(TestCase):
    def test_do_done(self):
        todo = any_model(ToDo)
        todo.do_done()

        self.assertEquals(True, ToDo.objects.get(pk=todo.id).done)

    def test_del(self):
        todo = any_model(ToDo)
        id = todo.id
        todo.delete()
        self.assertEquals(0, ToDo.objects.filter(pk=id).count())

