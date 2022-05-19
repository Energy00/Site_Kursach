from django.shortcuts import render
from django.views import View

from roof_order.models import *
# Create your views here.


def start_page(request):
    return render(request, 'roof_pages/start_page.html')


def about_page(request):
    return render(request, 'roof_pages/about_page.html')


class profile_page(View):
    def get(self, request):
        user = request.user
        orders = order.objects.filter(user=user.id) #или user.id
        # print(orders)
        # json_order = {}
        # for i in orders:
        #     json_order = {'size': i.size, 'adress': i.address, 'material': materials.objects.get(id=i.materials_id).name}
        context = {'orders': orders}
        # print(json_order)

        return render(request, 'roof_pages/profile_page.html', context=context)
