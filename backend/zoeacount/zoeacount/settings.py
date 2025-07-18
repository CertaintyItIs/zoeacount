"""
Django settings for zoeacount project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-dk_4diee)+$cu1_0-p#dh6f7v$83kbjwax#ju+8dq7oazz3kmi"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0', '192.168.1.12', 'localhost', '127.0.0.1', '10.42.0.1']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'rest_framework_simplejwt',
    "rest_framework",
    "zoeaapi",
    "corsheaders"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware"
]


CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://10.42.0.1:3000",
    "http://192.168.1.12:3000"
 
]
CORS_ALLOW_HEADERS = [
    'content-type',
    'authorization',
    'x-csrftoken',
]

CORS_ALLOW_CREDENTIALS = True
SESSION_COOKIE_SAMESITE = "None"
SESSION_COOKIE_SECURE = False  # Set to True if using HTTPS


ROOT_URLCONF = "zoeacount.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "zoeacount.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_ROOT = BASE_DIR / "media"

MEDIA_URL = "/media/"

RESULTS_ROOT = BASE_DIR / "zoeaapi" / "cv_app" / "processed"

RESULTS_URL = "/results/"

CAPTURED_ROOT = BASE_DIR / "zoeaapi" / "cv_app" / "to_detect"

CAPTURED_URL = "/captured/"

# Authentication
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
    'SLIDING_TOKEN_LIFETIME': timedelta(days=30),
    'SLIDING_TOKEN_REFRESH_LIFETIME_LATE_USER': timedelta(days=1),
    'SLIDING_TOKEN_LIFETIME_LATE_USER': timedelta(days=30),
    'TOKEN_OBTAIN_SERIALIZER': 'zoeaapi.serializer.CustomTokenObtainPairSerializer',
    "SIGNING_KEY": 'AAdFksq97fVIg1sHAgyygC3XaKkutJId8lzIKRixVQ0=',

    # Enable JWT in cookies
    "AUTH_COOKIE": "access_token",
    "AUTH_COOKIE_REFRESH": "refresh_token",
    "AUTH_COOKIE_SECURE": False,  # Set to False if not using HTTPS
    "AUTH_COOKIE_HTTP_ONLY": True,
    "AUTH_COOKIE_PATH": "/",
    "AUTH_COOKIE_SAMESITE": "None",  # Important for cross-origin requests
}

SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Default session engine
SESSION_COOKIE_HTTPONLY = True  # Helps prevent access to cookies via JavaScript
SESSION_COOKIE_SECURE = False  # Should be True in production (use HTTPS)

CSRF_COOKIE_SECURE = False  # Secure cookie (only for HTTPS)
CSRF_COOKIE_SAMESITE = 'None'
CSRF_COOKIE_HTTPONLY = False
# CSRF_TRUSTED_ORIGINS = ['http://0.0.0.0/', 'http://192.168.1.12/', 'http://localhost/', 'http://127.0.0.1/', 'http://10.42.0.1:8000/', 'http://10.42.0.1:3000/']
# CSRF_ALLOWED_ORIGINS = ['http://0.0.0.0/', 'http://192.168.1.12/', 'http://localhost/', 'http://127.0.0.1/', 'http://10.42.0.1:8000/', 'http://10.42.0.1:3000/']

SESSION_COOKIE_SAMESITE = 'None'