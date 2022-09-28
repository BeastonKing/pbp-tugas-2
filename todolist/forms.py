from django.forms import ModelForm
from django import forms
from todolist.models import Task
class TaskForm(ModelForm):
    title = forms.CharField()
    description = forms.CharField()

    class Meta:
        model = Task
        fields = ['title', 'description']