from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class materials(models.Model):
    name = models.CharField(max_length=40, null=False)
    photo = models.ImageField(upload_to='img/materials_photo/', null=False)
    price = models.IntegerField(null=False)
    description = models.TextField()


class order(models.Model):
    user = models.ForeignKey(User, blank=True, null=False, on_delete=models.CASCADE)
    materials = models.ForeignKey(materials, blank=True, null=False, on_delete=models.CASCADE)
    address = models.CharField(max_length=128, blank=False, null=False)
    size = models.IntegerField(blank=True, null=False)
    photo_roof = models.ImageField(upload_to='img/roof_photo/', null=True, blank=True)
