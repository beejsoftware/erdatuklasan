


from django.conf.urls.defaults import *

from django.shortcuts import get_object_or_404
urlpatterns = patterns('newsletters.views',
    (r'^newsletters/(\d+)/(\d+)/$', 'files1'),
    (r'^newsletters/(\d+)/$', 'files2'),	
    (r'^newsletters/$', 'recentfiles2'),	
    (r'^download/(?P<pk>.+)$', 'download_handler'),
    (r'^download2/(?P<pk>.+)$', 'download_handler2'),
)
