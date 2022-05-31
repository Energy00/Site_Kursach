from django import forms
from .models import *
from phonenumber_field.formfields import PhoneNumberField


class FastUserForm(forms.ModelForm):
    field_order = ['name', 'phone_number']

    phone_number = PhoneNumberField(strip=False,
                                    widget=forms.TextInput(attrs={'placeholder': 'Ваш номер телефона'}),
                                    region='RU')
    name = forms.CharField(strip=False,
                           widget=forms.TextInput(attrs={'placeholder': 'Ваше имя'}))

    class Meta:
        model = Fast_formUser
        fields = ('name', 'phone_number')
