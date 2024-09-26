from django.urls import path
from .views import subscribe
name = 'subscribe'

urlpatterns = [
    path('subscription/', subscribe, name='subscribe'),
]