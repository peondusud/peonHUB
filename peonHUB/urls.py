#from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'upload.views.home', name='home'),
    url(r'^upload/', include('fileupload.urls')),
    url(r'^accounts/', include('registration.urls')),
    #url(r'^admin/(.*)', admin.site.root),
    url(r'^accounts/', include('registration.urls')),
    url(r'^$', direct_to_template, 
            { 'template': 'index.html' }, 'index'),
    url(r'^admin/', include(admin.site.urls)),
)

import os
urlpatterns += patterns('',
        (r'^media/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.abspath(os.path.dirname(__file__)), 'media')}),
)
