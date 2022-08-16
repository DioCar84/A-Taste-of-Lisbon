from django.forms import DateInput

class FengyuanChenDatePickerInput(DateInput):
    """
    The FengyuanChenDatePickerInput class inherits from the DateInput class,
    it is then associated to a template which will define how it will be displayed.
    """
    template_name = 'restaurant/datepicker.html'