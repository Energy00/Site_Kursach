from django.shortcuts import render

# Create your views here.


def start_page(request):
    return render(request, 'roof_pages/start_page.html')


def about_page(request):
    return render(request, 'roof_pages/about_page.html')