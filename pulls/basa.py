from .models import *


def get_task():
    user = User.objects.get(id=1)
    tasks = Task.objects.filter(User_id=user)
    return tasks