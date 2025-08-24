from django.shortcuts import render, redirect
from .forms import RegistroForm, CustomAuthenticationForm
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from . import views


# Create your views here.



def registro(request):
    form= RegistroForm
    return render(request, 'registro.html',{'form': form})
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login.html')



class CustomLoginView(LoginView):
    template_name = "login.html"
    authentication_form = CustomAuthenticationForm
    
    def dashboard(request):
        if request.user.is_authenticated:
            return redirect('dashboard.html')   
        else:
            return render(request, 'login.html', {'form': form})