# MemCachier on Heroku and Django tutorial

This is an example Django (1.6) queue app (first in, first out) that
uses the [MemCachier add-on](https://addons.heroku.com/memcachier) in
[Heroku](http://www.heroku.com/). A running version of this app can be
found [here](http://memcachier-examples-django2.herokuapp.com).

Detailed instructions for developing this app are available
[here](https://devcenter.heroku.com/articles/django-memcache).

## Deploy to Heroku

You can deploy this app yourself to Heroku to play with.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Running Locally

Run the following commands to get started running this app locally:

~~~~ .sh
$ git clone https://github.com/memcachier/examples-django2.git
$ cd examples-django2
$ virtualenv -p python2 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py syncdb
$ python manage.py runserver
~~~~

Then visit `http://localhost:8000` to play with the app.

## Deploying to Heroku

Run the following commands to deploy the app to Heroku:

~~~~ .sh
$ git clone https://github.com/memcachier/examples-django2.git
$ cd examples-django2
$ heroku create
Creating high-flower-8873... done, stack is cedar
http://high-flower-8873.herokuapp.com/ | git@heroku.com:high-flower-8873.git
Git remote heroku added
$ heroku addons:add memcachier:25
$ git push heroku master
$ heroku run python manage.py syncdb
$ heroku open
~~~~

Note: when running `syncdb` you will be prompted to create a
superuser. Respond with `no`.

## Configuring MemCachier (settings.py)

To configure Django to use pylibmc with SASL authentication. You'll also need
to setup your environment, because pylibmc expects different environment
variables than MemCachier provides. Somewhere in your `settings.py` file you
should have the following lines:

~~~~ .python
os.environ['MEMCACHE_SERVERS'] = os.environ.get('MEMCACHIER_SERVERS', '').replace(',', ';')
os.environ['MEMCACHE_USERNAME'] = os.environ.get('MEMCACHIER_USERNAME', '')
os.environ['MEMCACHE_PASSWORD'] = os.environ.get('MEMCACHIER_PASSWORD', '')

CACHES = {
    'default': {
        # Use pylibmc
        'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',

        # Use binary memcache protocol (needed for authentication)
        'BINARY': True,

        # TIMEOUT is not the connection timeout! It's the default expiration
        # timeout that should be applied to keys! Setting it to `None`
        # disables expiration.
        'TIMEOUT': None,
        'OPTIONS': {
            # Enable faster IO
            'no_block': True,
            'tcp_nodelay': True,

            # Keep connection alive
            'tcp_keepalive': True,

            # Timeout for set/get requests (sadly timeouts don't mark a
            # server as failed, so failover only works when the connection
            # is refused)
            '_poll_timeout': 2000,

            # Use consistent hashing for failover
            'ketama': True,

            # Configure failover timings
            'connect_timeout': 2000,
            'remove_failed': 4,
            'retry_timeout': 2,
            'dead_timeout': 10
        }
    }
}
~~~~

Feel free to change the `_poll_timeout` setting to match your needs.

## Persistent Connections

By default, Django doesn't use persistent connections with memcached. This is a
huge performance problem, especially when using SASL authentication as the
connection setup is even more expensive than normal.

You can fix this by putting the following code in your `wsgi.py` file:

~~~~ .python
# Fix django closing connection to MemCachier after every request (#11331)
from django.core.cache.backends.memcached import BaseMemcachedCache
BaseMemcachedCache.close = lambda self, **kwargs: None

~~~~

There is a bug file against Django for this issue
([#11331](https://code.djangoproject.com/ticket/11331)).

## Get involved!

We are happy to receive bug reports, fixes, documentation enhancements,
and other improvements.

Please report bugs via the
[github issue tracker](http://github.com/memcachier/examples-django2/issues).

Master [git repository](http://github.com/memcachier/examples-django2):

* `git clone git://github.com/memcachier/examples-django2.git`

## Licensing

This library is BSD-licensed.

