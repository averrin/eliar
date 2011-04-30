from django.db import models

# Create your models here.

class ToDo(models.Model):
    text = models.CharField(max_length=500, blank=True)
    done = models.BooleanField(default=False)

    def do_done(self):
        if not self.done:
            self.done = True
            self.save()