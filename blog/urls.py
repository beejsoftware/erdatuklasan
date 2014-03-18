from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^review/(?P<review_key>.*)$', 'blog.views.review'),
    (r'^$', 'blog.views.recentfiles'),	
)
