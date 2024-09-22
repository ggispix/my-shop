from django.urls import path
from .views import index
name = 'orders'

urlpatterns = [
    path('', index, name='index'),
]