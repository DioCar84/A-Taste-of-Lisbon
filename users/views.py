from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from blog.models import Post, Comment
from restaurant.models import Reservation

# Create your views here.
def create_user(request):

    page = 'register'

    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            if User.objects.filter(username=user.username):
                messages.error(request, 'Username has already been taken, please choose a different username.')
                return redirect('register')
            else:
                user.save()

            messages.success(request, f'new user {user.username} was created.')
            return redirect('home')

    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)

@login_required
def user_profile(request):

    user = User.objects.filter(username=request.user.username).first()
    profile = user.userprofile

    reservations = Reservation.objects.filter(email= request.user.email).count()
    comments = 0
    likes = 0
    posts = Post.objects.all()
    for post in posts:
        comments += post.comments.filter(author=request.user).count()
        likes += post.likes.filter(username=request.user.username).count()

    

    context = {'profile': profile, 'reservations': reservations, 'comments': comments, 'likes':likes, }
    return render(request, 'users/profile_page.html', context)


def edit_profile(request):

    user = UserProfile.objects.filter(username=request.user.username).first()
    form = UserProfileForm(instance=user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Updated.')
            return redirect('profile')

    context = {'form': form, }
    return render(request, 'users/profile_form.html', context)
