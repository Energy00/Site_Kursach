from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', start_page, name='home'),
    path('about/', name='about')
]
