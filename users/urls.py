from django.urls import path
from django.contrib.auth import views as login_views
from . import views

urlpatterns = [
    # path('', views.blog, name='blog'),  
    path('register/', views.create_user, name='register'),
    path('login/', login_views.LoginView.as_view(template_name='users/login_register.html'), name='login'),
    path('logout/', login_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', views.user_profile, name='profile'),
]
