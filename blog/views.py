from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator
from django.db.models import Count
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import PostForm, CommentForm


def blog(request):
    """
    A view to render the blog page and all the posts.
    This view limits the posts to 4 per page and then creates page arrows.
    Also, has a search function that allows
    users to search for recipes by name.
    """
    Post.objects.annotate(Count('comments'))
    posts = Post.objects.all()
    comments = Post.objects.annotate(post_comments=Count('comments')) \
        .order_by('-post_comments')[:3]
    dish_type = PostForm

    if request.method == 'POST':
        recipe = request.POST.get('recipe_name')
        if recipe != '' and recipe is not None:
            blog_recipes = posts.filter(title__icontains=recipe) \
                .order_by('created_on')
            if not blog_recipes:
                messages.warning(request, 'No Recipes Found For Your Search')
                return redirect('blog')
            context = {
                'recipes': blog_recipes,
                'comments': comments, 'dishes': dish_type,
                }
            messages.success(request, 'Recipe(s) Found.')
            return render(request, 'blog/blog_recipes_search.html', context)

    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts': posts, 'comments': comments,
        'page_obj': page_obj, 'dishes': dish_type,
        }
    return render(request, 'blog/blog_home.html', context)


def blog_post(request, pk):
    """
    A view to render an individual blog post.
    This view allows users to like or unlike a post.
    There is also functionality for logged in Users to leave comments.
    Also, has a search function that allows
    users to search for recipes by name.
    """
    Post.objects.annotate(Count('comments'))
    all_posts = Post.objects.all()
    posts = Post.objects.annotate(post_comments=Count('comments')) \
        .order_by('-post_comments')[:3]
    post = Post.objects.get(id=pk)
    comments = post.comments.all().order_by('created_on')
    dish_type = PostForm

    liked = False
    if post.likes.filter(id=request.user.id).exists():
        liked = True

    if request.method == 'POST':
        if 'recipe_name' in request.POST:
            recipe = request.POST.get('recipe_name')
            if recipe != '' and recipe is not None:
                blog_recipes = all_posts. \
                    filter(title__icontains=recipe).order_by('created_on')
                if not blog_recipes:
                    messages.warning(
                        request, 'No Recipes Found For Your Search'
                        )
                    return redirect(f'/blog/{post.id}')
                context = {
                    'recipes': blog_recipes, 'posts': posts,
                    'dishes': dish_type,
                    }
                messages.success(request, 'Recipe(s) Found.')
                return render(
                    request, 'blog/blog_recipes_search.html',
                    context
                    )
        else:
            form = CommentForm(request.POST, request.FILES)
            if form.is_valid():
                form.instance.post = post
                form.instance.email = request.user.email
                form.instance.author = request.user
                form.save()
                messages.success(
                    request, 'Comment Created and Pending Approval.'
                    )
                next = request.POST.get('next', '/')
                return HttpResponseRedirect(next)

    context = {
        'posts': posts, 'post': post, 'dishes': dish_type,
        'comments': CommentForm(), 'post_comments': comments,
        'liked': liked,
        }
    return render(request, 'blog/blog_post.html', context)


def create_blog_post(request):
    """
    A view to render a form for creating new blog posts.
    """
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post Created.')
            return redirect('blog')

    context = {'form': form}
    return render(request, 'blog/create_post.html', context)


def edit_blog_post(request, pk):
    """
    A view to render a form for editing blog posts.
    It will retrieve the post data and prepopulate the form fields.
    """
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, f'{post.title} Updated.')
            return redirect(f'/blog/{post.id}')

    context = {'post': post, 'form': form}
    return render(request, 'blog/edit_post.html', context)


def delete_blog_post(request, pk):
    """
    A view to delete a blog post.
    """
    post = Post.objects.get(id=pk)

    if request.method == 'POST':
        post.delete()
        messages.success(request, f'Post Deleted.')
        return redirect('blog')

    context = {'post': post}
    return render(request, 'blog/delete_post.html', context)


def edit_blog_comment(request, pk):
    """
    A view to edit a comment on a blog post.
    It will retrieve the post data and prepopulate the form fields.
    """
    comment = Comment.objects.get(id=pk)
    post = comment.post.id
    form = CommentForm(instance=comment)

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comment Updated.')
            return redirect(f'/blog/{post}')

    context = {'post': comment, 'form': form, }
    return render(request, 'blog/edit_comment.html', context)


def delete_blog_comment(request, pk):
    """
    A view to delete a comment on a blog post.
    """
    comment = Comment.objects.get(id=pk)
    post = comment.post.id

    if request.method == 'POST':
        comment.delete()
        messages.success(request, f'Comment Deleted.')
        return redirect(f'/blog/{post}')

    context = {'post': comment}
    return render(request, 'blog/delete_comment.html', context)


def blog_meal_tag(request, tag):
    """
    A view to associate blog posts with a meal type tag.
    Allows the user to filter posts by those that contain the selected tag.
    """
    Post.objects.annotate(Count('comments'))
    all_posts = Post.objects.all()
    posts = Post.objects.filter(meal_type=tag)
    comments = Post.objects.annotate(post_comments=Count('comments')) \
        .order_by('-post_comments')[:3]
    dish_type = PostForm

    if request.method == 'POST':
        recipe = request.POST.get('recipe_name')
        if recipe != '' and recipe is not None:
            blog_recipes = all_posts.filter(title__icontains=recipe) \
                .order_by('created_on')
            if not blog_recipes:
                messages.warning(request, 'No Recipes Found For Your Search')
                return redirect('blog')
            context = {
                'recipes': blog_recipes, 'comments': comments,
                'dishes': dish_type,
                }
            messages.success(request, 'Recipe(s) Found.')
            return render(request, 'blog/blog_recipes_search.html', context)

    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts': posts, 'comments': comments,
        'page_obj': page_obj, 'dishes': dish_type,
        }
    return render(request, 'blog/blog_home.html', context)


def blog_dish_tag(request, tag):
    """
    A view to associate blog posts with a dish type tag.
    Allows the user to filter posts by those that contain the selected tag.
    """
    Post.objects.annotate(Count('comments'))
    all_posts = Post.objects.all()
    posts = Post.objects.filter(dish_type=tag)
    comments = Post.objects.annotate(post_comments=Count('comments')) \
        .order_by('-post_comments')[:3]
    dish_type = PostForm

    if request.method == 'POST':
        recipe = request.POST.get('recipe_name')
        if recipe != '' and recipe is not None:
            blog_recipes = all_posts.filter(title__icontains=recipe) \
                .order_by('created_on')
            if not blog_recipes:
                messages.warning(request, 'No Recipes Found For Your Search')
                return redirect('blog')
            context = {
                'recipes': blog_recipes, 'comments': comments,
                'dishes': dish_type,
                }
            messages.success(request, 'Recipe(s) Found.')
            return render(request, 'blog/blog_recipes_search.html', context)

    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts': posts, 'comments': comments,
        'page_obj': page_obj, 'dishes': dish_type,
        }
    return render(request, 'blog/blog_home.html', context)


def like_view(request, pk):
    """
    A view that allows users to like or unlike a blog post.
    """
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('blog_post', args=[str(pk)]))
