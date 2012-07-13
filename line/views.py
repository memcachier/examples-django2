from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, redirect
from line.models import LineItem

def index(request):
  line = LineItem.objects.order_by("id")
  return render_to_response('index.html', {'line': line})

@csrf_exempt
def add(request):
  item = LineItem(text=request.POST["text"])
  item.save()
  return HttpResponse("<li>%s</li>" % item.text)

def remove(request):
  items = LineItem.objects.order_by("id")[:1]
  if len(items) != 0:
    items[0].delete()
  return redirect("/")