from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.latest_vacancies, name='latest_vacancies'),
]