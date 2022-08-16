from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('create_post/', views.create_blog_post, name='create_post'),
    path('blog_search/', views.blog, name='blog_search'),
    path('<int:pk>/', views.blog_post, name='blog_post'),
    path('meal_tag/<str:tag>/', views.blog_meal_tag, name='blog_meal_tag'),
    path('dish_tag/<str:tag>/', views.blog_dish_tag, name='blog_dish_tag'),
    path('edit_post/<int:pk>/', views.edit_blog_post, name='edit_blog_post'),
    path(
        'delete_post/<int:pk>/',
        views.delete_blog_post,
        name='delete_blog_post'
    ),
    path(
        'edit_comment/<int:pk>/',
        views.edit_blog_comment,
        name='edit_blog_comment'
    ),
    path(
        'delete_comment/<int:pk>/',
        views.delete_blog_comment,
        name='delete_blog_comment'
    ),
    path('like/<int:pk>/', views.like_view, name='like_post'),
]
