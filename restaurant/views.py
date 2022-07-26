from django.shortcuts import render
from .models import Reservation, Photo

# Create your views here.
def home(request):
    hero_image = Photo.objects.get(title='Lisbon Tram');
    context = {'hero_image': hero_image, }
    return render(request, 'restaurant/home.html', context)

def menu(request):
    return render(request, 'restaurant/menu.html')

def reservations(request):
    return render(request, 'restaurant/reservations.html')

def about(request):
    return render(request, 'restaurant/about.html')
