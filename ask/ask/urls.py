from django.conf.urls import patterns, include, url
from qa.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
   url(r'^$', index, name='index'),
   url(r'^popular/', popular, name='popular'),
   url(r'^login/', login, name='login'),
   url(r'^signup/', signup, name='signup'),
   url(r'^question/(?P<id>\d+)/', question, name='question'),
   url(r'^ask/', ask_add, name='ask_add'),
   url(r'^answer/', answer_add, name='answer_add'),
   url(r'^new/$','qa.views.test',name='test'),
   url(r'^admin/', admin.site.urls),
   )
