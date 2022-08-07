from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:pk>/', views.blog_post, name='blog_post'),
    path('meal_tag/<str:tag>/', views.blog_meal_tag, name='blog_meal_tag'),
    path('dish_tag/<str:tag>/', views.blog_dish_tag, name='blog_dish_tag'),
    path('edit_post/<int:pk>/', views.edit_blog_post, name='edit_blog_post'),
    path('delete_post/<int:pk>/', views.delete_blog_post, name='delete_blog_post'),
]