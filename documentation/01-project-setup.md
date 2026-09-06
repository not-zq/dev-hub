
# Setting up a new project

- [Github repository](#github-repository)
- [Python environment](#python-environment)
    - [Create the base environment](#create-the-base-environment)
    - [Install packages](#install-packages)
    - [Load environment variables](#load-environment-variables)
- [Setting up for web development with Python](#setting-up-for-web-development-with-python)
    - [Initializing the project](#initializing-the-project)
    - [Including HTML templates and static files](#including-html-templates-and-static-files-like-css-and-js)
    - [Connect to SQL database](#connect-to-sql-database)

## GitHub repository

In [GitHub](https://github.com), create a repository for the project. 
This will create a web URL for the project, `https://github.com/<user>/<project-name>.git`.

Locally, create a folder for the project and create `README.md` and `.gitignore` files. 
It is suggested to have projects in a common memorable place like `C:\Projects\<project-name>`.

To initialize the repository locally and add the connection to the remote repository, in a terminal, run

```bash
git init
git branch -M main
git remote add origin https://github.com/<user>/<project-name>.git
```

Then, generally, you stage changes, commit and push them as

```bash
git add README.md
git add .gitignore
git commit -m "add README.md and .gitignore"
git push -u origin main
```

## Python environment

### Create the base environment

In a terminal, in the project's folder, to create a local environment for the project, run

```bash
python -m venv .venv
```

To link this new environment to the current **VS Code** workspace, we use the shortcut `Ctrl + Shift + P` and find the command `Python: Select Interpreter`. After running this command, we select our local environment interpreter `./.venv/Scripts/python.exe` for the workspace. 

Now, for python files, our local environment is selected as the interpreter, having the necessary packages. To manually activate the environment in a terminal we run

```bash
.venv/Scripts/activate
```

### Install packages

To install packages you can run `pip install <package>`.
However, it is better practice to set a `requirements.txt` file with the needed packages to keep track of the installed packages and for other to be able to recreate the same environment. The content for the `requirements.txt` file should look like following
```
pandas
pyodbc==5.3.0
matplotlib
pyyaml
```
where you can specify the version of the package. 

Having this file set up with the necessary packages, to install them you would instead run
```bash
python -m pip install -r requirements.txt
```

Finally, to confirm the installation, you can print a list of the installed packages in the active environment with
```bash
python -m pip list
```

### Load environment variables

Whenever you need environment variables for you code, let it be for credentials or for a configuration based on where your code runs, you create a `.env` file which, for your repository, should be added to the `.gitignore` as it might have sensible information or it is not necessarily reusable, and instead a `.env.sample` should be included with default values or no values depending on the field, like
```ini
# .env.sample

DB_SERVER="homeserver"
DB_DATABASE="local"
DB_UID=""
DB_PWD=""
```
The convention is to use all uppercase for the variables names.

The variables from this `.env` file can be loaded using the `load_dotenv()` function from the `dotenv` library which can be installed through `pip` from `python-dotenv`.

Then, to access the environment variables you can use the `os.getenv(<environment-variable>)` function.

## Setting up for web development with Python

It is suggested that a separate folder is created for the web app, such as `C:\Projects\<project>\django-app`. This folder will end up having a similar structure to the following
```
django_app
├── .venv/
├── app/
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── config/ 
│   ├── settings.py
│   └── urls.py
│── static/
│   ├── css/
│   ├── images/
│   └── js/
├── templates/
│   └── home.html
├── manage.py
└── requirements.txt
```

The project will need an environment with the `django` package, which to verify the installation of, you can run the following in a terminal
```bash
django-admin --version
```
which should return a version, like `6.0.6`.

### Initializing the project

Being in the target folder for the web app, while having the environment activated, we can run
```bash
django-admin startproject config .
```
which will create a `manage.py` file and a `config` folder with other necessary files. After this, we can already run the server using 
```bash
python manage.py runserver
```
which will start the Django welcome page in `http://127.0.0.1:8000/`, but we can skip this part to continue setting up our project.

Now, we can create an app using this command 
```bash
python manage.py startapp app
```
which will create an `app` folder with files we will use to set up our page. 

First, we need to register the app by adding its name to the `INSTALLED_APPS` list in `config/settings.py`
```Python
INSTALLED_APPS = [..., "app"]
```

Then, we create a view for the app in `app/views.py`, for example
```Python
from django.http import HttpResponse
def home(request):
    return HttpResponse("Hello World")
```

We set the URL to the application's view by adding it to `app/urls.py`, like so
```Python
from django.urls import path
from .views import home
urlpatterns = [path("", home)]
```
and include these URLs to `config/urls.py`
```Python
from django.urls import include, path
urlpatterns = [path("", include("app.urls"))]
```

### Including HTML templates and static files like CSS and JS

Typically, HTML files are stored as templates. For this example, we'll use the file `templates/home.html`. For this file to be considered, first we add it to our `TEMPLATES` list in `config/settings.py`
```Python
TEMPLATES = [
    {
        ...
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
    }
]
```
and then, we can render by modifying the app's view (`app/views.py`) like follows
```Python
from django.shortcuts import render
def home(request):
    return render(request, "home.html")
```

Now, CSS and JS files are considered static files, which we'll consider them to be in a `css` and `js` folders inside a `static` folder. For these folders to be considered we have to modify the following in `config/settings.py`
```Python
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
```

Then to call these files in the HTML file, we would have like to the following
```HTML
{% load static %}

<!DOCTYPE html >
<html>
<head>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
    ...
</head>
<body>
    ...
    <script src="{% static 'js/script.js' %}"></script>
</body>
</html>
```

### Connect to SQL database

For MS SQL databases it is necessary to install the `mssql-django` package.

First we include the database in the `config/settings.py` file
```Python
DATABASES = {
    "default" : {
        "ENGINE": "mssql",
        "NAME": "Local",
        "HOST": "localhost",
        "OPTIONS": {
            "driver": "ODBC Driver 17 for SQL Server",
            "trusted_connection": "yes",
        }
    }
}
```

Then we can let Django generate a model by running 
```bash
python manage.py inspectdb <table>
```
in the terminal, which will print the model we can then paste in `app/models.py`. The model will have this structure 
```Python
from django.db import models
class <table>(models.Model):
    # attributes definition ...
    class Meta:
            managed = False
            db_table = "<table>"
```
where the table from the database is a class we can call, and the attributes are defined as variables.

In the view we import the class from the model 
```Python
.models import <table>
```
and fetch data using Django's ORM (Object-Relational Mapper).
