from django import forms
from django.forms import ModelForm
from .widgets import FengyuanChenDatePickerInput
from .models import Menu, Reservation


class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'


class ReservationForm(ModelForm):
    date = forms.DateField(input_formats=['%d/%m/%Y'], widget=FengyuanChenDatePickerInput())
    
    class Meta:
        model = Reservation
        fields = ['first_name', 'last_name', 'email', 'total_people', 'date', 'time', ]
