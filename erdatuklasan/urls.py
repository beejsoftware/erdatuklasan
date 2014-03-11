from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'erdatuklasan.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'tuklasansite.views.index'),
    url(r'^tuklas/about', 'tuklasansite.views.about'),
    url(r'^tuklas/programs', 'tuklasansite.views.programs'),
    url(r'^admin/', include(admin.site.urls)),
)
