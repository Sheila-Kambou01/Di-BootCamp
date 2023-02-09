from django.shortcuts import render,redirect
from faker import Faker
from rent.models import Rental
from rent.models import Customer


def all_rental(request):
    rental = Rental.objects.all()
    return render(request, 'rent/index.html', {"rental":rental})

def all_customer(request):
    customer = Customer.objects.all()
    return render(request, 'rent/customer .html', {"customer":customer})

