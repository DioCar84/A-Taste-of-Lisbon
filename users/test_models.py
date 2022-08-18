import datetime as date
from django.test import TestCase
from .models import UserProfile


class TestUsersModels(TestCase):
    '''
    A class to test models in the Users app.
    '''
    def test_user_profile_created_now(self):
        item = UserProfile.objects.create()
        current_date = date.datetime.now()
        self.assertEqual(current_date.date(), item.created_on.date())

    def test_default_profile_image_name(self):
        item = UserProfile.objects.create()
        self.assertEqual(item.profile_image, 'muoktj5dbjhygxwuu0v3.png')
