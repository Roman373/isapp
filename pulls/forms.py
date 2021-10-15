from .models import Task
from django.forms import ModelForm,TextInput,DateTimeInput


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'data']

        widgets = {
            "task_name": TextInput(attrs={
                'id': "myInput",
                'placeholder': "Название..."
            }),
            "data": DateTimeInput(attrs={
                'id': "myDate"
            })
        }
