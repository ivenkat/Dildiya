from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
  path('signup/', views.SignUp.as_view(), name='signup'),
]