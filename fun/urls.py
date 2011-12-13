from django.conf.urls.defaults import *

urlpatterns = patterns('fun.views',
                       (r'^$', 'index'),
                       (r'^hd', 'hd'),
                       (r'^dart/notwork', 'dart_notwork'),
                       (r'^dart/sunflower', 'dart_sunflower'),
                       (r'^dart/slider', 'dart_slider'),
                       )
