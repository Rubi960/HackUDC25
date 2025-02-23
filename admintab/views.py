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

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
import matplotlib.pyplot as plt
import os, base64

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

    # Leer las imágenes SVG desde static y codificarlas en Base64
    """
    View to render the admin tab in the navigation bar.

    Input: request - The request object containing the current user's information.
    Output: HttpResponse - The rendered template for the admin tab.

    This view reads the SVG images from the static directory and encodes them in Base64.
    The encoded strings are passed to the template as context variables.
    """

    images = [
        'img/bigfive.svg',
        'img/enneagram.svg',
        'img/mbti.svg',
    ]

    images_base64 = []
    for image in images:
        with open(os.path.join('static', image), "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            images_base64.append(encoded_string)

    # Pasar el contexto con la gráfica y las imágenes al template
    context = {
        'imagen1_base64': images_base64[0],
        'imagen2_base64': images_base64[1],
        'imagen3_base64': images_base64[2],
    }
    return render(request, 'admintab/admin.html', context)