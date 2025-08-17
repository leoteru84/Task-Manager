from django import forms


    
class RegistroForm(UserCreationForm):
    birthday = forms.DateField(label="Birthday", widget=forms.SelectDateWidget(years=range(1900, 2024)))
    password1= forms.CharField(label="Password", widget=forms.PasswordInput)
    password2= forms.CharField(label="Password", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['Last_name', 'first_name', 'username', 'email', 'password1', 'password2']