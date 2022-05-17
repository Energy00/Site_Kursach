from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
# Create your models here.


class User_phones(models.Model):

    phone_number = PhoneNumberField(unique=True, blank=False, null=False, region='RU')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_blocked = models.BooleanField(default=False)
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
