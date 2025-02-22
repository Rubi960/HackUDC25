from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'email']  # Solo permitimos cambiar estos campos

class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User