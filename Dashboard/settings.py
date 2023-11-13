from pathlib import Path
import os
from django.core.exceptions import ImproperlyConfigured
from dotenv import load_dotenv


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

MEDIA_URL = 'images/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

#DOTENV_PATH = os.path.join(os.path.join(BASE_DIR, 'static'), '.env')

# Load environment variables from .env file
load_dotenv()

# Handles the error messages for any missing environment varibles
def get_env_value(env_variable):
    try:
        return os.environ[env_variable]
    except KeyError:
        error_msg = 'Set the {} environment variable'.format(env_variable)
        raise ImproperlyConfigured(error_msg)

# Directory of navbar template at the base of the project folder
#TEMP_DIR = os.path.join(BASE_DIR, 'templates')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_value('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =  get_env_value('DEBUG')

ALLOWED_HOSTS = []
if not DEBUG:
    ALLOWED_HOSTS += [get_env_value('ALLOWED_HOSTS')]


# Application definition
INSTALLED_APPS = [
    'accounts',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    
    'django_filters',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dashboard.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'dashboard.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

'''
1 - Download and install PostgreSQL & PG Admin
2 - Login to PG admin & Create Database
2 - Connect database to Django App & run migrations
4 - Create database on AWS
5 - Connect to live AWS Database with PG admin & Django
'''
print(DEBUG)
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": get_env_value('DATABASE_ENGINE'),
            "NAME": get_env_value('DATABASE_NAME'),
            "USER": get_env_value('DATABASE_USER'),
            "PASSWORD": get_env_value('DATABASE_PASSWORD'),
            "HOST": get_env_value('DATABASE_HOST'),
            "PORT": get_env_value('DATABASE_PORT'),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')

# Simple Mail Transfer Protocol Configuration
EMAIL_BACKEND = get_env_value('EMAIL_BACKEND')
EMAIL_HOST = get_env_value('EMAIL_HOST')
EMAIL_PORT = get_env_value('EMAIL_PORT')
EMAIL_USE_TLS = get_env_value('EMAIL_USE_TLS')
EMAIL_HOST_USER = get_env_value('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = get_env_value('EMAIL_HOST_PASSWORD')

#S3 Buckets config
AWS_ACCESS_KEY_ID = get_env_value('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = get_env_value('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = get_env_value('AWS_STORAGE_BUCKET_NAME')

AWS_S3_FILE_OVERWRITE = get_env_value('AWS_S3_FILE_OVERWRITE')
AWS_DEFAULT_ACL = get_env_value('AWS_DEFAULT_ACL')

DEFAULT_FILE_STORAGE = get_env_value('DEFAULT_FILE_STORAGE')
STATICFILES_STORAGE = get_env_value('STATICFILES_STORAGE')
