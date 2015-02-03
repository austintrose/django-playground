from __future__ import absolute_import
from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views

urlpatterns = patterns('',
    url(r'^$', views.homepage, name="home"),
    url(r'^profile/$', views.profile, name="profile"),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^people/', include('people.urls', namespace="people")),
)
