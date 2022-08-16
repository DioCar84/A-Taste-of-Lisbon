from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Reservation, Photo, Menu
from .forms import MenuForm, ReservationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime


def home(request):
    """
    A view to render the home page.
    """
    hero_image = Photo.objects.get(title='Lisbon Tram')
    context = {'hero_image': hero_image, }
    return render(request, 'restaurant/home.html', context)


def menu(request):

    """
    A view to render the menu page.
    Displays 6 menu items per page and the creates arrows to switch pages.
    """
    menu = Menu.objects.all().order_by('dish_type', 'created_on')
    paginator = Paginator(menu, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'menu': menu, 'page_obj': page_obj, }

    return render(request, 'restaurant/menu.html', context)


def create_menu_item(request):
    """
    A view that renders a form for creating menu items.
    """
    form = MenuForm()

    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item Created.')
            return redirect('menu')

    context = {'form': form}
    return render(request, 'restaurant/menu_form.html', context)


def edit_menu_item(request, pk):
    """
    A view that renders a form for editing menu items.
    Prepopulates the form with the existing data.
    """
    menu_item = Menu.objects.get(id=pk)
    form = MenuForm(instance=menu_item)

    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES, instance=menu_item)
        if form.is_valid():
            form.save()
            messages.success(request, f'{menu_item.title} Updated.')
            return redirect('menu')

    context = {'form': form}
    return render(request, 'restaurant/menu_form.html', context)


def delete_menu_item(request, pk):
    """
    A view for deleting menu items.
    """
    menu_item = Menu.objects.get(id=pk)

    if request.method == 'POST':
        menu_item.delete()
        messages.success(request, f'{menu_item.title} Deleted.')
        return redirect('menu')

    context = {'plate': menu_item}
    return render(request, 'restaurant/delete_item.html', context)


def reservations(request):
    """
    A view for rendering the reservations page.
    Allows users to book reservations for a specific day, time slot and table.
    """
    open_image = Photo.objects.get(title='Open Times')
    open_banner = Photo.objects.get(title='Open Times Banner')
    form = ReservationForm()

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        table = form['table'].value()
        date = form['date'].value()
        date_value = datetime.strptime(date, '%m/%d/%Y')
        time = form['time'].value()
        reservation = Reservation.objects. \
            filter(table=table, date=date_value, time=time)

        if reservation:
            messages.warning(
                request,
                'Reservation Already Exists Please '
                'Choose a Different Day, Time or Table.'
                )
            return redirect('reservations')
        else:
            if form.is_valid():
                form.save()
                messages.success(request, 'Reservation Created.')
                return redirect('reservations')

    context = {
        'open_image': open_image, 'open_banner': open_banner,
        'form': form
    }
    return render(request, 'restaurant/reservations.html', context)


@login_required
def user_reservations(request):
    """
    A view for rendering user reservations.
    Can only be accessed by users that are logged in.
    Allows staff members to view all reservations, however
    restricts non staff users to only being able to view their own.
    """
    reservations = Reservation.objects.all()

    if request.user.is_staff:
        user_reservations = reservations.order_by('date')
        if not user_reservations:
            messages.warning(request, 'No Reservations Booked At This Time.')
            return render(request, 'users/profile_page.html')
    else:
        user_reservations = reservations.filter(
            email=request.user.email
            ).order_by('date')
        if not user_reservations:
            messages.warning(request, 'No Reservations Found For This Email.')
            return render(request, 'users/profile_page.html')
    context = {'reservations': user_reservations}
    messages.success(request, 'Reservations Found.')
    return render(request, 'restaurant/user_reservations.html', context)


@login_required
def edit_user_reservation(request, pk):
    """
    A view for editing user reservations.
    Can only be accessed by users that are logged in.
    Prepopulates the form with the existing data.
    """
    reservation = Reservation.objects.get(id=pk)
    form = ReservationForm(instance=reservation)

    if request.method == 'POST':
        form = ReservationForm(
            request.POST, request.FILES,
            instance=reservation
            )
        if form.is_valid():
            form.save()
            messages.success(request, 'Reservation Updated.')
            return redirect('user_reservations')

    context = {'form': form}
    return render(request, 'restaurant/edit_reservation.html', context)


@login_required
def delete_user_reservation(request, pk):
    """
    A view for deleting user reservations.
    Can only be accessed by users that are logged in.
    """
    reservation = Reservation.objects.get(id=pk)

    if request.method == 'POST':
        reservation.delete()
        messages.success(request, 'Reservation Deleted.')
        return redirect('user_reservations')

    context = {'reservation': reservation}
    return render(request, 'restaurant/delete_reservation.html', context)


def about(request):
    """
    A view for rendering the about page.
    """
    map_image = Photo.objects.get(title='Map of London')
    context = {'map': map_image, }
    return render(request, 'restaurant/about.html', context)
