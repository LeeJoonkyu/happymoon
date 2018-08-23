from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import (authenticate,get_user_model,login,logout,)


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'email', 'placeholder': '이메일'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password', 'placeholder': '비밀번호'}))