# tasks/forms.py

from django import forms
from .models import Task, Project, Category, Priority, Tag

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed', 'category', 'assigned_to', 'due_date', 'project', 'priority', 'tags']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'user']

class PriorityForm(forms.ModelForm):
    class Meta:
        model = Priority
        fields = ['level']

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']