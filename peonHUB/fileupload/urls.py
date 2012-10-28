from django.conf.urls.defaults import *
from fileupload.views import *
#from fileupload.views import PictureCreateView, PictureDeleteView, gallery

urlpatterns = patterns('fileupload.views',
    (r'^new/$', PictureCreateView.as_view(), {}, 'upload-new'),
    (r'^list/$', gallery),
    #(r'^list/$', gallery),
    (r'^delete/(?P<pk>\d+)$', PictureDeleteView.as_view(), {}, 'upload-delete'),
)

