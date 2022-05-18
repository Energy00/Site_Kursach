from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', OrderView.as_view(), name='order')
]
