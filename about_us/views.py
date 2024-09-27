from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def aboutUs(request):
    return render(request, 'about_us/aboutus.html')


