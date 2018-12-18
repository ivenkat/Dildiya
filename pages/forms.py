from django import forms

from .models import Client, Background
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

  def __init__(self, *args, **kwargs):
        
    super(BackgroundDetailsForm, self).__init__(*args, **kwargs)
    Background.objects.bulk_create([
    	Background(culture="Tamil"),
    	Background(culture="Gujurati")])
        
    self.fields["background"].widget = CheckboxSelectMultiple()
    self.fields["background"].queryset = Background.objects.all()
