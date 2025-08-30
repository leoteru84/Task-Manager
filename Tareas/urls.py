from django.urls import path
from .views import CrearTarea, DetalleTarea, ActualizarTarea, EliminarTarea, ListaTareas
from . import views





urlpatterns = [

    path("", ListaTareas.as_view(), name='tareas'),  # Lista de tareas
    path("crear/", CrearTarea.as_view(), name='crear_tarea'),
    path("detalle/<int:pk>/", DetalleTarea.as_view(), name='detalle_tarea'),
    path("actualizar/<int:pk>/", ActualizarTarea.as_view(), name='actualizar_tarea'),
    path("eliminar/<int:pk>/", EliminarTarea.as_view(), name='eliminar_tarea'),
    
    
]