# TerapIA

Repository created to solve the HackUDC25 challenges. 

Made by **HackNCheese**:
- Ana Xiangning Pereira Ezquerro
- Pablo Juncal Moreira
- Rodrigo Naranjo González
- Rubén Diz Martínez

## :scroll: [License](LICENSE)

This project is licensed under the MIT License.  

However, this project uses PyTorch, which is subject to its own license.  
You can review the PyTorch license here: [https://github.com/pytorch/pytorch/blob/main/LICENSE](https://github.com/pytorch/pytorch/blob/main/LICENSE).

## :crystal_ball: Requirements

1. It is recommended to create a virtual environment.

```sh
python -m venv venv
```

2. Next run:

```sh
source venv/bin/activate 
```

3. Then install the model and the requirements.

```shell
curl -fsSL https://ollama.com/install.sh | sh
ollama pull deepseek-r1:32b
pip install -r requirements.txt
```

> [!CAUTION]
> The `deepseek-r1:32b` model is **very heavy**. Check your disk space and memory before downloading.

## :computer: Usage ([Manage.py](manage.py))

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


## :file_folder: Folder Structure

```
.
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── HackUDC25
│   ├── settings.py
│   └── urls.py
├── LICENSE
├── Login
│   ├── forms.py
│   ├── models.py
│   ├── templates
│   ├── urls.py
│   └── views.py
├── README.md
├── SECURITY.md
├── aboutme
│   ├── models.py
│   ├── profiler.py
│   ├── templates
│   ├── urls.py
│   └── views.py
├── admintab
│   ├── templates
│   ├── urls.py
│   └── views.py
├── chat
│   ├── assistant.py
│   ├── models.py
│   ├── templates
│   ├── urls.py
│   └── views.py
├── docs
│   ├── templates
│   ├── urls.py
│   ├── utils.py
│   └── views.py
├── manage.py
├── requirements.txt
├── settings
│   ├── forms.py
│   ├── models.py
│   ├── templates
│   ├── urls.py
│   └── views.py
├── static
│   ├── css
│   ├── img
│   └── javascript
└── templates
    ├── base.html
    └── chat.html
```

### Root Files
- **`CODE_OF_CONDUCT.md`** – Defines the expected behavior for contributors and users.
- **`CONTRIBUTING.md`** – Provides guidelines on how to contribute to the project.
- **`LICENSE`** – Specifies the legal terms under which the project can be used.
- **`README.md`** – Offers an overview of the project, including its contents and usage.
- **`SECURITY.md`** – Includes security policies and procedures for handling vulnerabilities.
- **`manage.py`** – The command-line utility for managing the Django project.
- **`requirements.txt`** – Lists the dependencies required for the project.

### Main Django Application (`HackUDC25`)
- **`settings.py`** – Configuration file for the Django project, including database and middleware settings.
- **`urls.py`** – Defines the URL patterns for routing requests.

### Applications

Each subdirectory represents a Django app within the project:

#### `Login`
Handles user authentication and login/register functionality.
- **`forms.py`** – Defines form structures for authentication.
- **`models.py`** – Contains database models related to authentication.
- **`templates/`** – Stores HTML templates related to login.
- **`urls.py`** – Defines routes for login-related views.
- **`views.py`** – Contains the logic for handling login requests.

#### `aboutme`

Psychological profile of the user.

- **`models.py`** – Defines database structures for user profiles.
- **`profiler.py`** – Helper module for profile-related operations.
- **`templates/`** – Stores HTML templates for profile pages.
- **`urls.py`** – Routes requests related to profiles.
- **`views.py`** – Handles profile-related logic.

#### `admintab`

Manages administrator-related functionalities.

- **`templates/`** – Stores HTML templates for the admin dashboard.
- **`urls.py`** – Routes admin-related requests.
- **`views.py`** – Handles admin dashboard functionalities.

#### `chat`
Handles real-time chat and psicological assistant functionalities.
- **`assistant.py`** – AI assistant logic file.
- **`models.py`** – Defines database structures for messages and conversations.
- **`templates/`** – Stores chat-related HTML templates.
- **`urls.py`** – Routes chat-related requests.
- **`views.py`** – Contains logic for handling chat interactions.

#### `docs`
Manages documentation-related features.
- **`templates/`** – Stores HTML templates for documentation pages.
- **`urls.py`** – Routes documentation-related requests.
- **`utils.py`** – Utility functions for processing documentation.
- **`views.py`** – Handles logic related to documentation.

#### `settings`
Manages user and application settings.
- **`forms.py`** – Defines forms related to user information.
- **`models.py`** – Stores settings-related database models.
- **`templates/`** – Stores HTML templates for settings pages.
- **`urls.py`** – Routes settings-related requests.
- **`views.py`** – Handles user settings management.

### Static Files (`static/`)
Stores static assets like stylesheets, images, and JavaScript files.
- **`css/`** – Contains CSS files for styling.
- **`img/`** – Stores images used in the application.
- **`javascript/`** – Holds JavaScript files for frontend interactions.

### Templates (`templates/`)
Houses shared HTML templates.
- **`base.html`** – The main layout template for the project.
- **`chat.html`** – Specific template for the chat support functionality.
