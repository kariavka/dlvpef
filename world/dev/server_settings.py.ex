# DJANGO DEFAULT SETTINGS
DEBUG = False
ALLOWED_HOSTS = ['dlvpef.org', 'localhost', '127.0.0.1', ]

# SESSIONS
# ** Optional.
# It is recommended to store the sessions in the radis.
SESSION_SERIALIZER='django.contrib.sessions.serializers.PickleSerializer'
SESSION_ENGINE = 'redis_sessions.session'
SESSION_REDIS_HOST = 'localhost'
SESSION_REDIS_PORT = 6379

# DATABASE
# ** Optional.
# For Django's projects recommended use PostgreSQL database.
# But, you can use any database: SQlite3, MySQL, PostgreSQL, etc:
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'NAME': 'dlvpef',
        'USER': '<USER>',
        'PASSWORD': '<PASSWORD>',
    }
}

# SECRET_KEY
# ** You must change this value - this is important!
SECRET_KEY = '987asd8jhg3^%&^%+eoegsv(1xp2#7_^=oxilhq)afy='

# EMAIL SETTINGS
# Specify the mail settings to inform administrator about errors on the
# server and and communication with users.
# ** For Gmail: http://www.google.com/accounts/DisplayUnlockCaptcha
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_PORT = 587

# Example for gmail.com
## EMAIL_HOST = 'smtp.gmail.com'
## DEFAULT_FROM_EMAIL = 'livarava.developer@gmail.com'
## EMAIL_HOST_USER = 'livarava.developer@gmail.com'
## EMAIL_HOST_PASSWORD = '<PASSWORD>'

# Example for mail.ru
## EMAIL_HOST = 'smtp.mail.ru'
## DEFAULT_FROM_EMAIL = 'livarava-developer@mail.ru'
## EMAIL_HOST_USER = 'livarava-developer@mail.ru'
## EMAIL_HOST_PASSWORD = '<PASSWORD>'

