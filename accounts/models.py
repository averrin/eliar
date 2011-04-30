from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    url = models.URLField("Website", blank=True)
    company = models.CharField(max_length=50, blank=True)
    wall_edited = models.DateField(null=True, blank=True, auto_now=True)
    wall_text = models.TextField()
# Create your models here.

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])