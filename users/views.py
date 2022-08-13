from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, login, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
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

def login_user(request):
    page = 'login'
    form = AuthenticationForm(request)

    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"You are now logged in as {username}.")
                return redirect('profile')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    
    context = {'page': page, 'form': form, }
    return render(request, 'users/login_register.html', context)

@login_required
def logout_user(request):
    logout(request)
    messages.success(request, 'User was logged out!')
    return redirect('login')


@login_required
def user_profile(request):

    user = User.objects.filter(username=request.user.username).first()
    profile = user.userprofile
    approvals = Comment.objects.filter(approved=False).count()

    reservations = Reservation.objects.filter(email= request.user.email).count()
    comments = 0
    likes = 0
    posts = Post.objects.all()
    for post in posts:
        comments += post.comments.filter(author=request.user).count()
        likes += post.likes.filter(username=request.user.username).count()

    

    context = {'profile': profile, 'reservations': reservations, 'comments': comments, 'likes':likes, 'approvals': approvals, }
    return render(request, 'users/profile_page.html', context)

@login_required
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

@login_required
def delete_profile(request):

    user = UserProfile.objects.filter(username=request.user.username).first()

    if request.method == 'POST':
        user.delete()
        logout(request)
        messages.success(request, 'Profile Deleted.')
        return redirect('home')

    context = {'user': user}
    return render(request, 'users/delete_profile.html')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form': form, }
    return render(request, 'users/change_password.html', context)


def approve_comments(request):
    comments = Comment.objects.filter(approved=False)

    if request.method == 'POST':
        post_comment = request.POST.get('id')
        
        comment = Comment.objects.get(id=post_comment)
        comment.approved = True
        comment.save()
        messages.success(request, 'Comment has been approved')
        return redirect('approve_comments')

    context = {'comments': comments}
    return render(request, 'users/approve_comments.html', context)

def delete_comment(request, pk):
    comment = Comment.objects.get(id=pk)
    
    if request.method == 'POST':
        comment.delete()
        messages.success(request, 'Comment Deleted.')
        return redirect('approve_comments')

    context = {'comment': comment}
    return render(request, 'users/delete_comment.html', context)
