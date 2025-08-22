from django.urls import path, include
from . import views
from users import views as users_views





urlpatterns = [

    path("", views.login, name='login'),
    
]