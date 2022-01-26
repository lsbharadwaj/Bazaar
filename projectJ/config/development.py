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
    "sslserver",
    'debug_toolbar',
]


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

REST_REGISTRATION.update(
    {
        'RESET_PASSWORD_VERIFICATION_URL':'https://localhost:3000/reset-password/',
        'REGISTER_VERIFICATION_URL':'https://localhost:3000/verify-registration/',
        'REGISTER_EMAIL_VERIFICATION_URL':'https://localhost:3000/register-new-email/',
        'VERIFICATION_FROM_EMAIL':'lsbharadwaj@gmail.com'
    }
)


CORS_ORIGIN_ALLOW_ALL=True