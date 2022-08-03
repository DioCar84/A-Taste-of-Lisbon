from django import forms
from django.forms import ModelForm
from .models import Menu, Reservation
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['first_name', 'last_name', 'email', 'total_people', 'date', 'time']
