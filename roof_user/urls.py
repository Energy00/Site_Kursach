from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register')
]