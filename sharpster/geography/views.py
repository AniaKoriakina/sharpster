from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from .models import Geography


def geography(request):
    geography = Geography.objects.all()
    data = {
        'title': 'География',
        'geography': geography,
    }
    return render(request, 'geography/geography.html', data)
