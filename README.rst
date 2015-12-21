DLVPEF
======

Droite la Vie Privée et Familiale (DLVPEF)

**Test site url:** http://dlvpef.weltwolke.com

**Test admin panel:** http://dlvpef.weltwolke.com/admin/

- Login: django
- Password: livarava

-------

.. attention::

    To work needed python 3.4 or higher!


Quick start guide
-----------------

Clone.
++++++

.. code-block::

    $ git  clone git@github.com:kariavka/dlvpef.git
    $ cd dlvpef

Install virtualenv.
++++++++++++++++++++

Python 2.7
----------

.. code-block::

    $ virtualenv --no-site-packages -p/usr/bin/python2.7 venv
    $ source venv/bin/activate
    (venv)$


Python 3.4
----------

.. code-block::

    $ pyvenv venv
    $ source venv/bin/activate
    (venv)$


Install packages.
+++++++++++++++++

Python 2.7
----------

.. code-block::

    (venv)$ pip install -r requirements.txt


Python 3.4
----------

.. code-block::

    (venv)$ pip3 install -r requirements.txt


Local settings.
+++++++++++++++

Create local django settings in `/some/path/to/projects/dlvpef/world/etc/local_settings.py`:

.. code-block:: python

    # DJANGO DEFAULT SETTINGS
    DEBUG = False
    ALLOWED_HOSTS = ['dlvpef.org', 'localhost', '127.0.0.1', ]

    # SESSIONS
    # ** Optional.
    SESSION_SERIALIZER='django.contrib.sessions.serializers.PickleSerializer'
    SESSION_ENGINE = 'redis_sessions.session'
    SESSION_REDIS_HOST = 'localhost'
    SESSION_REDIS_PORT = 6379

    # DATABASE
    # ** Optional (you can use sqlite).
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
    # ** You must change this value - this is important! Do not save the security
    #    key and a different password in the repository.
    SECRET_KEY = '987asd8jhg3^%&^%+eoegsv(1xp2#7_^=oxilhq)afy='

    # EMAIL SETTINGS
    # ** For Gmail: http://www.google.com/accounts/DisplayUnlockCaptcha
    # ** Specify the mail settings to inform administrator about errors on the
    #    server and and communication with users.
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


P.s. See examples in `dlvpef/world/dev/`, and use workpiece from `dlvpef/world/usr/options/`.

Create database.
++++++++++++++++

**It is optional!** You can use any database.

.. code-block::

    $ sudo -u postgres psql

    # CREATE USER <USER> WITH password <PASSWORD>;
    # drop database if exists dlvpef;
    # CREATE DATABASE dlvpef;
    # GRANT ALL privileges ON DATABASE dlvpef TO <USER>;

    #\q


Synchronize.
++++++++++++

.. code-block::

    (venv)$ pwd
    /some/path/to/projects/dlvpef
    (venv)$ cd src/
    (venv)$ ./manage.py migrate
    (venv)$ ./manage.py createsuperuser


Fixtures.
+++++++++

In order to quickly create website's pages, you need to install the pages fixtures:

.. code-block::

    (venv)$ pwd
    /some/path/to/projects/dlvpef
    (venv)$ cd src/
    (venv)$ ./manage.py loaddata apps/content/fixtures/pages.json
    (venv)$ ./manage.py loaddata apps/content/fixtures/informations.json


Run.
++++

.. code-block::

    (venv)$ pwd
    /some/path/to/projects/dlvpef
    (venv)$ cd src/
    (venv)$ ./manage.py runserver 127.0.0.1:7171


