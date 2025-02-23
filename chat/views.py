
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .models import Chat, Session, History
from .assistant import Assistant


def index(request):
    """
    View for the main chat page. Obtains the chat history associated with the current user and resets it when accessing the page. Renders the 'chat/chat.html' template.
    Input: request - The request object containing the current user's information.
    Output: HttpResponse - The rendered template for the chat page.
    """
    history, created = History.objects.get_or_create(
        user=request.user,
        defaults={'first_name': request.user.first_name, 'history': ''}
    )
    history.history = []
    history.save()
    return render(request, 'chat/chat.html', context={'history':history})


def response(request):
    """
    View for handling user responses. Handles POST requests, retrieves the user's message, calls the assistant, saves the chat, and returns the assistant's response.
    Input: request - The request object containing the user's message.
    Output: JsonResponse - The assistant's response.
    """

    if request.method == 'POST':
        message = request.POST.get('message', '')
        answer = Assistant(request.user).answer(message)
        new_chat = Chat(message=message, response=answer)
        new_chat.save() 
        return JsonResponse({'response': answer})
    return JsonResponse({'response': 'Invalid request'}, status=400)

def terminate(request):
    """
    View for terminating user sessions. Handles POST requests, calls the assistant to generate a summary of the session, saves the session, and redirects to the 'index' view.
    Input: request - The request object containing the current user's information.
    Output: JsonResponse - A response indicating the termination of the session.
    """
    if request.method == 'POST':
        assistant = Assistant(request.user)
        if len(assistant.info) > 1:
            print('Calling assistant summary')
            new_session = Session(summary=assistant.summary(), user=request.user)
            print('Ended summary')
            new_session.save()
        return JsonResponse({'response': 'Session terminated'}, status=200)
    return JsonResponse({'response': 'Invalid request'}, status=400)
