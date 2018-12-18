from django.urls import include, path
from django.conf.urls import url
from . import views

urlpatterns = [
  path('', views.HomePageView.as_view(), name='home'),
  path('client/new', views.client_new, name='client_new'),
  path('client/edit/', views.client_edit, name='client_edit'),
  path('client/detail/', views.client_detail, name='client_detail'),
  path('background/', views.client_background, name='background'),
  url(r'^$', views.index, name='index'),
]