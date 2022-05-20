from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class UserRegForm(UserCreationForm):
    field_order = ["email", "password1", "password2", "username"]
    email = forms.CharField(label='Электронная почта',
                            strip=False,
                            error_messages={'required': 'Обязательно для заполнения'})

    username = forms.CharField(label='Ваше имя',
                               strip=False,
                               error_messages={'required': 'Обязательно для заполнения'})

    password1 = forms.CharField(label='Пароль',
                                strip=False,
                                widget=forms.PasswordInput(
                                    attrs={"autocomplete": "new-password"}),
                                error_messages={'required': 'Обязательно для заполнения'})

    password2 = forms.CharField(label='Повторите пароль',
                                widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
                                strip=False,
                                error_messages={'required': 'Обязательно для заполнения'})

    class Meta:
        model = User
        fields = ("email", "password1", "password2", "username")

    def save(self, commit=True):
        user = super(UserRegForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class PhoneNumberForm(forms.ModelForm):
    phone_number = PhoneNumberField(label='Номер телефона',
                                    initial='+7',
                                    strip=False)

    class Meta:
        model = User_phones

        fields = ['phone_number']
        exclude = ['user', 'is_blocked']


class UserAuthForm(forms.Form):
    field_order = ['username_log', 'password_log']
    username_log = forms.CharField(label='Электронная почта',
                                   strip=False,
                                   widget=forms.EmailInput())

    password_log = forms.CharField(label='Пароль',
                                   strip=False,
                                   widget=forms.PasswordInput(
                                       attrs={"autocomplete": "new-password"}))
