from django.urls import path
from . import views
from users.views import CustomLoginView

urlpatterns= [    
    path("",  CustomLoginView.as_view(), name='login'), ##login funcion
    path("registro/", views.registro, name='registro'),
]