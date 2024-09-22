from django.urls import path
from .views import index
name = 'cart'

urlpatterns = [
    path('', index, name='index'),
]