from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Tarea(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    completada = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('detalle_tarea', kwargs={'pk': self.pk})


