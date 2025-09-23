from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # A URL '' (vazia) chama a função 'home' em views.py
]