import librtmp

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from testapp.forms import UploadFileForm
from django.core.context_processors import csrf
from django.template import RequestContext
# Create your views here.

def home(request):
    return HttpResponse('home.html')

def upload(request):
    if request.method=="POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse("Error occured")
    return render_to_response('upload.html', {'form':UploadFileForm}, context_instance=RequestContext(request))
