from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404
from filetransfers.api import serve_file
from newsletters.models import UploadModel
from newsletters.forms import UploadForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

def files2(request, year):

    events = list(UploadModel.objects.filter(date__year=year).order_by("-date"))
    return render_to_response('files.html',{'events': events},context_instance=RequestContext(request))


def files1(request, year, month):

    events = list(UploadModel.objects.filter(date__year=year, date__month= month).order_by("-date"))
    return render_to_response('files.html',{'events': events},context_instance=RequestContext(request))

def files(request):
	events = UploadModel.objects.all().order_by("-date")
	return render_to_response('files.html',{'events': events},context_instance=RequestContext(request))
	
def recentfiles(request):
	events = UploadModel.objects.all().order_by("-date")[:5]
	return render_to_response('files.html',{'events': events},context_instance=RequestContext(request))

def recentfiles2(request):
	events = UploadModel.objects.all().order_by("-date")[:5]
	return render(request,'files.html',{'events': events})




def download_handler(request, pk):
    upload = get_object_or_404(UploadModel, pk=pk)
    return serve_file(request, upload.file, save_as=True)
	
def download_handler2(request, pk):
    upload = get_object_or_404(UploadModel, pk=pk)
    return serve_file(request, upload.file, save_as=False)