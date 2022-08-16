from django import forms
from django.forms import ModelForm
from . models import UserProfile


class UserProfileForm(ModelForm):
    """
    The UserProfileForm class defines the user form
    output for the UserProfile model class.
    """
    class Meta:
        """
        The Meta class defines which model is associated and from that model,
        which fields will be accessible to the user.
        """
        model = UserProfile
        fields = ['username', 'name', 'email', 'profile_image', ]
