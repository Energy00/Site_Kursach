from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login
from .forms import *


# Create your views here.


class RegisterView(View):

    def get(self, request):
        form = UserForm()
        phone_form = PhoneNumberForm()
        context = {
            'form': form,
            'phone_form': phone_form
        }
        return render(request, 'roof_user/register.html', context=context)

    def post(self, request):
        form = UserForm(request.POST)
        phone_form = PhoneNumberForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            if user.id is not None:
                user_id = User.objects.get(pk=user.id)
                if phone_form.is_valid():
                    phone = phone_form.save(commit=False)
                    phone.user = user_id
                    phone.save()
                    return redirect('home')
        context = {
            'form': form,
            'phone_form': phone_form
            }
        return render(request, 'roof_user/register.html', context=context)

