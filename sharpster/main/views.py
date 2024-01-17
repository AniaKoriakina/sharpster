from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'main/index.html')


def trends(request):
    return render(request, 'main/index.html')


def geography(request):
    return render(request, 'main/index.html')


def skills(request):
    return render(request, 'main/index.html')


def vacancies(request):
    return render(request, 'main/index.html')
