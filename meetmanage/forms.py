#!/usr/bin/python3
''' Allow forms from django '''
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label="", max_length=50, widget=forms.TextInput(
        attrs={'class': 'fadeIn second', 'placeholder': 'Username'}))
    password = forms.CharField(label="", min_length=8, widget=forms.PasswordInput(
        attrs={'class': 'fadeIn second', 'placeholder': 'Password'}))


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="", max_length=100, widget=forms.TextInput(
        attrs={'class': 'fadeIn second', 'placeholder': 'Email Address'}))

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email"]
        widgets = {'first_name': forms.TextInput(attrs={'type': 'text', 'class': 'fadeIn second', 'placeholder': 'First name'}),
                   'last_name': forms.TextInput(attrs={'class': 'fadeIn second', 'placeholder': 'Last name'}),
                   'username': forms.TextInput(attrs={'type': 'text', 'class': 'fadeIn second', 'placeholder': 'Username'}),
                   'email': forms.TextInput(attrs={'type': 'email', 'class': 'fadeIn second', 'placeholder': 'Email'}),}

#                   'password': forms.TextInput(attrs={'type': 'pasword', 'class': 'fadeIn second', 'placeholder': 'Password'}),}
        help_texts = {'username': "", 'password2': ""}

        labels = {'first_name': "",
                  'last_name': "",
                  'username': "",
                  'email': "",
                  'password1': "",
                  'password2': ""}
