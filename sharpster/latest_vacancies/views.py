from django.shortcuts import render

from .scripts.get_latest_vacancies import get_vacancies


def latest_vacancies(request):
    vacancies = get_vacancies()
    data = {
        'title': 'Последние вакансии',
        'vacancies': vacancies,
    }
    return render(request, 'latest_vacancies/latest_vacancies.html', data)
