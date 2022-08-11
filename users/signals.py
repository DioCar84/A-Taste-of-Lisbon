from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile

@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):

    if created:
        user = instance
        UserProfile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
        )

@receiver(post_save, sender=UserProfile)
def edit_profile(sender, instance, created, **kwargs):
    user_profile = instance
    user = user_profile.user

    if created == False:
        user.first_name = user_profile.name
        user.username = user_profile.username
        user.email = user_profile.email
        user.save()
