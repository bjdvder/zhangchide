from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       (r'^$', 'start.views.index'),
                       (r'^works/$', 'start.views.works'),
    # Example:
    # (r'^zchome/', include('zchome.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)

if settings.LOCAL_DEV:
    urlpatterns += patterns(
        '',
        # (r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/img/favicon.ico'}),
        # (r'^js/(.*)$', 'django.views.static.serve', {'document_root':'./public/js'}),
        # (r'^css/(.*)$', 'django.views.static.serve', {'document_root':'./public/css'}),
        # (r'^img/(.*)$', 'django.views.static.serve', {'document_root':'./public/img'}),
        )

handler404 = 'start.views.not_found'
