from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^add$', 'line.views.add'),
    url(r'^remove$', 'line.views.remove'),
    url(r'^$', 'line.views.index'),
)

urlpatterns += staticfiles_urlpatterns()
