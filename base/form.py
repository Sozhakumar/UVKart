from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class CustomUserForm(UserCreationForm):
    username= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter username'}))
    email= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your email'}))
    password1= forms.CharField ( widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter password'}))
    password2= forms.CharField ( widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm the password'}))
  
    class Meta:
        model=User
        fields=['username','email','password1','password2']

    