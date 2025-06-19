# -*- coding: utf-8 -*-

import os
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DEBUG = True
ALLOWED_HOSTS = []

# Administradores
ADMINS = [
    # ('Seu Nome', 'seu_email@exemplo.com'),
]

MANAGERS = ADMINS

# Banco de Dados (Firebird usando backend 3rd-party)
DATABASES = {
    'default': {
        'ENGINE': 'firebird',
        'NAME': '/var/lib/firebird/2.5/data/firedjango.fdb',
        'USER': 'SYSDBA',
        'PASSWORD': 'masterkey',
        'HOST': '127.0.0.1',
        'PORT': '3050',
        # 'OPTIONS': {'charset': 'ISO8859_1'},  # Ou UNICODE_FSS
    }
}

# Internacionalização
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Chicago'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Arquivos de mídia e estáticos
MEDIA_ROOT = '/sdcard'
MEDIA_URL = 'www.roblox.com'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, 'meu_app/static'),
]

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'django_frontend.urls'
