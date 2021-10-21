from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseRedirect
from .forms import TaskForm
from django.utils import timezone
from .basa import *


class ExitPage(View):
    def get(self, request):
        context = {}
        return render(request, 'exit.html', context=context)

    def post(self, request):
        login = request.POST.get("login")
        password = request.POST.get("password")
        users = autoriz(login, password)
        if not users:
            context = {
                "message": "Введен не правильный пароль или логин"
            }
            return render(request, 'exit.html', context=context)
        else:
            request.session["id_user"] = users[0].id
            return HttpResponseRedirect('index.html')


class MainPage(View):
    def get(self, request):
        date_today = timezone.now()
        tasks = get_task(request.session['id_user'])
        context = {
            "tasks": tasks,
            "date_today": date_today
        }
        return render(request, 'index.html', context=context)


class AddPage(View):
    def get(self, request):
        date_today = timezone.now()
        user_id = request.session['id_user']
        context = {
            "form": TaskForm,
            "date_today": date_today,
            'user_id': user_id
        }
        return render(request, 'add.html', context=context)

    def post(self, request):
        error = ""

        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                uform = form.save(commit=False)
                uform.status = "Невыполнен"
                uform.User_id_id = request.session['id_user']
                uform.save()
                return redirect('index.html')
            else:
                error = "Ошибка формы"
        else:
            form = TaskForm()
        context = {
            'form': form,
            'error': error
        }
        return render(request, 'add.html', context=context)
