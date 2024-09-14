from django.db import models

# Create your models here


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField()
    time = models.TimeField(blank=True, null=True)
    google_calendar_id = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title
