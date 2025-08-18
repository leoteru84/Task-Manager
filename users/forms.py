from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

    
class RegistroForm(UserCreationForm):
    birthday = forms.DateField(label="Birthday", widget=forms.SelectDateWidget(years=range(1900, 2025)))
    password1= forms.CharField(label="Password", widget=forms.PasswordInput)
    password2= forms.CharField(label="Password", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'username', 'email', 'password1', 'password2']