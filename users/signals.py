from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile

@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):

    print('Sender:', sender)
    print('Instance:', instance)
    print('Created:', created)


    if created:
        user = instance
        UserProfile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
        )
