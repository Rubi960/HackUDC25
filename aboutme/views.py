import random

from django.http import JsonResponse
from django.shortcuts import render

from .models import Analysis
from .profiler import Profiler

# Create your views here.
def index(request):
    """
    View for the aboutme page. Renders the 'aboutme/aboutme.html' template.
    Input: request - The request object containing the current user
    Output: HttpResponse - The rendered template for the aboutme page.
    """
    return render(request, 'aboutme/aboutme.html')


def analyze(request):
    """
    View for handling user analysis requests. Handles POST requests, retrieves the user's analysis option, calls the profiler, saves the analysis, and returns the analysis result.
    Input: request - The request object containing the user's analysis option.
    Output: JsonResponse - The analysis result.
    """
    if request.method == 'POST':
        option = request.POST.get('option', '')
        answer = Profiler(request.user).analysis(option)
        new_chat = Analysis(option=option, result=answer)
        new_chat.save()
        return JsonResponse({'result': answer})
    return JsonResponse({'result': 'Invalid request'}, status=400)
