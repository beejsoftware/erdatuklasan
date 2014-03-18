from django.conf import settings
from django.conf.urls.defaults import *
from blog.models import PostsSitemap
from minicms.models import PagesSitemap
from django.contrib import admin
import dbindexer

handler500 = 'djangotoolbox.errorviews.server_error'

# django admin
admin.autodiscover()

# search for dbindexes.py in all INSTALLED_APPS and load them
dbindexer.autodiscover()

sitemaps = {
    'posts': PostsSitemap,
    'pages': PagesSitemap,
}

urlpatterns = patterns('',
    ('^admin/', include(admin.site.urls)),
    (r'^newsletters/', include('newsletters.urls')),
    #('^$', 'django.views.generic.simple.direct_to_template', {'template': 'home.html'}),##
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps}),
    (r'^search$', 'google_cse.views.search'),
    (r'^robots\.txt$', 'robots.views.robots'),

    (r'^$', 'tuklasansite.views.index'),
    (r'^tuklas/about', 'tuklasansite.views.about'),
    (r'^tuklas/programs', 'tuklasansite.views.programs'),
)

if 'djangoappengine' in settings.INSTALLED_APPS:
    urlpatterns = patterns('',
        ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    ) + urlpatterns
