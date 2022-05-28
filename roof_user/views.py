from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, authenticate, logout
from .forms import *


# Create your views here.
class User_register(View):

    def post(self, request):
        phone_form = PhoneNumberForm(request.POST)
        reg_form = UserRegForm(request.POST)
        if reg_form.is_valid() and phone_form.is_valid():
            user = reg_form.save(commit=True)
            print(user.id)
            if user.id is not None:
                user_id = User.objects.get(pk=user.id)
                phone = phone_form.save(commit=False)
                phone.user = user_id
                phone.save()
                login(request, user, backend='roof_user.backends.EmailBackend')
                data = {
                    'email': reg_form.cleaned_data['email'],
                    'username': reg_form.cleaned_data['username'],
                    'password1': reg_form.cleaned_data['password1'],
                    'password2': reg_form.cleaned_data['password2'],
                    'phone': str(phone.phone_number)
                }
                return JsonResponse({'success': data})
        else:
            return JsonResponse({'errors_reg': reg_form.errors, 'errors_num': phone_form.errors})


class User_login(View):

    def post(self, request):
        log_form = UserAuthForm(request.POST)
        if log_form.is_valid():
            username = log_form.cleaned_data.get('username_log')
            password = log_form.cleaned_data.get('password_log')
            user = authenticate(email=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse(data={})
            else:
                return JsonResponse(data={'error': 'Неверная почта или пароль'}, status=404)
        else:
            return JsonResponse(data={'error': 'Введите почту и пароль'}, status=404)


def User_logout(request):
    logout(request)
    return redirect('home')
