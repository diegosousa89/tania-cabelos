from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # A URL '' (vazia) chama a função 'home' em views.py
    path('agenda-admin.html', views.agenda_admin, name='agenda_admin'),
    path('agenda-cliente.html', views.agenda_cliente, name='agenda_cliente'),
    path('perfil-admin.html', views.perfil_adm, name='perfil_adm'), 
    path('perfil-cliente.html', views.perfil_cliente, name='perfil_cliente'),
    path('login-user-admin.html', views.login, name='login'),
  

]