
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .models import Chat, Session, History
from .assistant import Assistant


def index(request):
    """
        Vista que maneja la página principal del chat.
        - Obtiene el historial de chat asociado al usuario actual.
        - Reinicia el historial al acceder a la página.
        - Renderiza la plantilla 'chat/chat.html'.
    """
    history, created = History.objects.get_or_create(
        user=request.user,
        defaults={'first_name': request.user.first_name, 'history': ''}
    )
    history.history = []
    history.save()
    print(request.user.session_set.all())
    return render(request, 'chat/chat.html', context={'history':history})


def response(request):
    """
        Vista que maneja las respuestas del chatbot.
        - Solicitudes POST.
        - Obtiene el mensaje enviado por el usuario.
        - Llama al asistente para obtener una respuesta.
        - Guarda el intercambio en la base de datos.
        - Devuelve la respuesta.
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
        Vista para finalizar la sesión del usuario.
        - Maneja solicitudes POST.
        - Llama al asistente para generar un resumen de la sesión.
        - Guarda la sesión finalizada en la base de datos.
        - Redirige a la vista 'index' tras finalizar.
    """
    if request.method == 'POST':
        print('Calling assistant summary')
        assistant = Assistant(request.user)
        new_session = Session(summary=assistant.summary(), user=request.user)
        print('Ended summary')
        new_session.save()
        del assistant
        return redirect('index')
    return JsonResponse({'response': 'Invalid request'}, status=400)
