from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.trends_home, name='trends_home'),
]
