from django.urls import path
from .views import index, response, terminate

urlpatterns = [
    path('', index, name='index'),
    path('response', response, name='response'),
    path('terminate', terminate, name='terminate'),
]