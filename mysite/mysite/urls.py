from django.conf.urls import patterns, include, url
import mysite.views
from django.contrib import admin
import os
admin.autodiscover()

urlpatterns = patterns('',
  url(r'^hello/$', mysite.views.hello),
  url(r'^$', mysite.views.homepage_viewer),
  url(r'^template/$', mysite.views.template_practice),
  url(r'^menu_bar/$', mysite.views.homepage_viewer),
  (r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': os.getcwd() + '/static/'}),
)
