import random

from django.http import JsonResponse
from django.shortcuts import render

from .models import Chat


# Create your views here.
def index(request):
    return render(request, 'chat/chat.html')


def response(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')

        #completion = client.chat.completions.create(
        #    model="gpt-4o",
        #    messages=[
        #        {"role": "system", "content": "You are a helpful assistant."},
        #        {"role": "user", "content": message}
        #    ]
        #)
        placeholder = [
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ac tamen hic mallet non dolere. Quod quidem iam fit etiam in Academia. Cum id fugiunt, re eadem defendunt, quae Peripatetici, verba. Eam tum adesse, cum dolor omnis absit; Nam bonum ex quo appellatum sit, nescio, praepositum ex eo credo, quod praeponatur aliis. Si stante, hoc natura videlicet vult, salvam esse se, quod concedimus; "
        ]

        answer = random.choice(placeholder)
        new_chat = Chat(message=message, response=answer)
        new_chat.save()
        return JsonResponse({'response': answer})
    return JsonResponse({'response': 'Invalid request'}, status=400)
