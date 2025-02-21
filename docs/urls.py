from django.urls import path
from .views import DocumentationView

urlpatterns = [
    path('', DocumentationView.as_view(), name='documentation'),
]
