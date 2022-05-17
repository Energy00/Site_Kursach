from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from .models import *


class UserForm(UserCreationForm):
    email = forms.CharField(label='Электронная почта',
                            strip=False,
                            widget=forms.EmailInput(attrs={'placeholder': 'Введите свой электронный адрес'}),
                            help_text='Введите электронную почту верно!')
    username = forms.CharField(label='Имя',
                               strip=False,
                               widget=forms.TextInput(attrs={'placeholder': 'Введите свое имя'}))
    password1 = forms.CharField(label='Пароль',
                                strip=False,
                                widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'placeholder': 'Введите пароль'}),
                                help_text='Пароль должен состоять из больших, маленьких символов и из 8 символов')
    password2 = forms.CharField(
        label='Подтвердите пароль',
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text='Введите такой же пароль',
    )

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
                                                                   attrs={'placeholder': 'Введите номер телефона'}),
                                    help_text='Введите верный номер телефона',
                                    strip=False)

    class Meta:
        model = User_phones

        fields = ['phone_number']
        exclude = ['user', 'is_blocked']