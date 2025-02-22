from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import UserUpdateForm

# Create your views here.
@login_required(login_url="/", redirect_field_name=None)
def settings(request):   
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