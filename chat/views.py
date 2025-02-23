
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .models import Chat, Session, History
from .assistant import Assistant


# Create your views here.
def index(request):
    history, created = History.objects.get_or_create(
        user=request.user,
        defaults={'first_name': request.user.first_name, 'history': ''}
    )
    history.history = []
    history.save()
    print(request.user.session_set.all())
    return render(request, 'chat/chat.html', context={'history':history})


def response(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        answer = Assistant(request.user).answer(message)
        new_chat = Chat(message=message, response=answer)
        new_chat.save() 
        return JsonResponse({'response': answer})
    return JsonResponse({'response': 'Invalid request'}, status=400)

def terminate(request):
    if request.method == 'POST':
        assistant = Assistant(request.user)
        if len(assistant.info) > 1:
            print('Calling assistant summary')
            new_session = Session(summary=assistant.summary(), user=request.user)
            print('Ended summary')
            new_session.save()
        return redirect('')
    return JsonResponse({'response': 'Invalid request'}, status=400)
