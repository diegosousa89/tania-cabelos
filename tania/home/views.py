from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'index.html')  

def login(request):
    return render(request, 'login-user-admin.html')  

def perfil_adm(request):
    return render(request, 'pagina-admin.html') 

def perfil_cliente(request):
    return render(request, 'perfil-cliente.html')

def agenda_cliente(request):
    return render(request, 'agenda-cliente.html')

def agenda_admin(request):
    return render(request, 'agenda-admin.html')