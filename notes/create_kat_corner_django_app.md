# Kat Corner: A Reusable Django App

A standalone Django app for managing “Kats” (kitten data), complete with models, admin, views, static files, templates, packaging, and code-quality tooling.

---

## 1. Prerequisites

* **Python 3.11** (or ≥ 3.7)
* **pipenv** (or `venv` + `pip`)
* **Django ≥ 3.0**
* (Optional) Git

---

## 2. App Structure & Core Files

```
kats-kat-corner/
├── kat_corner/              # your app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── static/kat_corner/…  # any .css/.js/images
│   └── templates/kat_corner/…  # any HTML templates
├── manage.py
├── Pipfile                  # pipenv deps
├── pyproject.toml           # PEP 517 build-system
├── setup.py                 # setuptools packaging
├── MANIFEST.in              # include README, static, templates
└── .flake8                  # code-style config
```

---

### 2.1 `kat_corner/models.py`

```python
from django.db import models

class Kat(models.Model):
    name = models.CharField(max_length=255, help_text="The name of the kat")
    age  = models.IntegerField()

    def __str__(self):
        return f"{self.name} : {self.age}"
```

---

### 2.2 `kat_corner/admin.py`

```python
from django.contrib import admin
from .models import Kat

@admin.register(Kat)
class KatAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display  = ("name", "age")
    list_filter   = ("age",)
    ordering      = ("name",)
```

---

### 2.3 `kat_corner/apps.py`

```python
from django.apps import AppConfig

class KatCornerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name               = "kat_corner"
    verbose_name       = "Kat Corner"
```

---

### 2.4 `kat_corner/settings.py`

```python
from django.conf import settings

# Fallback site-name if not set in project’s settings.py
THE_SITE_NAME = getattr(settings, "THE_SITE_NAME", "Kat Corner")
```

---

### 2.5 `kat_corner/urls.py`

```python
from django.urls import path
from . import views

app_name = "kat_corner"

urlpatterns = [
    path("", views.index, name="index"),
]
```

---

### 2.6 `kat_corner/views.py`

```python
from django.http import HttpResponse
from .settings import THE_SITE_NAME

THE_APP_NAME = "Kat Corner"

def index(request):
    """Display a simple welcome message."""
    return HttpResponse(
        f"<title>{THE_SITE_NAME} - {THE_APP_NAME}</title>"
        f"Hello, Kats! You're at the {THE_SITE_NAME} : {THE_APP_NAME} site."
    )
```

---

## 3. Code-Quality & Packaging Files

### 3.1 `.flake8`

```ini
[flake8]
exclude         = migrations
max-line-length = 88
statistics      = True
```

### 3.2 `Pipfile`

```toml
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
django = "*"
black  = "*"
isort  = "*"
flake8 = "*"
build  = "*"

[requires]
python_version = "3.11"
```

### 3.3 `pyproject.toml`

```toml
[build-system]
requires    = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"
```

### 3.4 `setup.py`

```python
from setuptools import find_packages, setup

setup(
    name="KatCorner",
    version="0.1",
    packages=find_packages(exclude=["project_test", "kat_corner.migrations"]),
    include_package_data=True,
    description="A simple Django app for kat data.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.7",
    url="https://github.com/brucestull/kats-kat-corner",
    author="Flynnt Knapp",
    author_email="FlynntKnapp@gmail.com",
    license="MIT",
    install_requires=["django>=3.0"],
    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python :: 3",
    ],
)
```

### 3.5 `MANIFEST.in`

```ini
# Include README & LICENSE
include README.md
include LICENSE

# Include all static files & templates
recursive-include kat_corner/static *
recursive-include kat_corner/templates *

# Exclude migrations & tests
recursive-exclude kat_corner/migrations *.py
recursive-exclude tests *.py
```

---

## 4. Example Project: `kats`

1. **Create & activate** your pipenv (or venv):

    ```bash
    cd ~/Programming
    pipenv shell
    pipenv install --dev
    ```

2. **Install KatCorner** in editable mode:

    ```bash
    pipenv install -e /path/to/kats-kat-corner
    ```

3. **Start a new Django project** (if you haven’t already):

    ```bash
    django-admin startproject kats project_test
    mv project_test kats
    cd kats
    ```

4. **Enable the app** in `kats/settings.py`:

    ```python
    INSTALLED_APPS = [
        # …
        "kat_corner.apps.KatCornerConfig",
        # …
    ]

    # (optional) override the default site name
    THE_SITE_NAME = "My Awesome Kats"
    ```

5. **Include KatCorner’s URLs** in `kats/urls.py`:

    ```python
    from django.urls import include, path

    urlpatterns = [
        path("admin/", admin.site.urls),
        path("kats/", include("kat_corner.urls", namespace="kat_corner")),
    ]
    ```

---

## 5. Database & Admin

1. **Make migrations** for your new app:

    ```bash
    python manage.py makemigrations kat_corner
    python manage.py migrate
    ```

2. **Create a superuser**:

    ```bash
    python manage.py createsuperuser
    ```

3. **Run the server**:

    ```bash
    python manage.py runserver
    ```

4. **Visit**

    * [http://127.0.0.1:8000/kats/](http://127.0.0.1:8000/kats/) → your `index` view
    * [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) → manage `Kat` objects

---

## 6. Building & Distributing

* **Build** a source + wheel:

    ```bash
    pipenv run build
    ```

* **Publish** to PyPI (once you’ve created an account):

    ```bash
    twine upload dist/*
    ```

Now any Django project can simply `pip install KatCorner` and add it to `INSTALLED_APPS`!

---

🎉 You’ve got a fully-packaged, reusable Django app ready for any “kats” project. Enjoy!
