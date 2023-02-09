from django import views
from django.urls import path 
from . import views
urlpatterns = [
    path('', views.all_rental, name='all_rental'),
    path('customer', views.all_customer, name='all_customer'),
]

