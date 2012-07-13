from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, redirect
from line.models import LineItem
from django.core.cache import cache
import time

LINE_KEY = "line"

def index(request):
  line = cache.get(LINE_KEY)
  if not line:
    time.sleep(2) # simulate a slow query.
    line = _get_line()
    cache.set(LINE_KEY, line)
  return render_to_response('index.html', {'line': line})

@csrf_exempt
def add(request):
  item = LineItem(text=request.POST["text"])
  item.save()
  cache.set(LINE_KEY, _get_line())
  return HttpResponse("<li>%s</li>" % item.text)

def remove(request):
  items = LineItem.objects.order_by("id")[:1]
  if len(items) != 0:
    items[0].delete()
    cache.set(LINE_KEY, _get_line())
  return redirect("/")
  
def _get_line():
  return LineItem.objects.order_by("id")