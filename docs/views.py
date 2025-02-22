from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .utils import get_project_docs

class DocumentationView(View):
    """
    View for the documentation page.

    Input: request - The request object containing the current user's information.
    Output: HttpResponse - The rendered template for the documentation page.
    """

    def get(self, request, *args, **kwargs):
        docs = get_project_docs()
        return render(request, "docs/docs.html", {"docs": docs})

