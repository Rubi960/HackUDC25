from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def es_admin(user):
    return user.is_superuser

# Create your views here.
@user_passes_test(es_admin, login_url='/login/')
def admin_view(request):
    return render(request, "admintab/admin.html")