from fileupload.models import Picture
from django.views.generic import CreateView, DeleteView
from django.contrib.auth.decorators import login_required
import os
PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))
MEDIA_ROOT =os.path.join(PROJECT_ROOT, '/media/pictures')

from django.http import HttpResponse, HttpResponseRedirect
from django.utils import simplejson
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response

from django.conf import settings

def response_mimetype(request):
    if "application/json" in request.META['HTTP_ACCEPT']:
        return "application/json"
    else:
        return "text/plain"
@login_required
def gallery(request):
    path=os.path.realpath(os.path.dirname(__file__))
    #file_list=os.listdir(os.path.join(path, '/media/pictures/'))
    file_list=os.listdir("/home/peon/peonHUB/peonHUB/media/pictures/")
    return render_to_response('list2.html', {'files': file_list})


class PictureCreateView(CreateView):
    model = Picture


    def form_valid(self, form):
        self.object = form.save()
        f = self.request.FILES.get('file')
        data = [{'name': f.name, 'url': settings.MEDIA_URL + "pictures/" + f.name.replace(" ", "_"), 'thumbnail_url': settings.MEDIA_URL + "pictures/" + f.name.replace(" ", "_"), 'delete_url': reverse('upload-delete', args=[self.object.id]), 'delete_type': "DELETE"}]
        response = JSONResponse(data, {}, response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response


class PictureDeleteView(DeleteView):
    model = Picture


    def delete(self, request, *args, **kwargs):

        self.object = self.get_object()
        self.object.file.delete()
        self.object.delete(save=False)
        #os.remove(path)
        if request.is_ajax():
            response = JSONResponse(True, {}, response_mimetype(self.request))
            response['Content-Disposition'] = 'inline; filename=files.json'
            return response
        else:
            return HttpResponseRedirect('/upload/new')

class JSONResponse(HttpResponse):
    """JSON response class."""
    def __init__(self,obj='',json_opts={},mimetype="application/json",*args,**kwargs):
        content = simplejson.dumps(obj,**json_opts)
        super(JSONResponse,self).__init__(content,mimetype,*args,**kwargs)
