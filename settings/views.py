from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import UserUpdateForm

# Create your views here.
@login_required(login_url="/", redirect_field_name=None)
def settings(request):   
    """
    Render and process the settings page for logged-in users.

    Handles both profile updates and password changes submitted via POST requests. If the request method is POST, it processes the update profile or update password actions based on the presence of specific keys in the POST data. Valid profile updates or password changes are saved, and appropriate success messages are displayed. If validation fails, error messages are shown.

    The function also renders the settings page with pre-filled forms when the request method is GET.

    Input: request (HttpRequest) - The HTTP request object containing method and user data.

    Output: HttpResponse - The rendered settings page with user update and password change forms, or redirects to the login page with success/error messages.
    """

    if request.method == "POST":
        user_update_form = UserUpdateForm(request.POST)
        password_form = PasswordChangeForm(request.user, request.POST)
        user = request.user
                        
        if 'update_profile' in request.POST:  
            if user_update_form.is_valid():
                cleaned_data = user_update_form.cleaned_data

                if cleaned_data.get('first_name') not in ['', None]:
                    user.first_name = cleaned_data['first_name']
                if cleaned_data.get('email') not in ['', None]:
                    user.email = cleaned_data['email']

                user.save()
                messages.success(request, "Tu perfil ha sido actualizado correctamente.")
                return redirect('login')
            else:
                messages.error(request, "Error al actualizar el perfil. Revisa los datos.")

        elif 'update_password' in request.POST:  
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user) 
                messages.success(request, "Tu contraseña ha sido cambiada exitosamente.")
                return redirect('login')
            else:
                messages.error(request, "Error al cambiar la contraseña. Verifica los datos.")

    else:
        user_update_form = UserUpdateForm(instance=request.user)
        password_form = PasswordChangeForm(request.user)

    return render(request, "settings/settings.html", {
        'user_update_form': user_update_form,
        'password_form': password_form,
    })