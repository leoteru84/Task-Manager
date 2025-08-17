from django.shortcuts import render
from forms import RegistroForm
from django.http import HttpResponse


# Create your views here.
def login(request):
    return HttpResponse(request, '/user/login.html')

def registro(request)  :
    if request.method = 'POST'
    form =RegistroForm(request.POST)
    if form.is_valid():        
        form.save()
        return HttpResponse("Usuario registrado correctamente")
    else:
        return HttpResponse("Error al registrar el usuario")