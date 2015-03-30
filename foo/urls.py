from foo.views import *
from django.conf.urls import patterns, url

urlpatterns = patterns('',
                        url(r'^$', 'foo.views.home', name='home'),
                        url(r'^logout/$', 'foo.views.logout', name='logout'),
                        )