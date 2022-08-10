from django import forms
from django.forms import ModelForm
from . models import UserProfile

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'name', 'email', 'profile_image', ]