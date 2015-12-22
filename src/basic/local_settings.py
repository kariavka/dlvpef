# Django default settings.
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1', ]

# Database.
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'NAME': 'dlvpef',
        'USER': 'django',
        'PASSWORD': 'qazwsxe',
    }
}

# Secret key.
# ** You must change this value - this is important!
SECRET_KEY = 'bbz2u4=ja#gv$3n^4$g%(y+eoegsv(1xp2#7_^=oxilhq)afy='

# Email settings.
# ** For Gmail: http://www.google.com/accounts/DisplayUnlockCaptcha
# ** Specify the mail settings to inform administrator about errors on the
# server and and communication with users.
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_PORT = 587

## EMAIL_HOST = 'smtp.gmail.com'
## DEFAULT_FROM_EMAIL = 'livarava.developer@gmail.com'
## EMAIL_HOST_USER = 'livarava.developer@gmail.com'
## EMAIL_HOST_PASSWORD = 'livarava_developer'

EMAIL_HOST = 'smtp.mail.ru'
DEFAULT_FROM_EMAIL = 'livarava-developer@mail.ru'
EMAIL_HOST_USER = 'livarava-developer@mail.ru'
EMAIL_HOST_PASSWORD = 'developer_here'

