from django.db import models

# Create your models here.

class Link(models.Model):
    title = models.CharField(max_length=500, blank=True)
    url = models.URLField()

    def __unicode__(self):
        return self.url


class Wall(models.Model):
    wall_text = models.TextField()

