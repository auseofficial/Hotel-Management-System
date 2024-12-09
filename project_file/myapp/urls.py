# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.restaurant_list, name='restaurant_list'),  # Updated to show the restaurant list
]
