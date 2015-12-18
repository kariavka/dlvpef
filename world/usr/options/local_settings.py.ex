# -*- coding: utf-8 -*-

# DJANGO DEFAULT SETTINGS
DEBUG = False
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ['localhost', '127.0.0.1', ]

# DATABASES
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# SECRET_KEY
# ** You must change this value - this is important! Do not save the security
#    key and a different password in the repository.
## SECRET_KEY = 'bbz2u4=ja#gv$3n^4$g%(y+eoegsv(1xp2#7_^=oxilhq)afy='

# EMAIL SETTINGS
# ** Specify the mail settings to inform administrator about errors on the
#    server and and communication with users.
## EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
## EMAIL_USE_TLS = True
## EMAIL_HOST = 'smtp.gmail.com'
## EMAIL_PORT = 587
## DEFAULT_FROM_EMAIL = '<E-MAIL>'
## EMAIL_HOST_USER = '<E-MAIL>'
## EMAIL_HOST_PASSWORD = '<PASSWORD>'

