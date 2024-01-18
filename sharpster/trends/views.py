from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from .models import Trends


def trends_home(request):
    trends = Trends.objects.all()
    data = {
        'title': 'Востребованность',
        'trends': trends,
    }
    return render(request, 'trends/trends.html', data)


