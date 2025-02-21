import inspect
import pkgutil
import importlib
from django.apps import apps

def get_project_docs():
    """Recopila los docstrings de todas las funciones y clases de las apps instaladas en Django."""
    project_docs = {}

    # Iterar sobre todas las apps instaladas
    for app_config in apps.get_app_configs():
        app_name = app_config.name
        project_docs[app_name] = {}

        # Obtener todas las rutas de módulos dentro de la app
        app_path = app_config.path
        for _, module_name, _ in pkgutil.iter_modules([app_path]):
            full_module_name = f"{app_name}.{module_name}"
            try:
                module = importlib.import_module(full_module_name)

                # Extraer funciones y clases con docstring
                module_docs = {}
                for name, obj in inspect.getmembers(module):
                    if inspect.isfunction(obj) or inspect.isclass(obj):
                        docstring = inspect.getdoc(obj) or "No documentation available"
                        module_docs[name] = docstring

                if module_docs:
                    project_docs[app_name][module_name] = module_docs

            except Exception as e:
                project_docs[app_name][module_name] = {"error": str(e)}

    return project_docs
