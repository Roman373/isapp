from django.urls import path, include
from django.contrib import admin
from pulls.views import *
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ExitPage.as_view()),
    path('exit.html', ExitPage.as_view()),
    path('index.html', TasksView.as_view()),
    path('add.html', AddPage.as_view()),
]