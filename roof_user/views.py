from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth import login
from .forms import *
# Create your views here.


class RegisterView(View):

    def get(self, request):
        form = UserForm(request.POST)
        phone_form = PhoneNumberForm(request.POST)
        context = {
            'form': form,
            'phone_form': phone_form
        }
        return render(request, 'roof_user/register.html', context=context)

    def post(self, request):
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)