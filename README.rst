DLVPEF
======

Droite la Vie Privée et Familiale (DLVPEF)

**Test site url:** http://dlvpef.weltwolke.com

**Test admin panel:** http://dlvpef.weltwolke.com/admin/

- Login: django
- Password: livarava

-------

Agreement
=========

- The `(venv)$` identifier of command line is indicates that there must be active virtual environment.

- In this manual path to the project, for example: `/full/path/to/the/dlvpef/` - it will be designated as `$BASE_DIR`.


Attention
=========

- Puthon support: `2.7`, `3.4` or higher!

-------

Quick start guide
+++++++++++++++++

Clone
-----

.. code-block::

    $ git  clone git@github.com:kariavka/dlvpef.git
    $ cd dlvpef


Install virtualenv
------------------

Python 2.7
~~~~~~~~~~

.. code-block::

    $ virtualenv --no-site-packages -p/usr/bin/python2.7 venv
    $ source venv/bin/activate
    (venv)$


Python 3.4
~~~~~~~~~~

.. code-block::

    $ pyvenv venv
    $ source venv/bin/activate
    (venv)$


Install packages
----------------

Python 2.7
~~~~~~~~~~

.. code-block::

    (venv)$ pip install -r requirements.txt


Python 3.4
~~~~~~~~~~

.. code-block::

    (venv)$ pip3 install -r requirements.txt


Synchronize
+++++++++++

.. code-block::

    (venv)$ cd $BASE_DIR/src/
    (venv)$ ./manage.py migrate
    (venv)$ ./manage.py createsuperuser


Fixtures
++++++++

In order to quickly create website's pages and any informations, you need to install the some fixtures:

.. code-block::

    (venv)$ cd $BASE_DIR/src/
    (venv)$ ./manage.py loaddata apps/content/fixtures/pages.json
    (venv)$ ./manage.py loaddata apps/content/fixtures/informations.json


Test run
++++++++

.. code-block::

    (venv)$ cd $BASE_DIR/src/
    (venv)$ ./manage.py runserver 127.0.0.1:7171

-------

Server settings
===============

**It is optional settings.**

If you need to change the default project settings - use `local_settings.py`.

Create server django settings in `$BASE_DIR/src/basic/local_settings.py`:

.. code-block::

    (venv)$ cd $BASE_DIR/src/basic/
    (venv)$ touch local_settings.py
    (venv)$


Create `local_settings` as, example:

.. code-block:: python

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


P.s. See examples in `$BASE_DIR/world/dev/`, and use workpiece from `$BASE_DIR/world/usr/options/`.


Create database
+++++++++++++++

PostgreSQL
----------

.. code-block::

    $ sudo -u postgres psql

    # CREATE USER <USER> WITH password <PASSWORD>;
    # drop database if exists dlvpef;
    # CREATE DATABASE dlvpef;
    # GRANT ALL privileges ON DATABASE dlvpef TO <USER>;

    #\q


MySQL
-----

.. code-block::

    $ sudo mysql -uroot -p

    drop database if exists `dlvpef`;
    CREATE DATABASE `dlvpef` CHARACTER SET utf8 COLLATE utf8_general_ci;
    GRANT ALL ON `dlvpef`.* TO `<USER>`@localhost IDENTIFIED BY '<PASSWORD>';
    FLUSH PRIVILEGES;

