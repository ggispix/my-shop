from django.shortcuts import render
from django.http import HttpResponse
def aboutUs(request):
    return render(request, 'about_us/aboutus.html')
