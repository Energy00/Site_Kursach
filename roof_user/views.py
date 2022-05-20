from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, authenticate, logout
from .forms import *


# Create your views here.

def User_logout(request):
    logout(request)
    return redirect('home')
