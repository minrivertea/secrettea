from django.conf import settings
from django.utils import translation



def common(request):
    context = {}
    #context['paypal_return_url'] = settings.PAYPAL_RETURN_URL
    #context['paypal_notify_url'] = settings.PAYPAL_NOTIFY_URL
    #context['paypal_business_name'] = settings.PAYPAL_BUSINESS_NAME
    #context['paypal_receiver_email'] = settings.PAYPAL_RECEIVER_EMAIL
    #context['paypal_submit_url'] = settings.PAYPAL_SUBMIT_URL
    context['ga_is_on'] = settings.GA_IS_ON
    
    context['thumb_large'] = settings.THUMB_LARGE
    context['thumb_medium'] = settings.THUMB_MEDIUM
    context['thumb_small'] = settings.THUMB_SMALL

    context['project_name'] = settings.PROJECT_NAME
    context['project_website'] = settings.PROJECT_WEBSITE
    context['base_template'] = settings.BASE_TEMPLATE
    
    context['static_url'] = settings.STATIC_URL
    context['media_url'] = settings.MEDIA_URL

  
            
    return context
    