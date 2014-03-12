from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response, render, get_object_or_404
from django.http import Http404
from django.views import generic
from django.template import RequestContext



from tuklasansite.models import AboutPage
# Create your views here.
def index(request):
    return render_to_response('tuklasansite/index.html', context_instance=RequestContext(request))


def about(request):


    p = get_object_or_404(AboutPage, title='About Erda Tuklasan')
    return render_to_response('tuklasansite/about.html',{'About':p}, context_instance=RequestContext(request))




def programs(request):
    return render_to_response('tuklasansite/program.html', context_instance=RequestContext(request))

