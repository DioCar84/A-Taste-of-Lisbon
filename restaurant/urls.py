from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('create_menu/', views.create_menu_item, name='createMenu'),
    path('edit_menu/<int:pk>/', views.edit_menu_item, name='editMenu'),
    path('delete_menu/<int:pk>/', views.delete_menu_item, name='deleteMenu'),
    path('reservations/', views.reservations, name='reservations'),
    path('reservations/user/', views.user_reservations, name='user_reservations'),
    path('reservations/user/<int:pk>', views.edit_user_reservation, name='editReservations'),
    path('reservations/user/<int:pk>/delete', views.delete_user_reservation, name='deleteReservation'),
    path('about/', views.about, name='about'),
]
