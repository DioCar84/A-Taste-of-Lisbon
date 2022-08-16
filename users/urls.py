from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.create_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.user_profile, name='profile'),
    path('profile/password/', views.change_password, name='change_password'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/delete/', views.delete_profile, name='delete_profile'),
    path(
        'profile/approve_comments/',
        views.approve_comments,
        name='approve_comments'
    ),
    path(
        'profile/delete_comment/<int:pk>',
        views.delete_comment,
        name='delete_comment'
    ),
    path('profile/view_users', views.view_users, name='user_accounts'),
]
