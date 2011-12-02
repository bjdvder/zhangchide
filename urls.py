from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       (r'^$', 'start.views.index'),
                       (r'^works/$', 'start.views.works'),
                       (r'^fun/', include('fun.urls')),
    # Example:
    # (r'^zchome/', include('zchome.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)

if settings.LOCAL_DEV:
    urlpatterns += patterns(
        'django.views',
        (r'^favicon\.ico$', 'generic.simple.redirect_to', {'url': '/img/favicon.ico'}),
        (r'^img/(.*)$', 'static.serve', {'document_root': './public/img'}),
        (r'^js/(.*)$', 'static.serve', {'document_root': './public/js'}),
        (r'^css/(.*)$', 'static.serve', {'document_root': './public/css'}),
        )

# handler404 = 'start.views.not_found'
