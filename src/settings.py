"""
Django settings for yashankin project.

Generated by 'django-admin startproject' using Django 1.9.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*%gfoi)3+t^zo!o=g9!r@l6!_f1$5^yo(9^ss($7yxip8ti9rj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['ubuntu.local']


# Application definition

INSTALLED_APPS = [
    'suit',
    'yandex_cash_register',
    'ckeditor',
    'ckeditor_uploader',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'oferta.apps.OfertaConfig',
    'plastic',
    'mainapp',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',

                'mainapp.context_processors.slug.slug'
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Asia/Yekaterinburg'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.abspath(BASE_DIR + '/public/static/')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.abspath(BASE_DIR + '/public/media/')

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, "public"),
# )

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'User <yashankin-test@gmail.com>'
DEFAULT_CHARSET = 'utf-8'

SERVER_EMAIL = ""

ADMINS = [("Vladislav", "xservking@gmail.com")]

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
    'default': {
        'tabSpaces': 4,
        'width': '100%',
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['div', 'Source', '-', 'Preview',],
            ['Cut', 'Copy', 'Paste',],
            ['Undo', 'Redo', '-', 'Find', 'Replace', '-', 'SelectAll', 'RemoveFormat'],
            ['Maximize', 'ShowBlocks', '-', 'About', 'pbckcode'],
            ['Bold', 'Italic', 'Underline', 'Strike', '-', 'Subscript', 'Superscript'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', 'Blockquote', 'Table'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink','-', 'Image', 'Iframe', 'Button'],
            ['Styles', 'Format', 'Font', 'FontSize'],
            ['TextColor', 'BGColor'],
        ]
    }
}

OFERTA_URL = 'http://ubuntu.local:8000/oferta/'

# yandex-cash-register
YANDEX_CR_DEBUG = True
YANDEX_CR_SCID = 1234
YANDEX_CR_SHOP_ID = 1234
YANDEX_CR_SHOP_PASSWORD = 'qwerty'
YANDEX_CR_PAYMENT_TYPE = ['pc', 'ac', 'wm']
YANDEX_CR_ORDER_MODEL = 'plastic.Order'
YANDEX_CR_SHOP_DOMAIN = 'https://yashankin.com'

# sms auth
SMS_URL = "https://www.smsdirect.ru/submit_message"
SMS_LOGIN = "WorldGym"
SMS_PASS = "rjun32qvv"
SMS_FROM = "Powerhouse"

PAGES_URL = 'http://ubuntu.local:8000/pages/'
