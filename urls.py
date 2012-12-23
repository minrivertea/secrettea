from django.conf.urls.defaults import *
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

from website.views import page

urlpatterns = patterns('',
    (r'^', include('website.urls')),
    #(r'^reader/', include('creader.urls')),
    #url(r'^accounts/register/$', register, {'backend': 'website.regbackend.SimpleBackend',}, name='registration_register'),
    #(r'^accounts/', include('registration.backends.default.urls')),
    (r'^admin/', include(admin.site.urls)),
    url(r'^(?P<slug>[\w-]+)/$', page, name="page"),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

