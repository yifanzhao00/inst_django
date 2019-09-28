from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from inst.models import InstUser

# forms defined here handles user inputs

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = InstUser
        fields = ('username', 'email', 'profile_pic')