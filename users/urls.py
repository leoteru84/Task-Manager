from django.urls import path
from . import views
from users.views import CustomLoginView, dashboard, registro

urlpatterns= [    
    path("",  CustomLoginView.as_view(), name='login'), ##login funcion
    path("registro/", registro, name='registro'),
    path("dashboard/", dashboard, name='dashboard'),
]