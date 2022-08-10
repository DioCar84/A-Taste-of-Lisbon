from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from .models import UserProfile


def createProfile(sender, instance, created, **kwargs):
    
    if created:
        user = instance
        UserProfile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.name,
        )
post_save.connect(createProfile, sender=User)