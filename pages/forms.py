from django import forms

from .models import Client
from django.forms.widgets import CheckboxSelectMultiple

class ClientForm(forms.ModelForm):
  class Meta:
    model = Client
    fields = (
    	'bride_name',
     	'groom_name',
       	'phone_number',
       	'address')

class BackgroundDetailsForm(forms.ModelForm):
  class Meta:
    model = Client
    fields = ('background',)
