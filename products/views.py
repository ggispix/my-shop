from django.shortcuts import render
from .models import Category
def index(request):
    categories = Category().object.all()
    return f'{categories}'
# Create your views here.
