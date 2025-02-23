# HackUDC25

## :scroll: [Licencia](LICENSE)

Este proyecto está licenciado bajo la MIT License.  

Sin embargo, este proyecto utiliza PyTorch, que está sujeto a su propia licencia.  
Puedes revisar la licencia de PyTorch aquí: [https://github.com/pytorch/pytorch/blob/main/LICENSE](https://github.com/pytorch/pytorch/blob/main/LICENSE).

## :crystal_ball: [Manage.py](manage.py)
It serves the same function as django-admin and sets the DJANGO_SETTINGS_MODULE environment variable to point to the project's settings.py file. This tool uses the [Manage.py](manage.py) definition.

The following commands are available:
* `python3 manage.py makemigrations`: Creating new migrations based on the changes made to the models.
* `python3 manage.py migrate`: Applying and unapplying migrations 
* `python3 manage.py runserver`: Runs the server by default on `127.0.0.1:8000`.

Example of how to deploy:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
