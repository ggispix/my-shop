from django.urls import path
from .views import aboutUs
from django.urls import path
from django.contrib.auth import views as auth_views


name = 'about_us'

urlpatterns = [
    path('', aboutUs, name='index'),
]