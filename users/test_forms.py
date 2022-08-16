from django.test import TestCase
from .forms import UserProfileForm


class TestUserProfileForm(TestCase):
    """
    A class for testing the user profile form.
    """

    def test_form_data_input_is_valid(self):
        form = UserProfileForm(data={
            'name': 'John',
            'username': 'John123',
            'email': 'john@email.com'
        })

        self.assertTrue(form.is_valid())

    def test_fields_user_has_access_to(self):
        form = UserProfileForm()
        self.assertEqual(
            form.Meta.fields,
            ['username', 'name', 'email', 'profile_image']
        )

    def test_user_can_be_blank(self):
        form = UserProfileForm({'user': ''})
        self.assertTrue(form.is_valid())

    def test_username_can_be_blank(self):
        form = UserProfileForm({'username': ''})
        self.assertTrue(form.is_valid())

    def test_email_can_be_blank(self):
        form = UserProfileForm({'email': ''})
        self.assertTrue(form.is_valid())
