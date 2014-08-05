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
$ virtualenv venv --distribute
$ source venv/bin/activate
$ pip install Django psycopg2 dj-database-url
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

## Get involved!

We are happy to receive bug reports, fixes, documentation enhancements,
and other improvements.

Please report bugs via the
[github issue tracker](http://github.com/memcachier/examples-django2/issues).

Master [git repository](http://github.com/memcachier/examples-django2):

* `git clone git://github.com/memcachier/examples-django2.git`

## Licensing

This library is BSD-licensed.

