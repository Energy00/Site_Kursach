from django.shortcuts import render, redirect
from django.views import View
from .forms import *


class OrderView(View):
    def get(self, request):
        form = OrderForm()
        return render(request, 'roof_order/order.html', context={'form': form})

    def post(self, request):
        print(request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            order_form = form.save(commit=False)
            order_form.user = request.user
            order_form.save()
            return redirect('home')


