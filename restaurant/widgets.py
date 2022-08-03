from django.forms import DateInput

class FengyuanChenDatePickerInput(DateInput):
    template_name = 'restaurant/datepicker.html'