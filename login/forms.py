from django import forms
from .models import Profile
from django.contrib.auth.models import User


class InformationForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = '__all__'



class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']