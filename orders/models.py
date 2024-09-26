from django.db import models
from products.models import Product
from django.contrib.auth.models import User
from django.utils import timezone
from django import forms

class Order(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered_date = models.DateTimeField(default= timezone.now())
    final_price = models.DecimalField(max_digits=10, decimal_places=2)



# Create your models here.
