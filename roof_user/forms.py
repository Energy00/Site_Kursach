from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class UserRegForm(UserCreationForm):
    field_order = ["email", "password1", "password2", "username"]
    email = forms.CharField(strip=False,
                            widget=forms.EmailInput(attrs={'placeholder': 'Электронная почта'}),
                            error_messages={'required': 'Обязательно для заполнения'})

    username = forms.CharField(strip=False,
                               widget=forms.TextInput(attrs={'placeholder': 'Ваше имя'}),
                               error_messages={'required': 'Обязательно для заполнения'})

    password1 = forms.CharField(strip=False,
                                widget=forms.PasswordInput(
                                    attrs={"autocomplete": "new-password", 'placeholder':'Пароль'}),
                                error_messages={'required': 'Обязательно для заполнения'})

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"autocomplete": "new-password",
                                                                  'placeholder':'Повторите пароль'}),
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
    phone_number = PhoneNumberField(strip=False,
                                    widget=forms.NumberInput(attrs={'placeholder': 'Номер телефона'}),
                                    region='RU')

    class Meta:
        model = User_phones

        fields = ['phone_number']
        exclude = ['user', 'is_blocked']


class UserAuthForm(forms.Form):
    field_order = ['username_log', 'password_log']
    username_log = forms.CharField(strip=False,
                                   widget=forms.EmailInput(
                                       attrs={'placeholder': 'Электронная почта'}))

    password_log = forms.CharField(strip=False,
                                   widget=forms.PasswordInput(
                                       attrs={"autocomplete": "new-password", 'placeholder': 'Пароль'}))
