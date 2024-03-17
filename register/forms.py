
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']