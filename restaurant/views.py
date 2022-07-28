from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Reservation, Photo, Menu
from .forms import MenuForm

# Create your views here.
def home(request):
    hero_image = Photo.objects.get(title='Lisbon Tram')
    context = {'hero_image': hero_image, }
    return render(request, 'restaurant/home.html', context)

def menu(request):
    menu = Menu.objects.all().order_by('created_on')
    paginator = Paginator(menu, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'menu': menu, 'page_obj': page_obj,}

    return render(request, 'restaurant/menu.html', context)

def editMenu(request, pk):
    menuItem = Menu.objects.get(id=pk)
    form = MenuForm(instance=menuItem)

    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menuItem)
        if form.is_valid():
            form.save()
            return redirect('menu')

    context = { 'form': form }
    return render(request, 'restaurant/menu_form.html', context)

def reservations(request):
    return render(request, 'restaurant/reservations.html')

def about(request):
    map_image = Photo.objects.get(title='Map of London')
    context = {'map' : map_image, }
    return render(request, 'restaurant/about.html', context)
