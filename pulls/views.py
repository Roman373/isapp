from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.list import ListView

from pulls.models import Task


class ExitPage(View):
    def get(self, request):
        context = {}
        return render(request, 'exit.html', context=context)


class MainPage(View):
    def get(self, request):
        context = {}
        return render(request, 'index.html', context=context)


class AddPage(View):
    def get(self, request):
        context = {Task.objects.all()}
        return render(request, 'add.html', context=context)


class TasksView(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'tasks'