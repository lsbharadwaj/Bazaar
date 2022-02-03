from .base import *

DEBUG = True

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    "192.168.29.223",
    # ...
]

ALLOWED_HOSTS = ['*']


INSTALLED_APPS += [
    # Apps to use the installed packages
    # "sslserver",
    'debug_toolbar',
]


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'd4auiq0joiqpjg',

        'USER': 'lerdetczvpsyfb',

        'PASSWORD': '262938b2380aed9f4c686ad6dcaa0558fbba0362f6dba6360bc995ebbb4aa658',

        'HOST': 'ec2-54-224-64-114.compute-1.amazonaws.com',

        'PORT': '5432',

    }

}

REST_REGISTRATION.update(
    {
        'RESET_PASSWORD_VERIFICATION_URL':os.environ['FRONTEND_URL']+'/reset-password-confirm/',
        'REGISTER_VERIFICATION_URL':os.environ['FRONTEND_URL']+'/verify-registration/',
        'REGISTER_EMAIL_VERIFICATION_URL':os.environ['FRONTEND_URL']+'/register-new-email/',
        'VERIFICATION_FROM_EMAIL':'lsbharadwaj@gmail.com'
    }
)


CORS_ORIGIN_ALLOW_ALL=True