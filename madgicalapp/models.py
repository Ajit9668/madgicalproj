from django.db import models

class Issue(models.Model):
    number = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
    reporter = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    due_date = models.DateTimeField()


