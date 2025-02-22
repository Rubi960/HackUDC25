import random

from django.http import JsonResponse
from django.shortcuts import render

from .models import Analysis


# Create your views here.
def index(request):
    return render(request, 'aboutme/aboutme.html')


def analyze(request):
    if request.method == 'POST':
        option = request.POST.get('option', '')

        #completion = client.chat.completions.create(
        #    model="gpt-4o",
        #    messages=[
        #        {"role": "system", "content": "You are a helpful assistant."},
        #        {"role": "user", "content": message}
        #    ]
        #)
        placeholder = [
            f"Analysis {option} run,"
        ]

        answer = random.choice(placeholder)
        new_chat = Analysis(option=option, result=answer)
        new_chat.save()
        return JsonResponse({'result': answer})
    return JsonResponse({'result': 'Invalid request'}, status=400)
