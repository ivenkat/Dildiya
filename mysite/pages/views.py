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
    return render_to_response("pages/index.html",
                              RequestContext(request))

def client_detail(request):
    client = Client.objects.filter(client_id=request.user)[0]
    print(client)
    return render(request, "pages/client_detail.html", {'client':client})

def client_new(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        current_user = request.user
        print("USER ID:" + str(current_user.id))
        if form.is_valid() & current_user.is_authenticated:
            client = form.save(commit=False)
            client.client_id = current_user
            client.save()
            return redirect('client_detail')
    else:
        form = ClientForm()
    return render(request, "pages/client_edit.html", {'form': form})


def client_edit(request):
    client = get_object_or_404(Client)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=post)
        if form.is_valid():
            client = form.save(commit=False)
            client.client_id = current_user
            client.save()
            return redirect('client_detail')
    else:
        form = ClientForm()
    return render(request, "pages/client_edit.html", {'form': form})