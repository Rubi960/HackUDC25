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

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, models
from .forms import RegisterForm

# Create your views here.
def homepage(request):
    """
    Extracts docstrings from functions and classes in a Python source code file, ignoring imported modules.
    
    Input: HttpRequest - Http request object
    Output: HttpResponse - Http response with rendered template
    """
    context={}
    return render(request, 'login/base.html', context)

def login_view(request):
    """
    Handle user login.

    If the request method is POST, it attempts to authenticate the user using the provided 
    email and password. If authentication is successful, the user is logged in and redirected 
    to the homepage. If authentication fails, the user is logged out and an error message is 
    displayed.

    Input: HttpRequest - The HTTP request object containing user credentials.

    Output: HttpResponse - The rendered login page with or without an error message.
    """
    
    if request.method=="POST":
        email=request.POST.get("email")
        passwd=request.POST.get("passwd")
        user = authenticate(username=email, password=passwd)
        if user is not None:
            login(request, user)
            context = {}
            return redirect('/chat')
        logout(request=request)
        context={'error':'El usuario introducido no es correcto'}
        return render(request,'login/base.html', context)
    return render(request,'login/base.html', {})

def register(request):
    """
    Handle user registration.

    If the request method is POST, it attempts to create a new user from the provided email, username and password. If the email is not in use, the user is created and logged in. If the email is in use, an error message is displayed. If the request is not a POST request, the registration form is rendered.

    Input: HttpRequest - The HTTP request object containing user credentials.   
    Output: HttpResponse - The rendered registration page with or without an error message
    """
    form=RegisterForm()

    if request.method == 'POST':
        form=RegisterForm(request.POST)
        if form.is_valid():          
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password1']

            client = models.User.objects

            if not client.filter(email=email).exists():
                form.save()
                user = authenticate(username=username, password=password)
                if user is not None:
                    context = {}
                    login(request, user)
                    return redirect('/chat')
                else:
                    return redirect('/register')
            else:
                form.add_error('email', 'El email no es válido.')

    context={'form':form}
    return render(request, 'login/register.html', context)

def logout_view(request):
    """
    Logs out the user and redirects them to the homepage.

    Input: HttpRequest - The HTTP request object for the logout request.
    Output: HttpResponse - A redirection response to the homepage.
    """
    logout(request)
    return redirect('/')

def csrf_failure(request, reason=""):
    """
    Handles CSRF failure by rendering the CSRF failure template.

    Input: HttpRequest - The HTTP request object that triggered the CSRF failure.
           reason - A string explaining why the CSRF validation failed.
    Output: HttpResponse - A rendered page explaining the CSRF failure.
    """
    return render(request, 'login/csrf.html', {})
