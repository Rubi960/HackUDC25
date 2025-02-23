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
