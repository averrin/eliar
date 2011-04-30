from django.db import models

class inviteRequest(models.Model):
    email = models.CharField(max_length=50, blank=False)
    about = models.CharField(max_length=1000, blank=False)




