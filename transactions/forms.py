from django.forms import ModelForm, TextInput
from .models import Category
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CategoryForm(ModelForm):
    
    class Meta:
        model = Category
        fields = ["name",]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название Статьи',
            }),
        }

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', max_length=150)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)