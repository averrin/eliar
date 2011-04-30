"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""
from django.contrib.auth.models import User

from django_any import any_model
from django.test import TestCase
from accounts.models import UserProfile

class ProfileTest(TestCase):
    def test_autocreation(self):
        user = any_model(User)
        profile = user.profile

        self.assertEquals(1, UserProfile.objects.filter(user=user).count())




