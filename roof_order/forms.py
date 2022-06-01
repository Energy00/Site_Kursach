from django import forms
from .models import *


class OrderForm(forms.ModelForm):
    field_order = ['size', 'address', 'materials', 'photo_roof']

    size = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Размер крыши(примерно)',
                                                              'class': 'form-control intup__size'}))
    photo_roof = forms.ImageField(required=False,
                                  widget=forms.FileInput(attrs={'class': 'intup__file'}))
    materials = forms.ModelChoiceField(label='Материал',
                                       widget=forms.RadioSelect,
                                       queryset=materials.objects.all())
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Адрес',
                                                            'class': 'form-control intup__size'}))

    class Meta:
        model = order
        exclude = ['user']
