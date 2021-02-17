from django.urls import path
from todo_app import views 

app_name = 'todo_app'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('to-do/', views.todolist, name='todolist'),
    path('delete/<task_id>', views.delete_task, name='delete_task'),
    path('complete_task/<task_id>', views.complete_task, name='complete_task'),
    path('pending_task/<task_id>', views.pending_task, name='pending_task'),
    path('edit/<task_id>', views.edit_task, name='edit_task'),


]