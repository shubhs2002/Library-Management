from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Admin

class AdminSignupForm(UserCreationForm):
    class Meta:
        model = Admin
        fields = ('username', 'email', 'password1', 'password2')
