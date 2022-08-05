from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Post, Comment
from .forms import PostForm

# Create your views here.
def blog(request):
    posts = Post.objects.all()
    dish_type = PostForm

    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'posts': posts, 'page_obj': page_obj, 'dishes': dish_type, }
    return render(request, 'blog/blog_home.html', context)
