from django.shortcuts import render
from .forms import RegistroForm
from django.http import HttpResponse


# Create your views here.
def login(request):
    return render(request, 'login.html')


def registro(request):
    form= RegistroForm
    return render(request, 'registro.html',{'form': form})