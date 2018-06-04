from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
	username = forms.CharField(label='Username', max_length=64)
	password = forms.CharField(widget=forms.PasswordInput())

class SignupForm(forms.Form):
	username = forms.CharField(label='Username', max_length=64)
	email = forms.CharField(label='Email', max_length=64)
	password = forms.CharField(widget=forms.PasswordInput())