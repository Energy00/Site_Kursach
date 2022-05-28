from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('register/', User_register.as_view(), name='register'),
    path('login/', User_login.as_view(), name='login'),
    path('logout/', User_logout, name='logout')
]