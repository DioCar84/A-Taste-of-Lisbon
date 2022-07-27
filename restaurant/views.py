from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Reservation, Photo, Menu

# Create your views here.
def home(request):
    hero_image = Photo.objects.get(title='Lisbon Tram')
    context = {'hero_image': hero_image, }
    return render(request, 'restaurant/home.html', context)

def menu(request):
    menu = Menu.objects.all()
    paginator = Paginator(menu, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'menu': menu, 'page_obj': page_obj,}

    return render(request, 'restaurant/menu.html', context)

def reservations(request):
    return render(request, 'restaurant/reservations.html')

def about(request):
    map_image = Photo.objects.get(title='Map of London')
    context = {'map' : map_image, }
    return render(request, 'restaurant/about.html', context)
