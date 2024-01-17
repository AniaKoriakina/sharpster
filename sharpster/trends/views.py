from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def trends_home(request):
    data = {
        'title': 'Востребованность',
    }
    return render(request, 'trends/trends.html', data)
