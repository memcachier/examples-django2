from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^add$', 'line.views.add'),
    url(r'^remove$', 'line.views.remove'),
    url(r'^$', 'line.views.index'),
)
