from django import forms

from .models import Client

class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('bride_name',
        	'groom_name',
        	'address',
        	'phone_number')