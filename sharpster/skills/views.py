from django.shortcuts import render

from .models import Skills


# Create your views here.

def skills(request):
    skills = Skills.objects.all()
    data = {
        'title': 'Навыки',
        'skills': skills,
    }
    return render(request, 'skills/skills.html', data)
