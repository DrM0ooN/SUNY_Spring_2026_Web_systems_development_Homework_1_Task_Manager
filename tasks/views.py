from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from .models import Task
from .forms import TaskForm, LoginForm


def login_view(request):
    """Handle user login."""
    if request.user.is_authenticated:
        return redirect('task_list')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('task_list')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    
    return render(request, 'tasks/login.html', {'form': form})


@login_required(login_url='login')
def task_list(request):
    """Display incomplete tasks for the logged-in user."""
    tasks = Task.objects.filter(user=request.user, completed=False)
    context = {
        'tasks': tasks,
        'username': request.user.username,
    }
    return render(request, 'tasks/task_list.html', context)


@login_required(login_url='login')
def add_task(request):
    """Add a new task."""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    
    return render(request, 'tasks/add_task.html', {'form': form})


@login_required(login_url='login')
@require_http_methods(["GET", "POST"])
def complete_task(request, task_id):
    """Mark a task as completed."""
    task = get_object_or_404(Task, id=task_id, user=request.user)
    
    if request.method == 'POST' or request.method == 'GET':
        task.completed = True
        task.save()
        return redirect('task_list')
    
    return redirect('task_list')


def logout_view(request):
    """Handle user logout."""
    logout(request)
    return redirect('login')
