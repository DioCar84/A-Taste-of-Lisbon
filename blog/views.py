from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Count
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.
def blog(request):
    Post.objects.annotate(Count('comments'))
    posts = Post.objects.all()
    comments = Post.objects.annotate(post_comments=Count('comments')).order_by('-post_comments')[:3]
    dish_type = PostForm

    if request.method == 'POST':
        recipe = request.POST.get('recipe_name')
        if recipe != '' and recipe is not None:
            blog_recipes = posts.filter(title__icontains=recipe).order_by('created_on')
            if not blog_recipes:
                messages.warning(request, 'No Recipes Found For Your Search')
                return redirect('blog')
            context = {'recipes': blog_recipes, 'comments': comments, 'dishes': dish_type,}
            messages.success(request, 'Recipe(s) Found.')
            return render(request, 'blog/blog_recipes_search.html', context)

    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'posts': posts, 'comments': comments, 'page_obj': page_obj, 'dishes': dish_type, }
    return render(request, 'blog/blog_home.html', context)


def blog_post(request, pk):
    Post.objects.annotate(Count('comments'))
    posts = Post.objects.annotate(post_comments=Count('comments')).order_by('-post_comments')[:3]
    post = Post.objects.get(id=pk)
    comments = post.comments.all().order_by('created_on')
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

def edit_blog_post(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, f'{post.title} Updated.')
            return redirect('blog')

    context = { 'post': post, 'form': form }
    return render(request, 'blog/edit_post.html', context)


def delete_blog_post(request, pk):
    post = Post.objects.get(id=pk)

    if request.method == 'POST':
        post.delete()
        messages.success(request, f'Post Deleted.')
        return redirect('blog')

    context = {'post': post}
    return render(request, 'blog/delete_post.html', context)

def edit_blog_comment(request, pk):
    comment = Comment.objects.get(id=pk)
    form = CommentForm(instance=comment)

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comment Updated.')
            return redirect('blog')

    context = {'post': comment, 'form': form }
    return render(request, 'blog/edit_comment.html', context)


def delete_blog_comment(request, pk):
    comment = Comment.objects.get(id=pk)

    if request.method == 'POST':
        comment.delete()
        messages.success(request, f'Comment Deleted.')
        return redirect('blog')

    context = {'post': comment}
    return render(request, 'blog/delete_comment.html', context)


def blog_meal_tag(request, tag):
    Post.objects.annotate(Count('comments'))
    all_posts = Post.objects.all()
    posts = Post.objects.filter(meal_type=tag)
    comments = Post.objects.annotate(post_comments=Count('comments')).order_by('-post_comments')[:3]
    dish_type = PostForm

    if request.method == 'POST':
        recipe = request.POST.get('recipe_name')
        if recipe != '' and recipe is not None:
            blog_recipes = all_posts.filter(title__icontains=recipe).order_by('created_on')
            if not blog_recipes:
                messages.warning(request, 'No Recipes Found For Your Search')
                return redirect('blog')
            context = {'recipes': blog_recipes, 'comments': comments, 'dishes': dish_type,}
            messages.success(request, 'Recipe(s) Found.')
            return render(request, 'blog/blog_recipes_search.html', context)

    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'posts': posts, 'comments': comments, 'page_obj': page_obj, 'dishes': dish_type, }
    return render(request, 'blog/blog_home.html', context)

def blog_dish_tag(request, tag):
    Post.objects.annotate(Count('comments'))
    all_posts = Post.objects.all()
    posts = Post.objects.filter(dish_type=tag)
    comments = Post.objects.annotate(post_comments=Count('comments')).order_by('-post_comments')[:3]
    dish_type = PostForm

    if request.method == 'POST':
        recipe = request.POST.get('recipe_name')
        if recipe != '' and recipe is not None:
            blog_recipes = all_posts.filter(title__icontains=recipe).order_by('created_on')
            if not blog_recipes:
                messages.warning(request, 'No Recipes Found For Your Search')
                return redirect('blog')
            context = {'recipes': blog_recipes, 'comments': comments, 'dishes': dish_type,}
            messages.success(request, 'Recipe(s) Found.')
            return render(request, 'blog/blog_recipes_search.html', context)

    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'posts': posts, 'comments': comments, 'page_obj': page_obj, 'dishes': dish_type, }
    return render(request, 'blog/blog_home.html', context)
