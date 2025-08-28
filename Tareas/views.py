from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib import messages
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from .models import Tarea



# Create your views here.



class CrearTarea(LoginRequiredMixin,CreateView):
    model = Tarea
    template_name = 'crear_tarea.html'
    fields = ['titulo', 'descripcion', 'completada']
    success_url = '/dashboard/'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        messages.success(self.request, "✅ Tarea creada exitosamente.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "❌ Error al crear la tarea. Corrige los errores del formulario.")
        return super().form_invalid(form)

    


class DetalleTarea(LoginRequiredMixin,DetailView):
    model = Tarea
    template_name = 'detalle_tarea.html'
    context_object_name = 'tarea'

    def get_queryset(self):
        return views.Tarea.objects.filter(usuario=self.request.user)


class ActualizarTarea(LoginRequiredMixin,UpdateView):
    model = Tarea
    template_name = 'actualizar_tarea.html'
    fields = ['titulo', 'descripcion', 'completada']
    success_url = '/dashboard/'

    def get_queryset(self):
        return views.Tarea.objects.filter(usuario=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, "✅ Tarea actualizada exitosamente.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "❌ Error al actualizar la tarea. Corrige los errores del formulario.")
        return super().form_invalid(form)



class EliminarTarea(LoginRequiredMixin,DeleteView):
    model = Tarea
    template_name = 'eliminar_tarea.html'
    success_url = '/dashboard/'

    def get_queryset(self):
        return views.Tarea.objects.filter(usuario=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "✅ Tarea eliminada exitosamente.")
        return super().delete(request, *args, **kwargs)