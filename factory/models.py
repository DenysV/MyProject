from django.db import models
import datetime

class Tarea(models.Model):
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    project = models.ForeignKey('Project', on_delete = models.SET_NULL, null = True)
    name = models.CharField(max_length = 200)
    deadline = models.DateField(default = datetime.date.today)
    duration = models.IntegerField(default = 0)

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
