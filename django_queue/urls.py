from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^add$', 'queue.views.add'),
    url(r'^remove$', 'queue.views.remove'),
    url(r'^$', 'queue.views.index'),
)

urlpatterns += staticfiles_urlpatterns()
