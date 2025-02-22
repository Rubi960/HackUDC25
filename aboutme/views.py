import random

from django.http import JsonResponse
from django.shortcuts import render

from .models import Analysis
from .profiler import Profiler

# Create your views here.
def index(request):
    return render(request, 'aboutme/aboutme.html')


def analyze(request):
    if request.method == 'POST':
        option = request.POST.get('option', '')
        profiler = Profiler(request.user)
        
        # [PENDING]

        placeholder = [
            f"Analysis {option} run,"
        ]

        answer = random.choice(placeholder)
        new_chat = Analysis(option=option, result=answer)
        new_chat.save()
        return JsonResponse({'result': answer})
    return JsonResponse({'result': 'Invalid request'}, status=400)
