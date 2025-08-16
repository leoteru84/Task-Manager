from django.urls import path
from . import views


urlpatterns = [

    path("Tareas", views.tareas, name="tareas"),
]