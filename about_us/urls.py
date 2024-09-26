from django.urls import path
from .views import aboutUs
name = 'about_us'

urlpatterns = [
    path('', aboutUs, name='index'),
]