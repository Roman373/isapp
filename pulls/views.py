from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.list import ListView
from .forms import TaskForm
from pulls.models import Task
from django.utils import timezone
from .basa import  *


class ExitPage(View):
    def get(self, request):
        context = {}
        return render(request, 'exit.html', context=context)


class MainPage(View):
    def get(self, request):
        date_today = timezone.now()
        tasks = get_task()
        context = {
            "tasks": tasks,
            "date_today": date_today
        }
        return render(request, 'index.html', context=context)

    def Task(self,request):
        form = TaskForm()


class AddPage(View):
    def get(self, request):
        error = ""
        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index.html')
            else:
                error = "Ошибка формы"
        form = TaskForm()
        data = {
            'form': form,
            'error': error
        }
        return render(request, 'add.html',data)