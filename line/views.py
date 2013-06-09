## MemCachier Django Tutorial App
#
# This optimizes the loading of the index page, a page that is simply a read
# operation. In the optimized case it is one lookup from MemCachier and no load
# on the DB.
#
# The add and remove operations invovle an expensive query to the DB but should
# be rare compared to the index in most web apps (read Vs. writes).

from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from line.models import LineItem
from django.core.cache import cache
from django.core.context_processors import csrf
import time

LINE_KEY = "line"

# index.html -- display all lines from the queue.
def index(request):
  # try cache
  line = cache.get(LINE_KEY)
  if not line:
    # not in cache -- so hit db, then store in cache.
    line = db_slow_index()
    cache.set(LINE_KEY, line)

  # display the queue to the user.
  c = {'line': line}
  c.update(csrf(request))
  return render_to_response('index.html', c)


# /add -- add a new line to the front of the queue.
def add(request):
  item = LineItem(text=request.POST["text"])
  item.save()
  # Update cache -- have to hit DB.
  cache.set(LINE_KEY, db_get_lines())
  # ....^.............^
  # We may be tempted to use the `append` memcache method here instead of
  # retrieving the lines again. However, we are using pythons serialization of
  # the LineItem data structure, so `append` would not nessecarily work. We
  # could use append though if we used our own serialization method.
  #
  return HttpResponse("%s" % item.text)


# /remove -- remove the last line from the queue.
def remove(request):
  items = LineItem.objects.order_by("id")[:1]
  if len(items) != 0:
    items[0].delete()
    # update cache -- have to hit DB.
    cache.set(LINE_KEY, db_get_lines())
  return redirect("/")


# A 'slow' database lookup for the entire queue.
def db_slow_index():
  time.sleep(2) # simulate a slow query.
  return db_get_lines()


# A database lookup for the entire queue.
def db_get_lines():
  return LineItem.objects.order_by("id")

