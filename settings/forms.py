from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        required=False,
        label="Email",
        widget=forms.TextInput(
            attrs={"class": "input-centrado form-control", "placeholder": "Email"}
        ),
    )
    first_name = forms.CharField(
        required=False,
        label="First Name",
        widget=forms.TextInput(
            attrs={"class": "input-centrado form-control", "placeholder": "First Name"}
        ),
    )

    class Meta:
        model = User
        fields = ["first_name", "email"]


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Old Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "input-centrado form-control",
                "placeholder": "Old password",
                "id": "old_password"
            }
        ),
    )

    new_password1 = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "input-centrado form-control", 
                "placeholder": "Password",
                "id": "new_password1"
            }
        ),
        help_text="""<ul>
            <li>The password must be at least 8 characters long</li>
            <li>The password cannot be only numeric</li>
            <li>The password cannot be very common</li>
            </ul>""",
    )

    new_password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(
            attrs={
                "class": "input-centrado form-control",
                "placeholder": "Re-enter Password",
                "id": "new_password2"
            }
        ),
    )
