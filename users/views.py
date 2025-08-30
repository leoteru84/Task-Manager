from django.shortcuts import render, redirect
from .forms import RegistroForm, CustomAuthenticationForm
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from . import views
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.



def registro(request):
    form= RegistroForm()
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cuenta creada. Ahora puedes iniciar sesión.")
            return redirect('login')  # nombre de URL
        else:
            # útil para depurar en consola
           messages.error(request, "Corrige los errores del formulario.")
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})




class CustomLoginView(LoginView):
    template_name = "login.html"
    authentication_form = CustomAuthenticationForm
    
    def form_valid(self, form):
        messages.success(self.request, "✅ Has iniciado sesión exitosamente.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "❌ Usuario o contraseña incorrectos.")
        return super().form_invalid(form)

    
    
@login_required    
def dashboard(request):
     return render(request, 'dashboard.html')
     


