
# Web development

## Considerations

### Components

A web page is usually composed of
- **HTML**: structure/content
- **CSS**: appearance/styling
- **JavaScript**: behavior/interactivity

### Structure

Ideally, your web page project folder will be structured as follows
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
│   │   ├── style.css
│   └── js/
│       └── script.js
├── templates/
│   └── home.html
├── manage.py
└── requirements.txt
```

You would want to keep the web app in a separate folder in the project's directory.

## Setting up for web development with Python

### Initialize the project

Being in the web app folder for the project, `C:\Projects\<project>\django-app`, create an environment and install `django`. To verify the installation run
```bash
django-admin --version
```
which should return a version, like `6.0.6`.

To initialize the project run
```bash
django-admin startproject config .
```
which will create the following in your app folder
```
django_app/
├── manage.py
└── config
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

Running
```bash
python manage.py runserver
```
will start the Django welcome page in `http://127.0.0.1:8000/`

### Create an app

Running
```bash
python manage.py startapp app
```
will create the following folder
```
app/
├── migrations/
├── admin.py
├── apps.py
├── models.py
├── test.py
└── views.py
```

To register the app, in `config/setting.py`
```Python
INSTALLED_APPS = [
    ...
    "app",
]
```

Create a view

`app/views.py`
```Python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World")
```

Create URLs

`app/urls.py`
```Python
from django.urls import path
from .views import home

urlpatterns = [
    path("", home),
]
```

Include them in `config/urls.py`:
```Python
from django.urls import include, path

urlpatterns = [
    path("", include("app.urls")),
]
```

### Rendering an HTML template

Typically, HTML files are stored as templates. The simplest HTML file would look like this
`templates/home.html`
```HTML
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h1>Hello World</h1>
    <p>Served by Django.</p>
</body>
</html>
```

In `app/views.py`
```Python
from django.shortcuts import render

def home(request):
    return render(request, "home.html")
```
this will render the HTML template.

`config/settings.py`
```Python
TEMPLATES = [
    {
        ...
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        ...
    },
]
```

### Adding CSS and JavaScript

A CSS file would look like

`static/css/style.css`
```CSS
body {
    font-family: Arial, sans-serif;
}

h1 {
    color: blue;
}
```

While a JavaScript file would look like

`static/js/script.js`
```js
console.log("JavaScript loaded!");

document.addEventListener("DOMContentLoaded", () => {
    console.log("Page is ready");
});
```

In `config/settings.py`, we make sure static files are enabled and add the directory
```Python
STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```

In the HTML template, load the static tag library and reference the files like
```HTML
{% load static %}

<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
    <title>Home</title>
</head>
<body>
    <h1>Hello World</h1>
    <p>Served by Django.</p>
    <script src="{% static 'js/script.js' %}"></script>
</body>
</html>
```
