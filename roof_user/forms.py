from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class UserForm(UserCreationForm):
    field_order = ["email", "password1", "password2", "username"]
    email = forms.CharField(label='Электронная почта',
                            strip=False,
                            widget=forms.EmailInput(attrs={'placeholder': 'Введите свой электронный адрес'}),
                            error_messages={'required': 'Обязательно для заполнения'})

    username = forms.CharField(label='Ваше имя',
                               strip=False,
                               widget=forms.TextInput(attrs={'placeholder': 'Введите свое имя'}),
                               error_messages={'required': 'Обязательно для заполнения'})

    password1 = forms.CharField(label='Пароль',
                                strip=False,
                                widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'placeholder': 'Введите пароль'}),
                                error_messages={'required': 'Обязательно для заполнения'})

    password2 = forms.CharField(label='Повторите пароль',
                                widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
                                strip=False,
                                error_messages={'required': 'Обязательно для заполнения'})

    class Meta:
        model = User
        fields = ("email", "password1", "password2", "username")

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class PhoneNumberForm(forms.ModelForm):
    phone_number = PhoneNumberField(label='Номер телефона',
                                    widget=PhoneNumberPrefixWidget(initial='RU',
                                                                   attrs={
                                                                       'placeholder': 'Введите номер телефона'}),
                                    strip=False)

    class Meta:
        model = User_phones

        fields = ['phone_number']
        exclude = ['user', 'is_blocked']
