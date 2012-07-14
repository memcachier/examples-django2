# Django Line Example

This is an example Django line app (first in, first out) that uses the [MemCachier add-on](https://addons.heroku.com/memcachier) in [Heroku](http://www.heroku.com/).

Detailed instructions for developing this app are available here (TODO: link).

# Running Locally

[Setup a local Postgres database](https://devcenter.heroku.com/articles/local-postgresql) and be sure you have Python installed, too.

Run the following commands to get started running this app locally.

    $ git clone https://github.com/memcachier/memcachier_line.git
    $ cd memcachier_line
    $ virtualenv venv --distribute
    $ source venv/bin/activate
    $ pip install Django psycopg2 dj-database-url
    $ python manage.py syncdb
    $ python manage.py runserver

Then visit `http://localhost:8000` to play with the app.

# Deploying to Heroku
Run the following commands to deploy the app to Heroku:

    $ git clone https://github.com/memcachier/memcachier_line.git
    $ cd memcachier_line
    $ heroku create
    Creating high-flower-8873... done, stack is cedar
    http://high-flower-8873.herokuapp.com/ | git@heroku.com:high-flower-8873.git
    Git remote heroku added
    $ heroku addons:add memcachier:25
    $ git push heroku master
    $ heroku run python manage.py syncdb
    $ heroku open

Note: when running `syncdb` you will be prompted to create a superuser.  Respond with `no`.