"""
MIT License

Copyright (c) 2025 HackNCheese

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import os
import ast
from django.apps import apps
from django.conf import settings

def get_project_docs():
    """
    Gets DocStrings from all apps in the project.

    Input: None
    Output: Dictionary
    """
    project_docs = {}

    base_dir = settings.BASE_DIR

    for app_config in apps.get_app_configs():
        app_name = app_config.name

        if app_name.startswith("django.") or "site-packages" in app_config.path:
            continue

        app_docs = {}
        app_path = app_config.path

        for root, _, files in os.walk(app_path):
            for file in files:
                if file.endswith(".py") and file not in ["__init__.py", "apps.py", "tests.py", "migrations", "0002_history_session.py", "0001_initial.py", "0003_alter_history_history.py", "0004_alter_history_history.py"]:
                    file_path = os.path.join(root, file)
                    module_name = os.path.splitext(file)[0]

                    with open(file_path, "r", encoding="utf-8") as f:
                        source = f.read()

                    module_docs = extract_docstrings(source)

                    if module_docs:
                        app_docs[module_name] = module_docs

        if app_docs:
            project_docs[app_name] = app_docs

    return project_docs

def extract_docstrings(source_code):
    """
    Extracts DocStrings from functions and classes in a Python source code file, ignoring imported modules.

    Input: String
    Output: Dictionary
    """
    tree = ast.parse(source_code)
    docs = {}

    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):  # Solo funciones y clases
            docstring = ast.get_docstring(node) or "No documentation available"
            definition, description = split_docstring(docstring)
            docs[node.name] = {"type": "function", "definition": definition, "description": description}

    return docs

def split_docstring(docstring):
    """
    Splits a DocString into its definition and description.

    Input: String
    Output: Tuple
    """
    if not docstring or not isinstance(docstring, str):
        return "No definition available", "No additional details provided."

    lines = docstring.strip().split("\n", 1)  # Dividimos en dos partes
    description = lines[0].strip() if lines[0].strip() else "No definition available"
    definition = lines[1].strip() if len(lines) > 1 and lines[1].strip() else "No additional details provided."

    return definition, description



