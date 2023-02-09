from django.db import models
from faker import Faker
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number= PhoneNumberField()
    address =models.TextField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name

class VehicleType(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class VehicleSize(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(VehicleType, related_name=("Type"), on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    real_cost = models.FloatField()
    size = models.ForeignKey(VehicleSize, related_name=("Taille"), on_delete=models.CASCADE)
    
    def _str_(self):
        return self.vehicle_type



class Rental(models.Model):
    rental_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(auto_now_add = True,null=True )
    customer = models.ForeignKey(Customer, related_name=("Customer"), on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, related_name=("Vehicle"), on_delete=models.CASCADE)


    
    
class RentalRate(models.Model):
    daily_rate = models.FloatField()
    type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)

    def _str_(self):
        return self.daily_rate


fake = Faker()
for i in range(10): 
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    phone_number= fake.phone_number()
    address =fake.address()
    city = fake.city()
    country = fake.country()
    customer= Customer(first_name=first_name, last_name=last_name,email=email,phone_number=phone_number,address=address,city=city,country=country)
    customer.save() 
