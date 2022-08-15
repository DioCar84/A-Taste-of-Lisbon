from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class UserProfile(models.Model):
    """
    The UserProfile model class. Defines all the fields in the class.
    Creates a table in the database which stores each objects data.
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    profile_image = CloudinaryField('image', default='muoktj5dbjhygxwuu0v3.png')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        """
        The UserProfile model Meta class. 
        Defines that each instance is ordered by creation date.
        """
        ordering = ['created_on']
