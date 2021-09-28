from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class MainPage(View):
    def get(self, request):
        context = {}
        return render(request, 'index.html', context=context)


class AddPage(View):
    def get(self, request):
        context = {}
        return render(request, 'add.html', context=context)
