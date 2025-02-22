from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .utils import get_project_docs

class DocumentationView(View):
    """Vista para generar documentación dinámica de todas las funciones y clases del proyecto Django."""

    def get(self, request, *args, **kwargs):
        docs = get_project_docs()
        return render(request, "docs/docs.html", {"docs": docs})

