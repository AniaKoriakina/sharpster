from django.shortcuts import render

# Create your views here.

from django.shortcuts import render


def geography(request):
    data = {
        'title': 'География',
    }
    return render(request, 'geography/geography.html', data)
