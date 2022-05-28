from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Fast_formUser(models.Model):

    name = models.CharField(max_length=128, blank=False, null=False)
    phone_number = PhoneNumberField(unique=True, blank=False, null=False, region='RU')

