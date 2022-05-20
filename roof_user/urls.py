from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('logout/', User_logout, name='logout')
]