# pages/views.py
from .forms import ClientForm, BackgroundDetailsForm

from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from django.template import RequestContext
from django.views.generic import TemplateView

from pages.models import Client

class HomePageView(TemplateView):
  template_name = 'pages/home.html'

def index(request):
  return render_to_response("pages/index.html", RequestContext(request))

def client_detail(request):
  client = Client.objects.filter(logged_in_user=request.user)[0]
  return render(request, "pages/client_detail.html", {'client':client})

# Creating a new client
def client_new(request):
  if request.method == "POST":
    form = ClientForm(request.POST)
    current_user = request.user
    print("USER ID:" + str(current_user.id))
    if form.is_valid() & current_user.is_authenticated:
      client = form.save(commit=False)
      client.logged_in_user = current_user
      client.save()
      return redirect('client_detail')
  else:
    form = ClientForm()
    
  return render(request, "pages/client_edit.html", {'form': form})

# Editing an old client. If no client was found, a 404 error will be returned. If a client was found
# we will edit the existing client values.
# TODO: figure out how to update the form with the pre-existing values
def client_edit(request):
  client = get_object_or_404(Client, logged_in_user=request.user)
  current_user = request.user
  if request.method == "POST":
    form = ClientForm(request.POST)
    if form.is_valid() & current_user.is_authenticated:
      client.bride_name = form.cleaned_data['bride_name']
      client.groom_name = form.cleaned_data['groom_name']
      client.phone_number = form.cleaned_data['phone_number']
      client.address = form.cleaned_data['address']
      client.save()
      return redirect('client_detail')
  else:
    form = ClientForm()
    
  # Set the defaults if they already exist. If not, leave blank.
  form.fields['bride_name'].initial = client.bride_name
  form.fields['groom_name'].initial = client.groom_name
  form.fields['phone_number'].initial = client.phone_number
  form.fields['address'].initial = client.address
  print ("FORM FORM: %s" % form)
  return render(request, "pages/client_edit.html", {'form': form})

def client_background(request):
  current_user = request.user
  client = get_object_or_404(Client, logged_in_user=current_user)
  print ("CLIENT: %s" % client)
  print ("LOGGED IN USER: %s" % client.logged_in_user)
  if request.method == "POST":
    form = BackgroundDetailsForm(request.POST)
    if form.is_valid() & current_user.is_authenticated:
      client.background = form.cleaned_data['background']
      client.save()
      return redirect('client_detail')
  else:
    form = BackgroundDetailsForm(initial={
    'background': client.background
  })
    
  print ("FORM FORM: %s" % form)
  print ("BACKGOROUND: %s" % client.background)
  form.fields['background'].initial = client.background
  return render(request, "pages/client_edit.html", {'form': form})

