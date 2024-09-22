from django.urls import path
from .views import index
name = 'products'

urlpatterns = [
    path('', index, name='index'),
]