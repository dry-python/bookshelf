import os

from debug_toolbar.settings import PANELS_DEFAULTS
from environ import Env

env = Env()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = "92)08k$_5!90rcx9h)doje#p(50a$dpa!8(pchqnz59bpo!ez&"

DEBUG = True

ALLOWED_HOSTS = []

INTERNAL_IPS = ["127.0.0.1"]

INSTALLED_APPS = [
    # Builtin.
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.staticfiles",
    # Third-party.
    "django_extensions",
    "debug_toolbar",
    "stories.contrib.debug_toolbars.django",
    # Project.
    "bookshelf.apps.BookshelfConfig",
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "bookshelf.middlewares.ProfileIdMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "bookshelf.urls"

LOGIN_URL = "/login/"

LOGIN_REDIRECT_URL = "/profile/"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {},
    }
]

WSGI_APPLICATION = "bookshelf.wsgi.application"

DATABASES = {"default": env.db()}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
        )
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

DEBUG_TOOLBAR_PANELS = PANELS_DEFAULTS + [
    "stories.contrib.debug_toolbars.django.StoriesPanel"
]
