from django.conf.urls.defaults import *
from views import *


urlpatterns = patterns('',
    url(r'^$', home, name="home"),
    url(r'^book/$', book, name="book"),
    url(r'^book/confirmed/$', booking_confirmed, name="booking_confirmed"),
    url(r'^tours/$', tours, name="tours"),
    url(r'^tours/(?P<slug>[\w-]+)/$', tour, name="tour"),
    url(r'^gallery/$', galleries, name="galleries"),
    url(r'^gallery/(?P<slug>[\w-]+)/$', gallery, name="gallery"),
    url(r'^gallery/(?P<slug>[\w-]+)/(?P<id>[\w-]+)/$', gallery_image, name="gallery_image"),
)
