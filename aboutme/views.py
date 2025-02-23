import random

from django.http import JsonResponse
from django.shortcuts import render

from .models import Analysis
from .profiler import Profiler

# Create your views here.
def index(request):
    """
        Vista que renderiza la página principal del análisis.
    """
    return render(request, 'aboutme/aboutme.html')


def analyze(request):
    """
        Vista que procesa la solicitud de análisis
        - Recibe el tipo de análisis que se desea realizar
        - Ejecuta el Profiler para obtener el análisis del usuario
        - Muestra por pantalla el análisis
    """
    if request.method == 'POST':
        option = request.POST.get('option', '')
        answer = Profiler(request.user).analysis(option)
        new_chat = Analysis(option=option, result=answer)
        new_chat.save()
        return JsonResponse({'result': answer})
    return JsonResponse({'result': 'Invalid request'}, status=400)
