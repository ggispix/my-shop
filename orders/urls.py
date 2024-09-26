from django.urls import path
from .views import checkout
name = 'orders'

urlpatterns = [
    path('checkout/', checkout, name='checkout'),
]