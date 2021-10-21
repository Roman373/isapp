from .models import *


def get_task(user_id):
    tasks = Task.objects.filter(User_id=user_id)
    return tasks


def autoriz(login, password):
    users = User.objects.filter(login=login, password=password)
    return users
