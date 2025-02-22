import random

from django.http import JsonResponse
from django.shortcuts import render

from .models import Chat, Session, History, User
from .assistant import Assistant

# Create your views here.
def index(request):
    history, created = History.objects.get_or_create(
        user=request.user,
        defaults={'first_name': request.user.first_name, 'history': ''}
    )
    history.history = []
    history.save()
    return render(request, 'chat/chat.html', context={'history':history})


def response(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        history = History.objects.get(user=request.user)
        history.append({'message':message})
        history.save()

        h = History.objects.get(user=request.user)
        print(h.history)

        answer = "A" # assistant.answer(message)
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
