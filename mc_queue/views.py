from django.http import HttpResponse
from django.template.context_processors import csrf
from django.shortcuts import render_to_response, redirect
from mc_queue.models import QueueItem
from django.core.cache import cache
import time

QUEUE_KEY = "queue"

def index(request):
  queue = cache.get(QUEUE_KEY)
  if not queue:
    time.sleep(2)  # simulate a slow query.
    queue = QueueItem.objects.order_by("id")
    cache.set(QUEUE_KEY, queue)
  c = {'queue': queue}
  c.update(csrf(request))
  return render_to_response('index.html', c)

def add(request):
  item = QueueItem(text=request.POST["text"])
  item.save()
  cache.set(QUEUE_KEY, _get_queue())
  return HttpResponse("<li>%s</li>" % item.text)

def remove(request):
  items = QueueItem.objects.order_by("id")[:1]
  if len(items) != 0:
    items[0].delete()
    cache.set(QUEUE_KEY, _get_queue())
  return redirect("/")

def _get_queue():
  return QueueItem.objects.order_by("id")
