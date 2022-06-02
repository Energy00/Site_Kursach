from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from .forms import *


class OrderView(LoginRequiredMixin, View):
    login_url = 'home'

    def get(self, request):
        form = OrderForm()
        form.fields['materials'].queryset = materials.objects.values_list('name', flat=True)
        return render(request, 'roof_order/order.html', context={'order_form': form})

    def post(self, request):
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.POST)
            materials_id = request.POST['materials']
            materials_id = materials.objects.get(pk=materials_id)
            order_form = form.save(commit=False)
            order_form.materials = materials_id
            order_form.user = request.user
            order_form.save()
            return redirect('profile')
        else:
            form.fields['materials'].queryset = materials.objects.values_list('name', flat=True)
            return render(request, 'roof_order/order.html', context={'order_form': form})


