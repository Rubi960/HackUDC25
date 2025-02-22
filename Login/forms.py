from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):
    username = forms.CharField(required=True, 
                               label="Usuario",
                               widget=forms.TextInput(attrs={'class': 'input-centrado form-control', 'placeholder': 'Usuario'})
    )
    email = forms.EmailField(required=True, label="Email",
                               widget=forms.TextInput(attrs={'class': 'input-centrado form-control', 'placeholder': 'Email'})
    )
    first_name = forms.CharField(required=True, label="Nombre",
                               widget=forms.TextInput(attrs={'class': 'input-centrado form-control', 'placeholder': 'Nombre'})
    )
    password1 = forms.CharField(    
        widget=forms.PasswordInput(attrs={'class': 'input-centrado form-control', 'placeholder': 'Password'}),
        label="Contraseña",
        help_text='<ul><li>La contraseña debe tener como mínimo 8 caracteres</li><li>La contraseña no puede ser solo numérica</li><li>La contraseña no puede ser muy común</li></ul>',
    )
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-centrado form-control', 'placeholder': 'Re-enter Password'}), label="Contraseña")

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "password1", "password2"]
