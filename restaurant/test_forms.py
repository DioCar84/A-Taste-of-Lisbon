from django.test import TestCase
from .forms import MenuForm, ReservationForm


class TestMenuForm(TestCase):
    """
    A class for testing the Menu form.
    """

    def test_form_data_input_is_valid(self):
        form = MenuForm(data={
            'title': 'Roast Lamb',
            'description': 'Roast Lamb',
            'dish_type': 2,
            'price': 12.99,
        })

        self.assertTrue(form.is_valid())

    def test_fields_user_has_access_to(self):
        form = MenuForm()
        self.assertEqual(
            form.Meta.fields,
            '__all__'
        )

    def test_title_field_cannot_be_empty(self):
        form = MenuForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_price_field_cannot_be_empty(self):
        form = MenuForm({'price': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors.keys())
        self.assertEqual(form.errors['price'][0], 'This field is required.')

    def test_description_field_cannot_be_empty(self):
        form = MenuForm({'description': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(
            form.errors['description'][0],
            'This field is required.'
        )

    def test_dish_type_field_cannot_be_empty(self):
        form = MenuForm({'dish_type': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('dish_type', form.errors.keys())
        self.assertEqual(
            form.errors['dish_type'][0],
            'This field is required.'
        )


class TestReservationForm(TestCase):
    """
    A class for testing the Reservation form.
    """

    def test_form_data_input_is_valid(self):
        form = ReservationForm(data={
            'email': 'john@email.com',
            'table': 6,
            'number_of_clients': 4,
            'date': '08/22/2022',
            'time': 3,
        })

        self.assertTrue(form.is_valid())

    def test_fields_user_has_access_to(self):
        form = ReservationForm()
        self.assertEqual(
            form.Meta.fields,
            [
                'name',
                'email',
                'table',
                'number_of_clients',
                'date',
                'time'
            ]
        )

    def test_email_field_cannot_be_empty(self):
        form = ReservationForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_table_field_cannot_be_empty(self):
        form = ReservationForm({'table': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('table', form.errors.keys())
        self.assertEqual(form.errors['table'][0], 'This field is required.')

    def test_number_of_clients_field_cannot_be_empty(self):
        form = ReservationForm({'number_of_clients': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('number_of_clients', form.errors.keys())
        self.assertEqual(
            form.errors['number_of_clients'][0],
            'This field is required.'
        )

    def test_date_field_cannot_be_empty(self):
        form = ReservationForm({'date': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('date', form.errors.keys())
        self.assertEqual(form.errors['date'][0], 'This field is required.')

    def test_time_field_cannot_be_empty(self):
        form = ReservationForm({'time': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('time', form.errors.keys())
        self.assertEqual(form.errors['time'][0], 'This field is required.')
