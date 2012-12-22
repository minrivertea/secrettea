from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
    (r'^', include('website.urls')),
    #(r'^reader/', include('creader.urls')),
    #(r'^srs/', include('srs.urls')),
    #(r'^user/', include('users.urls')),

    #url(r'^accounts/register/$', register, {'backend': 'website.regbackend.SimpleBackend',}, name='registration_register'),
    #(r'^accounts/', include('registration.backends.default.urls')),
    (r'^admin/', include(admin.site.urls)),
    #url(r'^(?P<slug>[\w-]+)/$', page, name="page"),
)
