from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404
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


    

# the homepage view
def home(request):
    
    return _render(request, "website/home.html", locals())


def tours(request):
    
    return _render(request, 'website/tours.html', locals())
    

def tour(request, slug):
    
    return _render(request, 'website/tour.html', locals())
    

def gallery(request):
    
    return _render(request, 'website/gallery.html', locals())


def gallery_image(request, id):
    
    return _render(request, 'website/gallery_image.html', locals())

