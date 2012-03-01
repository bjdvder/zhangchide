from django.conf.urls.defaults import *

urlpatterns = patterns('fun.views',
                       (r'^$', 'index'),
                       (r'^hd/$', 'hd'),
                       (r'^har-view/$', 'har_view'),
                       (r'^dart/$', 'dart'),
                       (r'^dart/notwork$', 'dart_notwork'),
                       (r'^dart/sunflower$', 'dart_sunflower'),
                       (r'^dart/slider$', 'dart_slider'),
                       )
