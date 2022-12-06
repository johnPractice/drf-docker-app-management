"""
Django settings for hamravesh project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import logging
import os
# from datetime import date
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
env_path = os.path.join(BASE_DIR, '.env')
load_dotenv(env_path)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', None)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 3rd party app
    'rest_framework',
    # apps
    "docker_app",

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

ROOT_URLCONF = 'hamravesh.urls'

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

WSGI_APPLICATION = 'hamravesh.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    # # database config for connect db to postgres
    # "default": {
    #     "ENGINE": "django.db.backends.postgresql_psycopg2",
    #     "NAME": os.environ.get("DB_NAME", "api_dano"),
    #     "USER": os.environ.get("DB_USER", "postgres"),
    #     "PASSWORD": os.environ.get("DB_PASSWORD", None),
    #     "PORT": os.environ.get("DB_PORT", "5432"),
    #     "HOST": os.environ.get("DB_HOST", "localhost"),
    # },
}


# # initalize cache
# # # if want use django cache uncomment below code

# REDIS_HOST = os.environ.get('REDIS_HOST', None)
# REDIS_PORT = int(os.environ.get('REDIS_PORT', "6379"))
# REDIS_USERNAME = os.environ.get('REDIS_USERNAME', "default")
# REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD', None)
# REDIS_DANO_CACHE_DB = os.environ.get('REDIS_DANO_CACHE_DB', '1')
# REDIS_KEY_PREFIX = os.environ.get('REDIS_KEY_PREFIX', '')
# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": f"redis://{REDIS_USERNAME}:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DANO_CACHE_DB}",
#         "OPTIONS": {
#             'REDIS_CLIENT_CLASS': 'django_cluster_redis.cache.ClusterRedis',
#         },
#         "KEY_PREFIX": REDIS_KEY_PREFIX,
#     }
# }


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

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# # Initialize logger
# # # config logger settings

# today = date.today()
# log_file_name = f'/logs/api-dano-{today.year}-{today.month}-{today.day}.log'
# output_file = Path(log_file_name)
# output_file.parent.mkdir(exist_ok=True, parents=True)
# output_file.touch()

# LOGGING = {
#     'version': 1,
#     'formatters': {
#         'verbose': {
#             'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
#         },
#         'simple': {
#             'format': '%(levelname)s %(message)s'
#         },
#     },
#     'handlers': {
#         'logstash': {
#             'level': 'DEBUG',
#             'class': 'logger.logstash.TCPLogstashHandler',
#             'host': os.environ.get('LOGSTASH_HOST', 'logstash'),
#             'port': os.environ.get('LOGSTASH_PORT', 8080),
#             'version': 1,
#             'message_type': 'logstash',
#             'fqdn': False,
#             'tags': ['api-dano', 'django', os.environ.get('ENV_NAME', 'dev')],
#         },
#         'console_logger': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'simple'
#         },
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': log_file_name,
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['logstash', 'file', 'console_logger'],
#             'level': 'INFO',
#             'propagate': True,
#         },
#         'django.request': {
#             'handlers': ['logstash', 'file', 'console_logger'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#     },
# }
logger = logging.getLogger('django')
