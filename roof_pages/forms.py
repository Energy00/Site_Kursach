from django import forms
from .models import *
from phonenumber_field.formfields import PhoneNumberField


class FastUserForm(forms.ModelForm):
    field_order = ['name', 'phone_number']

    phone_number = PhoneNumberField(label=' ',
                                    strip=False,
                                    widget=forms.TextInput(attrs={'placeholder': 'Телефон'}),
                                    region='RU')
    name = forms.CharField(label=' ',
                           strip=False,
                           widget=forms.TextInput(attrs={'placeholder': 'Имя'}))

    class Meta:
        model = Fast_formUser
        fields = ('name', 'phone_number')
