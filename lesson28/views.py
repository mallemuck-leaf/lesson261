from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import LoginForm

from django.http import HttpResponse

# Create your views here.


def task_page(request):
    content = {
        'tasks': Task.objects.all(),
    }
    return render(request, 'lesson28/tasks.html', content)


def show_task(request, task_id):
    task_item = Task.objects.filter(id=task_id)

    content = {
        'tasks': task_item,
    }
    return render(request, 'lesson28/task.html', content)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Вход выполнен успешно.')
                else:
                    return HttpResponse('Учетная запись отключена.')
            else:
                return HttpResponse('Неверная учетная запись.')
    else:
        form = LoginForm()
    return render(request, 'lesson28/login.html', {'form': form})


@login_required
def dashboard(request):
    return render(request,
                  'lesson28/dashboard.html',
                  {'section': 'dashboard'})
