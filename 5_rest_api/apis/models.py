from django.db import models
from django.db.models.fields import BooleanField

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    class Meta:
        db_table = 'task'
        ordering = ['-date_created']

    def __str__(self):
        return self.title