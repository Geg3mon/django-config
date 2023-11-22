import os
from pathlib import Path
from datetime import timedelta
from django.utils.module_loading import import_string

from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

load_dotenv()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# JWT SETTINGS
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
REST_USE_JWT = int(os.getenv("REST_USE_JWT", 1))
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME":    timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME":   timedelta(days=7),
    "ROTATE_REFRESH_TOKENS":    True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN":        True,
    "SIGNING_KEY":              JWT_SECRET_KEY
    }

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.getenv("DEBUG", 0))

# GETENV VARIABLES
# SET DOMAIN AND NAME FOR HEROKU
DOMAIN = os.getenv("DOMAIN")
SITE_NAME = os.getenv("SITE_NAME")
URL = os.getenv("URL")
LOGIN_URL = os.getenv("LOGIN_URL")
LOGIN_REDIRECT_URL = os.getenv("LOGIN_REDIRECT_URL")
CALLBACK_URL = os.getenv("CALLBACK_URL")
FRONTEND_URL = os.getenv("FRONTEND_URL")
SITE_ID = 1

# DRF SETTINGS
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer"
        ),
    }

# SWAGGER SETTINGS
SWAGGER_USE_HEADER = int(os.getenv("SWAGGER_USE_HEADER"))
SWAGGER_TITLE = os.getenv("SWAGGER_TITLE")
SWAGGER_HEADER = os.getenv("SWAGGER_HEADER")
SWAGGER_TOKEN = os.getenv("SWAGGER_TOKEN")

# CORS AND HOSTS SETTINGS
ALLOWED_HOSTS = []
ALLOWED_HOST = os.getenv("ALLOWED_HOST")

if ALLOWED_HOST:
    ALLOWED_HOST = ALLOWED_HOST.replace(' ', '').split(',')
    ALLOWED_HOSTS.extend(ALLOWED_HOST)

if DEBUG:
    hosts = ["localhost", "127.0.0.1", ]
    ALLOWED_HOSTS.extend(hosts)


# HTTPS SETTINGS
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ["*"]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    "https://localhost:3000",
    "http://localhost",
    "https://localhost",
    "http://127.0.0.1",
    "https://127.0.0.1",
    "http://0.0.0.0",
    "https://0.0.0.0",
    "http://django",
    "https://django",
    ]

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
    ]

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # 3rd party libraries
    "debug_toolbar",
    "drf_yasg",
    "rest_framework",

    ]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND":  "django.template.backends.django.DjangoTemplates",
        "DIRS":     [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS":  {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                ],
            },
        },
    ]

WSGI_APPLICATION = "config.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DOCKER AND DEV DATABASE SETTINGS
DATABASES = {
    "default": {
        "ENGINE":   "django.db.backends.postgresql_psycopg2",
        "NAME":     os.getenv("POSTGRES_DATABASE"),
        "USER":     os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST":     os.getenv("POSTGRES_HOST"),
        "PORT":     os.getenv("POSTGRES_PORT"),
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
        },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
        },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
        },
    ]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Europe/Kiev"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = "/static/"
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

# Media settings
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# Email settings
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# TODO: Change on release
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_PORT = int(os.getenv("EMAIL_PORT"))
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

if DEBUG:
    INTERNAL_IPS = [
        "127.0.0.1",
        ]

# LOGGER SETTINGS
LOGGING = {
    "version":                  1,
    "disable_existing_loggers": False,
    "formatters":               {
        "main_format": {
            "format": "{asctime} - {levelname} - {module} - {filename} - {message}",
            "style":  "{",
            },
        },
    "handlers":                 {
        "console": {"class": "logging.StreamHandler", "formatter": "main_format"},
        "file":    {
            "level":     "DEBUG",
            "class":     "logging.FileHandler",
            "filename":  os.path.join(BASE_DIR, "logfile.log"),  # Adjust the file path as needed
            "formatter": "main_format",
            },
        },

    "loggers":                  {
        "django": {
            "handlers":  ["console", "file"],
            "propagate": True,
            "level":     "INFO",
            },
        },
    }

# JAZZMIN SETTINGS
# JAZZMIN_SETTINGS = {
#     "site_title":      "Config",
#     "site_header":     "Config",
#     "site_brand":      "Config",
#     "welcome_sign":    "Welcome to Config",
#     "copyright":       "Hihi",
#     "hide_models":     [],  # "authtoken.tokenproxy", "auth.group"
#     "show_ui_builder": True,
#     "icons":           {
#         # https: // fontawesome.com / v5 / search
#         "modul.model": "fas fa-comments",
#         },
#     }
