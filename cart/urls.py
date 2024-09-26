from django.urls import path
from .views import add_to_cart,cart_view
name = 'cart'

urlpatterns = [
    path('cart/', cart_view, name='index'),
    path('add_to_cart/<int:product_id>/',add_to_cart, name='add_to_cart'),
]
