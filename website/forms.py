from django import forms
from django.conf import settings
from django.forms import ModelForm
from django.contrib.auth.models import User

from website.models import *

NUMBER_CHOICES = (
    ('1', u"1"), 
    ('2', u"2"), 
    ('3', u"3"), 
    ('4', u"4"), 
    ('5', u"5"), 
    ('6', u"6"), 
    ('7', u"7"), 
    ('8', u"8"),
) 

class BookingForm(forms.Form):
    tour = forms.ModelChoiceField(queryset=Tour.objects.all())
    your_name = forms.CharField()
    your_email_address = forms.EmailField()
    your_phone_number = forms.CharField()
    number_places_required = forms.ChoiceField(choices=NUMBER_CHOICES, required=True)
     
"""

class AddressAddForm(ModelForm): 
    class Meta:
        model = Address
        exclude = ('owner', 'is_preferred',)
        
            
# handles the submission of their personal details during the order process
class OrderStepOneForm(forms.Form):
    email = forms.EmailField(required=True, 
        error_messages={'required': '* Please give an email address', 'invalid': '* Please enter a valid e-mail address.'})
    first_name = forms.CharField(max_length=200, required=True, error_messages={'required': '* Please give your first name'})
    last_name = forms.CharField(max_length=200, required=True, error_messages={'required': '* Please give your last name'})
    house_name_number = forms.CharField(max_length=200, required=True)
    address_line_1 = forms.CharField(max_length=200, required=False)
    address_line_2 = forms.CharField(max_length=200, required=False)
    town_city = forms.CharField(max_length=200, required=True, error_messages={'required': '* Please provide a town or city name'})
    province_state = forms.CharField(max_length=200, required=False)
    postcode = forms.CharField(max_length=200, required=True)
    country = forms.ChoiceField(required=True, choices=COUNTRY_CHOICES)
    phone = forms.CharField(max_length=80, required=False)
    
    def clean(self):
        
        cleaned_data = self.cleaned_data      
        if cleaned_data.get('province_state'):
            if cleaned_data.get('town_city'):
                sep = ', '
            else:
                cleaned_data['town_city'] = ''
                sep = ''
            
            string = ''.join((sep, cleaned_data.get('province_state')))
            cleaned_data["town_city"] =  ''.join((cleaned_data.get('town_city'), string))
            del cleaned_data['province_state']
           
        
        return cleaned_data

class UpdateDiscountForm(forms.Form):
    discount_code = forms.CharField(required=True)


class MonthlyBoxForm(forms.Form):
    frequency = forms.ChoiceField(required=False, choices=settings.REPEAT_FREQUENCIES)
    tea = forms.ModelChoiceField(required=False, queryset=UniqueProduct.objects.filter(is_active=True, weight="100", 
        currency__code='GBP'), empty_label=None)
    quantity = forms.ChoiceField(required=False, choices=settings.MONTHLY_ORDER_AMOUNTS)
    
    # perhaps if it's a custom package, these fields should be required=True??
    
    

# handles the contact us form
class ContactForm(forms.Form):
    your_name = forms.CharField(required=True)
    your_email = forms.EmailField(required=True, error_messages={'required': 'Please enter a valid email address'})
    your_message = forms.CharField(widget=forms.Textarea, required=False)
    captcha = CaptchaField()

class UpdateProfileForm(forms.Form):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.EmailField(required=False, error_messages={'required': 'Please enter a valid email address'})
  
# the form for submitting a tell-a-friend email address
class TellAFriendForm(forms.Form):
    recipient = forms.EmailField(required=True, error_messages={'required': '* You must give an email address for your friend'})
    sender = forms.EmailField(required=True, error_messages={'required': '* You must give your own email address'})
    message = forms.CharField(required=False, widget=forms.Textarea)

# after the user has finished ordering, handles submission of their twitter username
class SubmitTwitterForm(forms.Form):
    twitter_username = forms.CharField()
    
# handles the testimonials or reviews of a particular tea (views.review)
class ReviewForm(forms.Form):
    text = forms.CharField(required=True, widget=forms.Textarea)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True, error_messages={'required': '* You must give a valid email address'})

class NotifyForm(forms.Form):
    email = forms.EmailField(required=True, error_messages={'required': 'Please enter a valid email address'})
    country = forms.ChoiceField(required=False, choices=all_countries)

class SelectWishlistItemsForm(forms.Form):
    hashkey = forms.CharField()
    items = forms.CharField(required=False)
    

class WishlistSubmitEmailForm(forms.Form):
    email = forms.CharField()
    order = forms.CharField()    
   
    
class CreateSendEmailForm(forms.Form):
    subject_line = forms.CharField(required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)




class ValentinesForm(forms.Form):
    email = forms.EmailField(error_messages={'required': '* Please give an email address', 'invalid': '* Please enter a valid e-mail address.'})
    name = forms.CharField(max_length=200, required=True, error_messages={'required': '* Please give your surname'})
    address_line_1 = forms.CharField(max_length=200, required=False)
    address_line_2 = forms.CharField(max_length=200, required=False)
    town_city = forms.CharField(max_length=200, required=False)
    postcode = forms.CharField(max_length=200, required=False)

"""
