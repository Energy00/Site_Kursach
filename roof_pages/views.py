from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, authenticate, logout
from roof_user.forms import *
from roof_order.models import *

# Create your views here.


class start_page(View):
    def get(self, request):
        reg_form = UserRegForm()
        phone_form = PhoneNumberForm()
        log_form = UserAuthForm()
        context = {
            'reg_form': reg_form,
            'phone_form': phone_form,
            'log_form': log_form
        }
        return render(request, 'roof_pages/start_page.html', context=context)

    def post(self, request):
        phone_form = PhoneNumberForm(request.POST)
        reg_form = UserRegForm(request.POST)
        log_form = UserAuthForm(request.POST)
        context = {
            'reg_form': reg_form,
            'phone_form': phone_form,
            'log_form': log_form
            }
        if reg_form.is_valid():
            user = reg_form.save(commit=True)
            if user.id is not None:
                user_id = User.objects.get(pk=user.id)
                if phone_form.is_valid():
                    phone = phone_form.save(commit=False)
                    phone.user = user_id
                    phone.save()
                    return redirect('login')
                else:
                    return render(request, 'roof_pages/start_page.html', context=context)
        elif log_form.is_valid():
            username = log_form.cleaned_data.get('username_log')
            password = log_form.cleaned_data.get('password_log')
            user = authenticate(email=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'roof_pages/start_page.html', context=context)
        else:
            return render(request, 'roof_pages/start_page.html', context=context)


def about_page(request):
    return render(request, 'roof_pages/about_page.html')


class profile_page(View):
    def get(self, request):
        user = request.user
        orders = order.objects.filter(user=user.id)
        # print(orders)
        # json_order = {}
        # for i in orders:
        #     json_order = {'size': i.size, 'address': i.address, 'material': materials.objects.get(id=i.materials_id).name}
        context = {'orders': orders}
        # print(json_order)

        return render(request, 'roof_pages/profile_page.html', context=context)
