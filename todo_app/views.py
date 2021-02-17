from django.shortcuts import render, redirect
from django.http import HttpResponse
from todo_app.models import TaskList
from todo_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return render(request, 'frontlist/index.html')

def about(request):
    return render(request, 'frontlist/about.html')

def contact(request):
    return render(request, 'frontlist/contact.html')

def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, ("New Task Added"))
        return redirect('todo_app:todolist')
    else:
        all_tasks = TaskList.objects.all()
        paginator = Paginator(all_tasks, 5)
        page = request.GET.get('pg')
        all_tasks  = paginator.get_page(page) 
        context = {
            'task': all_tasks
        }
    return render(request, 'frontlist/todolist.html', context)

def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.delete()
    return redirect('todo_app:todolist')

def edit_task(request, task_id):
    if request.method == "POST":
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance = task)
        if form.is_valid():
            form.save()
        messages.success(request, ("Task Edited"))
        return redirect('todo_app:todolist')
    else:
        task_obj = TaskList.objects.get(pk=task_id)
        all_tasks = TaskList.objects.all()
        
        context = {
            'task_obj': task_obj, 
            'task': all_tasks
        }
    return render(request, 'frontlist/edit.html', context)

def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = True
    task.save()
    return redirect('todo_app:todolist')

def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = False
    task.save()
    return redirect('todo_app:todolist')