from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProfile

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

    profile = UserProfile.objects.filter(user=request.user)

    context = {'profile': profile}
    return render(request, 'users/profile_page.html', context)
