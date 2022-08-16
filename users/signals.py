from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    The create_profile function triggers a signal
    everytime a new user is created.
    It will associate this user to a
    profile which is also created at that time.
    It will then populate the profile with the user,
    username and email fields,
    from the newly created user.
    """
    if created:
        user = instance
        UserProfile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
        )


@receiver(post_save, sender=UserProfile)
def edit_profile(sender, instance, created, **kwargs):
    """
    The edit_profile function triggers a signal
    everytime a user is altered.
    It will associate this user to their profile in the database.
    It will then alter and save the fields in the
    user and profile objects,
    based on the user input.
    """
    user_profile = instance
    user = user_profile.user

    if created is False:
        user.first_name = user_profile.name
        user.username = user_profile.username
        user.email = user_profile.email
        user.save()
