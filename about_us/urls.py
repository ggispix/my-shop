from django.urls import path
from .views import index
name = 'about-us'

urlpatterns = [
    path('', index, name='index'),
]