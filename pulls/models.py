from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)


class Task(models.Model):
    status = models.CharField(max_length=20, blank=True)
    task_name = models.CharField(max_length=50)
    data = models.DateField()

    User_id = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True)
