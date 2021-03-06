from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, authenticate, logout
from .forms import *
from roof_order.models import *


# Create your views here.


class start_page(View):
    def get(self, request):
        form = FastUserForm()
        return render(request, 'roof_pages/start_page.html', context={'form': form})

    def post(self, request):
        form = FastUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('home')
        else:
            return render(request, 'roof_pages/start_page.html', context={'form': form})


def about_page(request):
    return render(request, 'roof_pages/about_page.html')


class profile_page(LoginRequiredMixin, View):
    login_url = 'home'

    def get(self, request):
        user = request.user
        orders = order.objects.filter(user=user.id)
        json_order = []
        for i in orders:
            json_order.append(
                {'size': i.size, 'address': i.address, 'material': materials.objects.get(id=i.materials_id).name,
                 'photo_roof': i.photo_roof})
        context = {'orders': json_order}

        return render(request, 'roof_pages/profile_page.html', context=context)


def material_page(request):
    materials_all = materials.objects.all()
    return render(request, 'roof_pages/material_page.html', context={'materials': materials_all})
