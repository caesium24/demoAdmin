from django.db import models
from datetime import datetime

class admins(models.Model):
    name = models.CharField(max_length=200)
    section = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class ticket(models.Model):
    name = models.ForeignKey(admins, on_delete=models.DO_NOTHING)
    site = models.CharField(max_length=8)
    urgency = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=False)
    date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title