from .models import Task
from django.forms import ModelForm, TextInput, DateTimeInput,NumberInput


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'data', 'User_id', 'status']
        widgets = {
            "task_name": TextInput(attrs={
                'id': "myInput",
                'placeholder': "Название..."
            }),
            "data": DateTimeInput(attrs={
                'id': "myDate"

            })
        }
