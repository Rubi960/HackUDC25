from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
import matplotlib.pyplot as plt

from io import BytesIO
import base64

def graph_to_file(plot):
    buffer = BytesIO()
    plot.savefig(buffer, format='png',bbox_inches='tight')
    buffer.seek(0)
    image_png=buffer.getvalue()
    graph=base64.b64encode(image_png).decode('utf-8')
    buffer.close()
    plt.clf()
    return graph

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

def your_view(request):
    images = [
        'img/image1.svg',
        'img/image2.svg',
        'img/image3.svg',
    ]

    # Pasa el contexto con las imágenes al template
    return render(request, 'your_app/your_template.html', {'images': images})