from django.db import models

# Create your models here.

class Reservation(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    total_people = models.IntegerField()
    date = models.DateTimeField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.last_name + " " + self.date

    class Meta:
        ordering = ['-date']
