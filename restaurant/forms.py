from django import forms
from django.forms import ModelForm
from .widgets import FengyuanChenDatePickerInput
from .models import Menu, Reservation


class MenuForm(ModelForm):
    """
    The MenuForm class defines the user form output for the Menu model class.
    """
    class Meta:
        """
        The Meta class defines which model is associated and from that model,
        which fields will be accessible to the user.
        """
        model = Menu
        fields = '__all__'


class ReservationForm(ModelForm):
    """
    The ReservationForm class defines the user
    form output for the Reservation model class.
    """
    date = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=FengyuanChenDatePickerInput()
        )

    class Meta:
        """
        The Meta class defines which model is associated and from that model,
        which fields will be accessible to the user.
        """
        model = Reservation
        fields = [
            'name',
            'email',
            'table',
            'number_of_clients',
            'date',
            'time'
        ]
