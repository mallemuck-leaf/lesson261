from django.shortcuts import render
from .models import Project
from .forms import ProjectForm

# Create your views here.


def hello_page(request):
    if request.method == 'POST':
        Project.objects.create(title=request.POST.get('title'),
                               description=request.POST.get('description'))
        context = {
            'welcome_message': 'Главная страница проектов',
            'projects': Project.objects.all(),
            'form': ProjectForm(),
        }
        return render(request, 'tasks/projects.html', context)

    else:
        context = {
            'welcome_message': 'Главная страница проектов',
            'projects': Project.objects.all(),
            'form': ProjectForm(),
        }
        return render(request, 'tasks/projects.html', context)
