# pages/views.py
from .forms import ClientForm

from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import TemplateView

from pages.models import Client

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

def index(request):
    return render_to_response("pages/index.html", RequestContext(request))

def client_detail(request):
    client = Client.objects.filter(logged_in_user=request.user)[0]
    print(client)
    return render(request, "pages/client_detail.html", {'client':client})

def client_new(request):
    print("DLFKJSDLFKJSD:LFKJDSLFKJ")
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


def client_edit(request):
    print("DLFKJSDLFKJSD:LFKJDSLFKJ")
    client = get_object_or_404(Client)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=post)
        if form.is_valid():
            client.bride_name = form.cleaned_data['bride_name']
            client.groom_name = form.cleaned_data['groom_name']
            client.address = form.cleaned_data['address']
            client.phone_number = form.cleaned_data['phone_number']
            client.logged_in_user = current_user
            client.save()
            return redirect('client_detail')
    else:
        form = ClientForm()
    
    form = ClientForm(request.POST, instance=post)
    form.field['bride_name'].initial = client.bride_name
    form.field['groom_name'].initial = client.groom_name
    form.field['address'].initial = client.address
    form.field['phone_number'].initial = client.phone_number
    return render(request, "pages/client_edit.html", {'form': form})
