from django import forms
from .models import *


class OrderForm(forms.ModelForm):
    field_order = ['size', 'address', 'materials', 'photo_roof']

    size = forms.IntegerField(label='Размер крыши (примерно)')
    photo_roof = forms.ImageField(label='Фото объекта, если есть', required=False)
    materials = forms.ModelChoiceField(label='Материал',
                                       widget=forms.RadioSelect,
                                       queryset=materials.objects.all())
    address = forms.CharField(label='Адрес')

    class Meta:
        model = order
        exclude = ['user']
