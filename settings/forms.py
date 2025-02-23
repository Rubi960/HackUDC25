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

from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User


class UserUpdateForm(forms.ModelForm):
    """
    Form for updating user profile.
    Input: forms.ModelForm - The parent class to inherit from.
    Output: UserUpdateForm - The form with custom fields.
    """
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
    """
    Subclass of PasswordChangeForm with custom fields.
    Input: PasswordChangeForm - The parent class to inherit from.
    Output: CustomPasswordChangeForm - The subclass with custom fields.
    """
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
