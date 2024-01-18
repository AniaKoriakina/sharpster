from django.shortcuts import render
from django.http import HttpResponse

from .models import CSharpProgrammer


# Create your views here.

def index(request):
    main_content = CSharpProgrammer.objects.all()
    data = {
        'title': 'Главная страница',
        'main_content': main_content,
    }
    return render(request, 'main/index.html', data)


def trends(request):
    data = {
        'title': 'Востребованность',
    }
    return render(request, 'main/trends.html', data)


def geography(request):
    return render(request, 'main/index.html')


def skills(request):
    return render(request, 'main/index.html')


def vacancies(request):
    return render(request, 'main/index.html')

