import os
import ast
from django.apps import apps
from django.conf import settings

def get_project_docs():
    """Recopila los docstrings de cada archivo Python en las apps del proyecto, ignorando funciones importadas."""
    project_docs = {}

    # Directorio base del proyecto
    base_dir = settings.BASE_DIR

    for app_config in apps.get_app_configs():
        app_name = app_config.name

        # Excluir aplicaciones de Django y paquetes de terceros
        if app_name.startswith("django.") or "site-packages" in app_config.path:
            continue

        app_docs = {}
        app_path = app_config.path  # Ruta de la app

        # Recorrer archivos .py dentro de la aplicación
        for root, _, files in os.walk(app_path):
            for file in files:
                if file.endswith(".py") and file not in ["__init__.py", "apps.py", "tests.py", "migrations"]:
                    file_path = os.path.join(root, file)
                    module_name = os.path.splitext(file)[0]

                    with open(file_path, "r", encoding="utf-8") as f:
                        source = f.read()

                    # Analizar el código fuente para extraer docstrings
                    module_docs = extract_docstrings(source)

                    if module_docs:
                        app_docs[module_name] = module_docs

        if app_docs:
            project_docs[app_name] = app_docs

    return project_docs

def extract_docstrings(source_code):
    """Extrae docstrings de clases y funciones en un archivo fuente, ignorando las importadas."""
    tree = ast.parse(source_code)
    docs = {}

    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):  # Solo funciones y clases
            docstring = ast.get_docstring(node) or "No documentation available"
            docs[node.name] = docstring  # Guardamos nombre y docstring

    return docs



