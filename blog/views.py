from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Count
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.
def blog(request):
    Post.objects.annotate(Count('comments'))
    posts = Post.objects.all()
    dish_type = PostForm

    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'posts': posts, 'page_obj': page_obj, 'dishes': dish_type, }
    return render(request, 'blog/blog_home.html', context)


def blog_post(request, pk):
    Post.objects.annotate(Count('comments'))
    posts = Post.objects.all()
    post = Post.objects.get(id=pk)
    comments = post.comments.all().order_by('-created_on')
    dish_type = PostForm

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.post = post
            form.instance.email = request.user.email
            form.instance.author = request.user
            form.save()
            messages.success(request, 'Comment Created.')
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)

    context = {'posts': posts, 'post': post, 'dishes': dish_type, 'comments': CommentForm(), 'post_comments': comments, }
    return render(request, 'blog/blog_post.html', context)
