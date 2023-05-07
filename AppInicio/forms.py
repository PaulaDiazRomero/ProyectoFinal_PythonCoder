from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User



class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=50, label="Usuario")
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        