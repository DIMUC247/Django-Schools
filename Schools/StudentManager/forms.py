from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import MySuperStudent
from django import forms


class  SignUpForm(UserCreationForm):
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Логін",
        help_text="Введіть імя користувача, максимум 50 символів"
    )
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}), label="Ім'я")
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}), label="Прізвище")
    phone_number = forms.CharField(required=False,max_length=15, widget=forms.TextInput(attrs={"class": "form-control"}), label="Номер телефону")
    address = forms.CharField(required=False,max_length=250, widget=forms.TextInput(attrs={"class": "form-control"}), label="Адреса")
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={"class": "form-control"}), label="Пароль")
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={"class": "form-control"}), label="Підтвердження пароля")

    class Meta:
        model = MySuperStudent
        fields = ("username", "first_name", "last_name", "phone_number", "address", "password1", "password2",)

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Логін", widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-control"}))