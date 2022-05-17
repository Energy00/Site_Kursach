from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, authenticate
from .forms import *


# Create your views here.


class RegisterView(View):

    def get(self, request):
        form = UserRegForm()
        phone_form = PhoneNumberForm()
        context = {
            'form': form,
            'phone_form': phone_form
        }
        return render(request, 'roof_user/register.html', context=context)

    def post(self, request):
        form = UserRegForm(request.POST)
        phone_form = PhoneNumberForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            if user.id is not None:
                user_id = User.objects.get(pk=user.id)
                if phone_form.is_valid():
                    phone = phone_form.save(commit=False)
                    phone.user = user_id
                    phone.save()
                    return redirect('login')
        context = {
            'form': form,
            'phone_form': phone_form
            }
        return render(request, 'roof_user/register.html', context=context)


class LoginForm(View):

    def get(self, request):
        form = UserAuthForm()
        return render(request, 'roof_user/login.html', context={'form': form})

    def post(self, request):
        form = UserAuthForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(email=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'roof_user/login.html', context={'form': form})
        else:
            return render(request, 'roof_user/login.html', context={'form': form})
