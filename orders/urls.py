from django.urls import path
from .views import checkout, order_checkout, order_success, payment_view,payment_succeed
app_name = 'orders'
app_name ='order_success'
urlpatterns = [
    path('checkout/', checkout, name='checkout'),  # Checkout page
    path('success/<int:order_id>/', order_success, name='order_success'),  # Order success with order_id
    path('order/checkout/', order_checkout, name='order_checkout'),
    path('payment/', payment_view, name='payment'),
    path('payment-succeed/', payment_succeed, name='payment-succeed'),
]