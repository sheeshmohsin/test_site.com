from django.shortcuts import render, render_to_response
from testapp.forms import UploadFileForm
from django.core.context_processors import csrf
from django.template import RequestContext
# Create your views here.

def upload(request):
	return render_to_response('upload.html', {'form':UploadFileForm}, context_instance=RequestContext(request))
