from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Rota para a página inicial
    path('tasks/', views.task_list, name='task_list'),
    path('task/create/', views.task_create, name='task_create'),
    path('task/<int:task_id>/comment/create/', views.comment_create, name='comment_create'),
    path('projects/', views.project_list, name='project_list'),
    path('project/create/', views.project_create, name='project_create'),
    path('priorities/', views.priority_list, name='priority_list'),
    path('priority/create/', views.priority_create, name='priority_create'),
    path('tags/', views.tag_list, name='tag_list'),
    path('tag/create/', views.tag_create, name='tag_create'),
    path('categories/', views.category_list, name='category_list'),
    path('category/create/', views.category_create, name='category_create'),
]
