"""
Django settings for kranti project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-mr$lyud*as+t7q$^xp_@og_c&&^*s6@ovkx05xlg0h55s#yz#6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mainapp',
    'storages'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kranti.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates")],
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
CSRF_TRUSTED_ORIGINS=['https://kranti2k23.tech']
WSGI_APPLICATION = 'kranti.wsgi.application'
SKEY="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"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}

DATABASES={
    'default':{
    'ENGINE':'django.db.backends.postgresql',
    'NAME':'postgres',
    'HOST':'db.lxvlckkxcmzejpcucmxb.supabase.co',
    'USER':'postgres',
    'POST':5432,
    'PASSWORD':'kranti2k23#'
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

if(DEBUG==True):
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static')
    ]
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

else:
    DEFAULT_FILE_STORAGE = 'kranti.custom_azure.AzureMediaStorage'
    STATICFILES_STORAGE = 'kranti.custom_azure.AzureStaticStorage'

    STATIC_LOCATION = "static"
    MEDIA_LOCATION = "media"

    AZURE_ACCOUNT_NAME = "kranti2k23"
    AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'
    STATIC_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
    MEDIA_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{MEDIA_LOCATION}/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
