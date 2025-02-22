from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, models
from .forms import RegisterForm

# Create your views here.
def homepage(request):
    context={}
    return render(request, 'login/base.html', context)

def login_view(request):
    if request.method=="POST":
        email=request.POST.get("email")
        passwd=request.POST.get("passwd")
        user = authenticate(username=email, password=passwd)
        if user is not None:
            login(request, user)
            context = {}
            return render(request, 'login/base.html', context) # TODO -> Temporal
        logout(request=request)
        context={'error':'El usuario introducido no es correcto'}
        return render(request,'login/base.html', context)
    return render(request,'login/base.html', {})

def register(request):
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
                    return render(request, 'login/base.html', context) # TODO -> Temporal
                else:
                    return redirect('/register')
            else:
                form.add_error('email', 'El email no es válido.')

    context={'form':form}
    return render(request, 'login/register.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')

def csrf_failure(request, reason=""):
    return render(request, 'login/csrf.html', {})
