from .models import *


def get_task():
    tasks = Task.objects.all()
    return tasks