from django.conf.urls.defaults import *
from views import *


urlpatterns = patterns('',
    url(r'^$', home, name="home"),
    url(r'^tours/$', tours, name="tours"),
    url(r'^tours/(?P<slug>[\w-]+)/$', tour, name="tour"),
    url(r'^gallery/$', gallery, name="gallery"),
    url(r'^gallery/(?P<slug>[\w-]+)/$', gallery_image, name="gallery_image"),
)
