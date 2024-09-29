from django.db import models

from cart.models import Cart
from products.models import Product
from django.contrib.auth.models import User
from django.utils import timezone
from products.models import Product
from django import forms


class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

class OrderInfo(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered_date = models.DateTimeField(default= timezone.now())
    final_price = models.DecimalField(max_digits=10, decimal_places=2)

# Create your models here.
