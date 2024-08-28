# tasks/admin.py

from django.contrib import admin
from .models import Task, Category, Project, Priority, Tag

admin.site.register(Task)
admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Priority)
admin.site.register(Tag)