from django.shortcuts import render, redirect
from django.views import View
from .forms import *


class OrderView(View):
    def get(self, request):
        form = OrderForm()
        return render(request, 'roof_order/order.html', context={'form': form})

    def post(self, request):
        print(request.POST['materials'])
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            materials_id = request.POST['materials']
            materials_id = materials.objects.get(pk=materials_id)
            print(materials_id)
            order_form = form.save(commit=False)
            order_form.materials = materials_id
            order_form.user = request.user
            order_form.save()
            return redirect('profile')
        else:
            return render(request, 'roof_order/order.html', context={'form': form})


