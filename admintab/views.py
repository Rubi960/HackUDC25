from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def es_admin(user):
    """
    Checks if the given user has superuser status.

    Input: user - The user object to check.
    Output: bool - True if the user is a superuser, False otherwise.
    """
    return user.is_superuser

# Create your views here.
@user_passes_test(es_admin, login_url='/login/')
def admin_view(request):
    """
    View for the admin tab in the navigation bar.

    Input: request - The request object containing the current user's information.
    Output: HttpResponse - The rendered template for the admin tab.

    This view is only accessible if the user is authenticated and has superuser status.
    """
    return render(request, "admintab/admin.html")