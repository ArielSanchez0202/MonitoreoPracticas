# autenticacion/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='Correo', max_length=255)
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
