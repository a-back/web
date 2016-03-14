from django.conf.urls import patterns, include, url
from qa.views import test, index, question, popular, ask_add, answer_add

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
   url(r'^popular/', popular, name='popular'),
   url(r'^$', index, name='index'),
   url(r'^login/$','qa.views.test',name='test'),
   url(r'^signup/$','qa.views.test',name='test'),
   url(r'^question/(?P<id>\d+)/', question, name='question'),
   url(r'^ask/', ask_add, name='ask_add'),
   url(r'^answer/', answer_add, name='answer_add'),
   url(r'^new/$','qa.views.test',name='test'),
   )
