from django.contrib import admin
from .models import Reservation, Photo, Menu

# Register your models here.
admin.site.register(Reservation)
admin.site.register(Photo)
admin.site.register(Menu)
