from django.urls import path
from .views import index, analyze

urlpatterns = [
    path('', index, name='index'),
    path('analyze', analyze, name='analyze'),
]