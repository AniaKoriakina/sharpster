from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    # path('trends', views.trends, name="trends"),
    path('geography', views.geography, name="geography"),
    path('skills', views.skills, name="skills"),
    path('vacancies', views.vacancies, name="vacancies"),
]
