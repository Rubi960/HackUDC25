"""
MIT License

Copyright (c) 2025 HackNCheese

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

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
