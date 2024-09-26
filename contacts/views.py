from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse('Contacts Index Page')
# Create your views here.
