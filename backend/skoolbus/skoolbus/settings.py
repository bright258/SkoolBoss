from pathlib import Path
import os
import cloudinary
import django_on_heroku
import dj_database_url


django_on_heroku.settings(locals())

BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = 'django-insecure-xf)$fl7x-n$vy%uh_2$6+0gvx27e_6*c1%4^$y&_t_v+%60gsm'


DEBUG = False

ALLOWED_HOSTS = []



INSTALLED_APPS = [
    'whitenoise.runserver_nostatic'
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'rest_framework',
    'rest_framework.authtoken',
    'videochat',
    'crypto'
    
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "core.middleware.PaystackMiddleware"
]

ROOT_URLCONF = 'skoolbus.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'skoolbus.wsgi.application'
AUTH_USER_MODEL = 'core.User'


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


DATABASES = {

    'default':{

        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME':'',
        'USER':"",
        'PASSWORD':'',
        'HOST':'localhost',
        'PORT':""
    }
}


db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)


WHITENOISE_USE_FINDERS = True
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

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ),
    
}

# REST_FRAMEWORK ={

#     'DEFAULT_PERMISSION_CLASSES':[
#         'rest_framework.permissions.isAdminUser'
#     ]
# }

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static files')
STATICFILES_DIRS = [ 
    os.path.join(BASE_DIR, 'static')

]
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestFilesStorage'
COINBASE_COMMERCE_API_KEY ="8acfabb8-cd44-4096-8274-6b11a56a2aff"


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
PAYSTACK_SECRET_KEY = "sk_test_4b55ff77139812eeff86146e0ce6ad5fb8d503ce"
PAYSTACK_URL = "https://api.paystack.co"


cloudinary.config(
    cloud_name= 'dmjwzcjel',
    api_key=  '166665833888589',
    api_secret= 'FmuK9ZcteGr3UJg10wvrHGHOAAA'
)