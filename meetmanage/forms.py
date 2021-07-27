#!/usr/bin/python3
''' Allow forms from django '''
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="", max_length=50, widget=forms.TextInput(
        attrs={'class': 'fadeIn second', 'placeholder': 'Username'}))
    password = forms.CharField(label="", min_length=8, widget=forms.PasswordInput(
        attrs={'class': 'fadeIn second', 'placeholder': 'Password'}))


class SignUpForm(forms.Form):
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(
        attrs={'class': 'fadeIn second', 'placeholder': 'First name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(
        attrs={'class': 'fadeIn second', 'placeholder': 'Last name'}))
    username = forms.CharField(label="", max_length=50, widget=forms.TextInput(
        attrs={'class': 'fadeIn second', 'placeholder': 'Username'}))
    email = forms.EmailField(label="", max_length=100, widget=forms.TextInput(
        attrs={'class': 'fadeIn second', 'placeholder': 'Email Address'}))
    password = forms.CharField(label="", min_length=8, widget=forms.PasswordInput(
        attrs={'class': 'fadeIn second', 'placeholder': 'Password'}))
