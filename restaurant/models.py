from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Reservation(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    number_of_clients = models.PositiveSmallIntegerField(choices=(
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
    ), null=True)
    date = models.DateField()
    time = models.PositiveSmallIntegerField(choices=(
        (1, '11:00-12:00'),
        (2, '12:00-13:00'),
        (3, '13:00-14:00'),
        (4, '14:00-15:00'),
    ), null=True)
    table = models.PositiveSmallIntegerField(choices=(
        (1, 'Table 1'),
        (2, 'Table 2'),
        (3, 'Table 3'),
        (4, 'Table 4'),
        (5, 'Table 5'),
        (6, 'Table 6'),
        (7, 'Table 7'),
        (8, 'Table 8'),
    ), null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name) + " " + str(self.date)

    class Meta:
        ordering = ['-date']


class Photo(models.Model):
    title = models.CharField(max_length=100)
    image = CloudinaryField('image', default='yleipz1gqfmdwpnbtx0v.jpg')

    def __str__(self):
        return self.title


class Menu(Photo):
    description = models.TextField()
    price = models.FloatField()
    dish_type = models.PositiveSmallIntegerField(choices=(
        (1, 'starter'),
        (2, 'main'),
        (3, 'dessert'),
    ), null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
