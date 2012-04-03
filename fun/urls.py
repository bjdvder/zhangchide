from django.conf.urls.defaults import *

urlpatterns = patterns('fun.views',
                       (r'^$', 'index'),
                       (r'^guess/$', 'guess'),
                       (r'^guess1/$', 'guess1'),
                       (r'^guess2/$', 'guess2'),
                       (r'^guess3/$', 'guess3'),
                       (r'^drag2upload/$', 'drag2upload'),
                       (r'^j_upload/$', 'j_upload'),                       
                       (r'^hd/$', 'hd'), # happy day
                       (r'^har-view/$', 'har_view'),
                       (r'^dart/$', 'dart'),
                       (r'^dart/notwork$', 'dart_notwork'),
                       (r'^dart/sunflower$', 'dart_sunflower'),
                       (r'^dart/slider$', 'dart_slider'),
                       )
