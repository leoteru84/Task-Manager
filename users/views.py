from django.shortcuts import render
from .forms import RegistroForm, CustomAuthenticationForm
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from . import views


# Create your views here.
def login(request):
    return render(request, 'login.html')


def registro(request):
    form= RegistroForm
    return render(request, 'registro.html',{'form': form})



class CustomLoginView(LoginView):
    template_name = "login.html"
    authentication_form = CustomAuthenticationForm