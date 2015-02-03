from __future__ import absolute_import
from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views

urlpatterns = patterns('',
    url(r'^$', views.list_people, name="list_people"),
    url(r'^(?P<person_id>\d+)/$', views.person_detail,
        name="person_detail"),
    url(r'^(?P<person_id>\d+)/edit/$', views.edit_person,
        name="edit_person"),
    url(r'^add/$', views.add_person, name="add_person"),
)
