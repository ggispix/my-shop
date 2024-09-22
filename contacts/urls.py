from django.urls import path
from .views import index
name = 'contacts'

urlpatterns = [
    path('', index, name='index'),
]