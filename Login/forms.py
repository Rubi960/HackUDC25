from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):
    """
    Form for registering a new user with email, username and password.
    
    Input: None
    Output: RegisterForm
    Inherits from UserCreationForm and adds email field.
    """
    username = forms.CharField(required=True, 
                               label="Usuario",
                               widget=forms.TextInput(attrs={'class': 'input-centrado form-control', 'placeholder': 'Username'})
    )
    email = forms.EmailField(required=True, label="Email",
                               widget=forms.TextInput(attrs={'class': 'input-centrado form-control', 'placeholder': 'Email'})
    )
    first_name = forms.CharField(required=True, label="Nombre",
                               widget=forms.TextInput(attrs={'class': 'input-centrado form-control', 'placeholder': 'First name'})
    )
    password1 = forms.CharField(    
        widget=forms.PasswordInput(attrs={'class': 'input-centrado form-control', 'placeholder': 'Password'}),
        label="Contraseña",
        help_text='<ul><li>Passwords must be longer than 8 characters</li><li>Passwords can\'t have only numbers</li><li>Passwords must not be common</li></ul>',
    )
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-centrado form-control', 'placeholder': 'Re-enter Password'}), label="Contraseña")

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "password1", "password2"]
