from django import forms
from django.contrib.auth.models import User

class LoginFormAdmin(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Email','class':'input100'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password', 'class':'input100'}))
    fields = ['username', 'password']