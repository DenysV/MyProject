from django.db import models
from django.utils import timezone

class Tarea(models.Model):
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    project = models.ForeignKey('Project', on_delete = models.SET_NULL, null = True)
    name = models.CharField(max_length = 200)
    deadline = models.DateTimeField(default = timezone.now)
    duration = models.CharField(max_length = 20, blank = True, null = True)

    def __str__(self):
        return self.name

    def publish(self):
        self.save()

class Project(models.Model):
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

    def publish(self):
        self.save()
