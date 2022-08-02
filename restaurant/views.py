from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Reservation, Photo, Menu
from .forms import MenuForm
from django.contrib import messages
from cloudinary.forms import cl_init_js_callbacks

# Create your views here.
def home(request):
    hero_image = Photo.objects.get(title='Lisbon Tram')
    context = {'hero_image': hero_image, }
    return render(request, 'restaurant/home.html', context)

def menu(request):
    menu = Menu.objects.all().order_by('dish_type', 'created_on')
    paginator = Paginator(menu, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'menu': menu, 'page_obj': page_obj,}

    return render(request, 'restaurant/menu.html', context)

def createMenuItem(request):
    form = MenuForm()

    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item created.')
            return redirect('menu')

    context = {'form': form}
    return render(request, 'restaurant/menu_form.html', context)


def editMenuItem(request, pk):
    menuItem = Menu.objects.get(id=pk)
    form = MenuForm(instance=menuItem)

    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES, instance=menuItem)
        if form.is_valid():
            form.save()
            messages.success(request, f'{menuItem.title} updated.')
            return redirect('menu')

    context = { 'form': form }
    return render(request, 'restaurant/menu_form.html', context)

def deleteMenuItem(request, pk):
    menuItem = Menu.objects.get(id=pk)

    if request.method == 'POST':
        menuItem.delete()
        messages.success(request, f'{menuItem.title} deleted.')
        return redirect('menu')

    context = {'plate': menuItem}
    return render(request, 'restaurant/delete_item.html', context)

def reservations(request):
    open_image = Photo.objects.get(title='Open Times')
    context = {'open_image': open_image, }
    return render(request, 'restaurant/reservations.html', context)

def about(request):
    map_image = Photo.objects.get(title='Map of London')
    context = {'map' : map_image, }
    return render(request, 'restaurant/about.html', context)
