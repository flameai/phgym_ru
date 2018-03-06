# coding:utf-8
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gym7',
        'USER': 'bbx',
        'PASSWORD': '12345',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}
ALLOWED_HOSTS = ['*', '2017.u46521.netangels.ru', 'powerhousegym.ru', 'www.powerhousegym.ru']

DEBUG = True



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(ROOT_PATH, 'static/')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_ROOT = os.path.join(ROOT_PATH, 'media/')
MEDIA_URL = '/media/'
