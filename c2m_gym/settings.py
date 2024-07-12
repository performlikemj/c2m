"""
Django settings for c2m_gym project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
from django.utils.translation import gettext_lazy as _
from celery.schedules import crontab
from decouple import config
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Ensure log directory exists
LOG_DIR = os.path.join(BASE_DIR, 'logs')
os.makedirs(LOG_DIR, exist_ok=True)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'c2m_gym',
    'gymApp',
    'gym_info',
    'class_schedule',
    'products',
    'documentation',
    'stripe',
    'csp',
    'axes',
    'crispy_forms',
    'modeltranslation',
    'django_celery_beat',
    'corsheaders',
    'whitenoise.runserver_nostatic',
    'storages',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'csp.middleware.CSPMiddleware',
    'axes.middleware.AxesMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = [
    'gymApp.backends.CaseInsensitiveModelBackend',
    'gymApp.backends.EmailVerificationBackend',
    'django.contrib.auth.backends.ModelBackend',
    'axes.backends.AxesStandaloneBackend',
]

ROOT_URLCONF = 'c2m_gym.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'gymApp.context_processors.user_groups',
                'gymApp.context_processors.current_datetime',
            ],
        },
    },
]

WSGI_APPLICATION = 'c2m_gym.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': config('DATABASES_ENGINE'),
        'NAME': config('DATABASES_NAME'),
        'USER': config('DATABASES_USER'),
        'PASSWORD': config('DATABASES_PASSWORD'),
        'HOST': config('DATABASES_HOST'),
        'PORT': config('DATABASES_PORT'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

TIME_ZONE = 'Asia/Tokyo'
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

if not DEBUG:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Add your languages here
LANGUAGES = [
    ('en', _('English')),
    ('ja', _('Japanese')),
]

USE_I18N = True

# Default language code
LANGUAGE_CODE = 'en'

# Path where Django will store the compiled translation files
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

# Stripe settings
STRIPE_PUBLIC_KEY = config('STRIPE_PUBLIC_KEY')
STRIPE_SECRET_KEY = config('STRIPE_SECRET_KEY')
STRIPE_WEBHOOK_SECRET = config('STRIPE_WEBHOOK_SECRET')

# Login URL
LOGIN_URL = 'login'  # Redirect to login page

# Logging settings
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',  # Change to INFO to reduce verbosity
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'file_debug': {
            'level': 'DEBUG',  # Change to DEBUG for more verbosity
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'debug.log'),
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file_debug'],
            'level': 'DEBUG',  # Change to DEBUG to see more messages
            'propagate': True,
        },
        'gymApp': {
            'handlers': ['console', 'file_debug'],
            'level': 'DEBUG',  # Adjust this level as needed
            'propagate': True,
        },
    },
}



# # Email backend settings
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.your-email-provider.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'your-email@example.com'
# EMAIL_HOST_PASSWORD = 'your-email-password'
# DEFAULT_FROM_EMAIL = 'your-email@example.com'

# # Celery settings
# CELERY_BROKER_URL = 'redis://localhost:6379/2'
# CELERY_RESULT_BACKEND = 'redis://localhost:6379/2'
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_TIMEZONE = 'Asia/Tokyo'
# CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
# CELERY_BEAT_SCHEDULE = {
#     'check_active_subscriptions': {
#         'task': 'gymApp.tasks.check_active_subscriptions',
#         'schedule': crontab(hour=9, minute=0),  # Schedule to run every day at 9:00 AM
#         'options': {
#             'timezone': 'Asia/Tokyo',
#         },
#     },
# }

# # Site URL for generating verification links
# SITE_URL = 'http://c2mmuaythai.com/'

# settings.py

# Email backend settings for development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Celery settings
if not DEBUG:

    CELERY_BROKER_URL = config('CELERY_BROKER_URL')
    CELERY_RESULT_BACKEND = config('CELERY_RESULT_BACKEND') 
    CELERY_ACCEPT_CONTENT = ['json']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_TIMEZONE = 'Asia/Tokyo'
    CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
    CELERY_BEAT_SCHEDULE = {
        'check_active_subscriptions': {
            'task': 'gymApp.tasks.check_active_subscriptions',
            'schedule': crontab(hour=9, minute=0),  # Schedule to run every day at 9:00 AM
            'options': {
                'timezone': 'Asia/Tokyo',
            },
        },
    }
else:
    # Celery settings
    CELERY_BROKER_URL = 'redis://localhost:6379/2'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/2'
    CELERY_ACCEPT_CONTENT = ['json']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_TIMEZONE = 'Asia/Tokyo'
    CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
    CELERY_BEAT_SCHEDULE = {
        'check_active_subscriptions': {
            'task': 'gymApp.tasks.check_active_subscriptions',
            'schedule': crontab(hour=9, minute=0),  # Schedule to run every day at 9:00 AM
            'options': {
                'timezone': 'Asia/Tokyo',
            },
        },
    }

# Site URL for generating verification links
SITE_URL = config('SITE_URL')

# Azure Email settings
AZURE_CONNECTION_STRING = config('AZURE_CONNECTION_STRING')

# Azure Blob Storage settings
if not DEBUG:
    # Azure Storage settings
    AZURE_ACCOUNT_NAME = config('AZURE_ACCOUNT_NAME')
    AZURE_STORAGE_KEY = config('AZURE_STORAGE_KEY')
    AZURE_MEDIA_CONTAINER = config('AZURE_MEDIA_CONTAINER')
    AZURE_BLOB_CONNECTION_STRING = config('AZURE_BLOB_CONNECTION_STRING')
    DEFAULT_FILE_STORAGE = 'c2m_gym.azure_storage.AzureMediaStorage'
    MEDIA_URL = f'https://{AZURE_ACCOUNT_NAME}.blob.core.windows.net/{AZURE_MEDIA_CONTAINER}/'



if not DEBUG:
    # HTTPS settings
    # SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True

    # Cookie settings
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    CSRF_COOKIE_SECURE = True

    # Axes settings
    AXES_ENABLED = True
    AXES_FAILURE_LIMIT = 5
    AXES_COOLOFF_TIME = 1  # Cool off time in hours
    AXES_LOCK_OUT_AT_FAILURE = True
    AXES_RESET_ON_SUCCESS = True
    AXES_LOCKOUT_TEMPLATE = 'registration/account_lockout.html'
    AXES_LOCKOUT_URL = '/account_locked/'

    # Dynamically define the base URL for CSP
    AZURE_ACCOUNT_NAME = config('AZURE_ACCOUNT_NAME')
    CSP_BASE_URL = f'https://{AZURE_ACCOUNT_NAME}.blob.core.windows.net'

    # CSP settings (using django-csp) with dynamic Azure account name
    CSP_DEFAULT_SRC = (
        "'self'",
        'c2m-muay-thai.azurewebsites.net',
        '40.80.58.226',
        'https://c2m-muay-thai.azurewebsites.net',
        'https://c2mmuaythai.com',
        'https://www.c2mmuaythai.com',
        CSP_BASE_URL,
    )
    CSP_STYLE_SRC = (
        "'self'", 
        'fonts.googleapis.com',
        f'{CSP_BASE_URL}/static/css/style.css',
        'https://cdn.jsdelivr.net',
        'https://use.fontawesome.com',
        'https://cdnjs.cloudflare.com',
        'https://www.gstatic.com', 
    )
    CSP_FONT_SRC = (
        "'self'", 
        'fonts.gstatic.com',
        'https://use.fontawesome.com',
        'https://cdnjs.cloudflare.com'
    )
    CSP_SCRIPT_SRC = (
        "'self'", 
        'ajax.googleapis.com', 
        'https://code.jquery.com',
        'https://js.stripe.com', 
        'https://cdn.jsdelivr.net',
        f'{CSP_BASE_URL}/static/js/main.js',
        'https://cdnjs.cloudflare.com',
        'https://unpkg.com/@zxing/library@latest',
    )
    CSP_IMG_SRC = (
        "'self'",
        'c2m-muay-thai.azurewebsites.net',
        '40.80.58.226',
        CSP_BASE_URL,
        'c2mmuaythai.com',
        'www.c2mmuaythai.com',
        'data:',
    )
    CSP_FORM_ACTION = (
    "'self'",
    'https://c2mmuaythai.com',
    'https://www.c2mmuaythai.com',
    '40.80.58.226',
    )
else:
    # Dynamically define the base URL for CSP
    AZURE_ACCOUNT_NAME = config('AZURE_ACCOUNT_NAME')
    CSP_BASE_URL = f'https://{AZURE_ACCOUNT_NAME}.blob.core.windows.net'

    # CSP settings (using django-csp) with dynamic Azure account name
    CSP_DEFAULT_SRC = (
        "'self'",
        'c2m-muay-thai.azurewebsites.net',
        '40.80.58.226',
        'https://c2m-muay-thai.azurewebsites.net',
        'https://c2mmuaythai.com',
        'https://www.c2mmuaythai.com',
        '127.0.0.1',
        CSP_BASE_URL,
    )
    CSP_STYLE_SRC = (
        "'self'", 
        'fonts.googleapis.com',
        f'{CSP_BASE_URL}/static/css/style.css',
        'https://cdn.jsdelivr.net',
        'https://use.fontawesome.com',
        'https://cdnjs.cloudflare.com',
        'https://www.gstatic.com', 
        '127.0.0.1'
    )
    CSP_FONT_SRC = (
        "'self'", 
        'fonts.gstatic.com',
        'https://use.fontawesome.com',
        'https://cdnjs.cloudflare.com',
        '127.0.0.1'
    )
    CSP_SCRIPT_SRC = (
        "'self'", 
        'ajax.googleapis.com', 
        'https://code.jquery.com',
        'https://js.stripe.com', 
        'https://cdn.jsdelivr.net',
        f'{CSP_BASE_URL}/static/js/main.js',
        'https://cdnjs.cloudflare.com',
        'https://unpkg.com/@zxing/library@latest',
        '127.0.0.1'
    )
    CSP_IMG_SRC = (
        "'self'",
        'c2m-muay-thai.azurewebsites.net',
        '40.80.58.226',
        CSP_BASE_URL,
        'c2mmuaythai.com',
        'www.c2mmuaythai.com',
        '127.0.0.1',
        'data:',
    )
    CSP_FORM_ACTION = (
    "'self'",
    'https://c2mmuaythai.com',
    'https://www.c2mmuaythai.com',
    '40.80.58.226',
    '127.0.0.1'
    )