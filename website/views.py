from django.conf import settings
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMultiAlternatives
from django.core.urlresolvers import reverse
from django.utils import simplejson
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.translation import ugettext as _
from django.utils.translation import get_language
from django.core.exceptions import MultipleObjectsReturned


import urllib
import urllib2
import xml.etree.ElementTree as etree
from django.utils import simplejson

from PIL import Image
from cStringIO import StringIO
import os
import datetime
from datetime import timedelta
import uuid
import re


from utils import _render
from website.models import *
from website.forms import BookingForm

    

# the homepage view
def home(request):
    tours = Tour.objects.filter()
    photos = GalleryImage.objects.all().order_by('?')[:4]
    return _render(request, "website/home.html", locals())

def book(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # do something here
            
            return HttpResponseRedirect(reverse('booking_confirmed'))
        else:
            form = BookingForm(request.POST)
    else:
        form = BookingForm()
    return _render(request, 'website/book.html', locals())

def booking_confirmed(request):
    return _render(request, 'website/booking_confirmed.html', locals())


def tours(request):
    tours = Tour.objects.filter()
    return _render(request, 'website/tours.html', locals())
    

def tour(request, slug):
    tour = get_object_or_404(Tour, slug=slug)
    return _render(request, 'website/tour.html', locals())
    

def galleries(request):
    tours = Tour.objects.filter()
    return _render(request, 'website/galleries.html', locals())

def gallery(request, slug):
    tour = get_object_or_404(Tour, slug=slug)
    first = tour.get_photos()[0]
    return HttpResponseRedirect(reverse('gallery_image', args=[tour.slug, first.id]))


def gallery_image(request, slug, id):
    image = get_object_or_404(GalleryImage, pk=id)
    try:
        next = get_object_or_404(GalleryImage, pk=(image.id+1), tour=image.tour)
    except:
        next = None
    
    try:
        prev = get_object_or_404(GalleryImage, pk=(image.id-1), tour=image.tour)
    except:
        prev = None
    return _render(request, 'website/gallery_image.html', locals())


def page(request, slug):
    page = get_object_or_404(Page, slug=slug)
    
    return _render(request, 'website/page.html', locals())

