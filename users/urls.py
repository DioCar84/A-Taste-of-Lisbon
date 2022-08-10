from django.urls import path
from . import views

urlpatterns = [
    # path('', views.blog, name='blog'),  
    path('register/', views.create_user, name='register'),  
]
