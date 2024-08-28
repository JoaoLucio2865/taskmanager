from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/', views.task_list, name='task_list'),
    path('task/create/', views.task_create, name='task_create'),
    path('task/edit/<int:pk>/', views.task_edit, name='task_edit'),
    path('task/delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('projects/', views.project_list, name='project_list'),
    path('project/create/', views.project_create, name='project_create'),
    path('project/edit/<int:pk>/', views.project_edit, name='project_edit'),
    path('project/delete/<int:pk>/', views.project_delete, name='project_delete'),
    path('priority/edit/<int:pk>/', views.priority_edit, name='priority_edit'),
    path('priority/delete/<int:pk>/', views.priority_delete, name='priority_delete'),
    path('priorities/', views.priority_list, name='priority_list'),
    path('priority/create/', views.priority_create, name='priority_create'),
    path('priority/edit/<int:pk>/', views.priority_edit, name='priority_edit'),
    path('priority/delete/<int:pk>/', views.priority_delete, name='priority_delete'), 
    path('tags/', views.tag_list, name='tag_list'),
    path('tag/create/', views.tag_create, name='tag_create'),
    path('tag/edit/<int:pk>/', views.tag_edit, name='tag_edit'),
    path('tag/delete/<int:pk>/', views.tag_delete, name='tag_delete'),
    path('categories/', views.category_list, name='category_list'),
    path('category/create/', views.category_create, name='category_create'),
    path('category/edit/<int:pk>/', views.category_edit, name='category_edit'),
    path('category/delete/<int:pk>/', views.category_delete, name='category_delete'),
]
