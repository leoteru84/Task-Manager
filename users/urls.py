from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns= [    
    path("",  CustomLoginView.as_view(), name='login'),
    path("registro/", views.registro, name='registro'),
]