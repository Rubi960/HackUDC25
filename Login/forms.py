from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):
    username=forms.CharField(required=True, label='Usuario')
    email= forms.EmailField(required=True, label='Email')
    password1=forms.CharField(widget=forms.PasswordInput(),label='Contraseña', 
                              help_text='<div id="errores"><p>La contraseña debe tener como mínimo 8 caracteres</p><p>La contraseña no puede ser solo numérica</p><p>La contraseña no puede ser muy común</p></div>')
    password2=forms.CharField(widget=forms.PasswordInput(),label='Contraseña')
    
    class Meta():
        model = User
        fields = ["username", "password1", "password2"]