# MemCachier and Django on Heroku tutorial

This is an example Django 2.0 queue app (first in, first out) that
uses the [MemCachier add-on](https://addons.heroku.com/memcachier) in
[Heroku](http://www.heroku.com/). A running version of this app can be
found [here](http://memcachier-examples-django2.herokuapp.com).

Detailed instructions for developing this app are available
[here](https://devcenter.heroku.com/articles/django-memcache).

*Note: this example works with Python 3 and Django 2.0. It should also work for
Django 1.11. For older versions please check out our previous Django 1.6
[version](https://github.com/memcachier/examples-django2/tree/django1.6)*

## Deploy to Heroku

You can deploy this app yourself to Heroku to play with.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Running Locally

Run the following commands to get started running this app locally:

```sh
$ git clone https://github.com/memcachier/examples-django2.git
$ cd examples-django2
$ virtualenv -p python2 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py makemigrations mc_queue
$ python manage.py migrate
$ python manage.py runserver
```

Then visit `http://localhost:8000` to play with the app.

## Deploying to Heroku

Run the following commands to deploy the app to Heroku:

```sh
$ git clone https://github.com/memcachier/examples-django2.git
$ cd examples-django2
$ heroku create
Creating app... done, ⬢ rocky-chamber-17110
https://rocky-chamber-17110.herokuapp.com/ | https://git.heroku.com/rocky-chamber-17110.git
$ heroku addons:create memcachier:dev
$ git push heroku master
$ heroku run python manage.py makemigrations mc_queue
$ heroku run python manage.py migrate
$ heroku open
```

## Configuring MemCachier (settings.py)

To configure Django to use pylibmc with SASL authentication. You'll also need
to setup your environment, because pylibmc expects different environment
variables than MemCachier provides. Somewhere in your `settings.py` file you
should have the following lines:

```python
servers = os.environ['MEMCACHIER_SERVERS']
username = os.environ['MEMCACHIER_USERNAME']
password = os.environ['MEMCACHIER_PASSWORD']

CACHES = {
    'default': {
        # Use Django's native pylibmc backend (since Django 1.11, use
        # django-pylibmc for older versions)
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        # TIMEOUT is not the connection timeout! It's the default expiration
        # timeout that should be applied to keys! Setting it to `None`
        # disables expiration.
        'TIMEOUT': None,
        'LOCATION': servers,
        'OPTIONS': {
            # Use binary memcache protocol (needed for authentication)
            'binary': True,
            'username': username,
            'password': password,
            'behaviors': {
                # Enable faster IO
                'no_block': True,
                'tcp_nodelay': True,
                # Keep connection alive
                'tcp_keepalive': True,
                # Timeout settings
                'connect_timeout': 2000, # ms
                'send_timeout': 750 * 1000, # us
                'receive_timeout': 750 * 1000, # us
                # Timeout for set/get requests (sadly timeouts don't mark a
                # server as failed, so failover only works when the connection
                # is refused)
                '_poll_timeout': 2000, # ms
                # Better failover
                'ketama': True,
                'remove_failed': 1,
                'retry_timeout': 2,
                'dead_timeout': 30,
            }
        }
    }
}
```

Feel free to change the `_poll_timeout` setting to match your needs.

## Get involved!

We are happy to receive bug reports, fixes, documentation enhancements,
and other improvements.

Please report bugs via the
[github issue tracker](http://github.com/memcachier/examples-django2/issues).

Master [git repository](http://github.com/memcachier/examples-django2):

* `git clone git://github.com/memcachier/examples-django2.git`

## Licensing

This library is BSD-licensed.
