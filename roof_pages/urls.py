from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', start_page, name='home'),
    path('about/', about_page, name='about'),
    path('profile/', profile_page.as_view(), name='profile')
]
