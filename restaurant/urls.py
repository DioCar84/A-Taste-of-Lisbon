from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('create_menu/', views.createMenuItem, name='createMenu'),
    path('edit_menu/<int:pk>/', views.editMenuItem, name='editMenu'),
    path('delete_menu/<int:pk>/', views.deleteMenuItem, name='deleteMenu'),
    path('reservations/', views.reservations, name='reservations'),
    path('reservations/user/', views.userReservations, name='userReservations'),
    path('reservations/user/<int:pk>', views.editUserReservation, name='editReservations'),
    path('about/', views.about, name='about'),
]
