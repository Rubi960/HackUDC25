import random

from django.http import JsonResponse
from django.shortcuts import render

from .models import Chat, Session
from .assistant import Assistant


# Create your views here.
def index(request):
    assistant = Assistant(request.user)
    return render(request, 'chat/chat.html', context=dict(assistant=assistant))


def response(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        assistant: Assistant = request.POST.get('assistant', '')
        answer = assistant.answer(message)
        new_chat = Chat(message=message, response=answer)
        new_chat.save()
        return JsonResponse({'response': answer})
    return JsonResponse({'response': 'Invalid request'}, status=400)

def terminate(request):
    if request.method == 'POST':
        assistant: Assistant = request.POST.get('assistant', '')
        new_session = Session(summary=assistant.summary(), user=request.user)
        new_session.save()
        del assistant
        return JsonResponse({'response': f'Session {new_session.id} terminated'})
    return JsonResponse({'response': 'Invalid request'}, status=400)
