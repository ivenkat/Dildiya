from django import forms
from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import date
from enum import Enum
from phonenumber_field.modelfields import PhoneNumberField

class VendorTypes(Enum):   # A subclass of Enum
    PH = "Photographer"
    VI = "Videographer"
    DE = "Decorator"
    CA = "Caterer"
    BA = "Bartender"

class Client(models.Model):
    client_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bride_name = models.CharField(max_length=200, null = True)
    groom_name = models.CharField(max_length=200, null = True)
    phone_number = PhoneNumberField(null=True, unique=True)
    wedding = models.ForeignKey('Wedding', on_delete=models.CASCADE, null = True)

    def __str__(self):
        return '%s %s %s' % (self.bride_name, self.groom_name, self.client_id.email)

    # Want to make sure theres only one instance of Client - once Client can have one wedding
    # and one logged in user can only create one profile. Once they do it should always update
    # from existing data
    def save(self, *args, **kwargs):
        #if Client.objects.exists() and not self.pk:
        # if you don't check for pk, then error will also raised in update of exists model
            #raise forms.ValidationError('There is can be only one Client instance')
            return super(Client, self).save(*args, **kwargs)

    def has_completed_profile(self):
        # if the user has a completed profile, then they can move on to the next set of questions
        return bride_name != null & groom_name != null & phone_number != null & wedding != null

class Budget(models.Model):
    estimated_total_budget = models.IntegerField()
    actual_amount_spent = models.IntegerField()

class BudgetLineItem(models.Model):
    budget = models.ForeignKey('Budget', default = 1, on_delete=models.CASCADE)
    estimated_price = models.IntegerField()
    contracted_price = models.IntegerField()
    payment_price = models.IntegerField()
    vendor_type = models.CharField(max_length=5,
      choices=[(tag, tag.value) for tag in VendorTypes]
    )  # Choices is a list of Tuple
    client_note = models.CharField(max_length=200)
    due_date = models.DateField(default=date.today)
    payee = models.CharField(max_length=200)
    payment_method = models.CharField(max_length=200)


class Wedding(models.Model):
	name = models.CharField(max_length=200)
	location = models.CharField(max_length=200)
	budget = models.ForeignKey('Budget', default = 1, on_delete=models.CASCADE)
	#Has many events and many vendors but are searched using foregin key in the Event and Vendor models below

class ChecklisTask(models.Model):
	wedding = models.ForeignKey('Wedding', default = 1, on_delete=models.CASCADE)
	description = models.CharField(max_length=200)
	assignee = models.CharField(max_length=200)
	client_note = models.CharField(max_length=200)
	due_date = models.DateField(default=date.today)

class TimelineTask(models.Model):
    time = models.TimeField(null=True)
    description = models.CharField(max_length=200)
    client_note = models.CharField(max_length=200)
    related_vendor = models.CharField(max_length=5,
      choices=[(tag, tag.value) for tag in VendorTypes]
    )
    location = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)
    event = models.ForeignKey('Event', default = 1, on_delete=models.CASCADE)

class Event(models.Model):
    wedding = models.ForeignKey(Wedding, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    date = models.DateField(default=date.today)
    start_time = models.TimeField(default=timezone.now) 
    end_time = models.TimeField(default=timezone.now)

class Vendor(models.Model):
    # A vendor can have multiple weddings, but a wedding can also have multiple Vendors
    weddings = models.ManyToManyField(Wedding)
    company_name = models.CharField(max_length=200)
    vendor_type = models.CharField(max_length=5,
      choices=[(tag, tag.value) for tag in VendorTypes]  # Choices is a list of Tuple
    )
    events = models.ManyToManyField(Event)
    contact_name = models.CharField(max_length=200)
    contact_email = models.CharField(max_length=200)
    contact_phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    #client_note = models.CharField(max_length=200)
    vendor_location = models.CharField(max_length=200)
    booked = models.BooleanField(default=False)
    website = models.CharField(max_length=200)


