from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth \
    import logout, login, authenticate, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import messages
from blog.models import Post, Comment
from restaurant.models import Reservation
from .models import UserProfile
from .forms import UserProfileForm


def create_user(request):
    """
    A view for creating a new user.
    Prevents registering with a username that already exists in the database.
    """
    page = 'register'
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            if User.objects.filter(username=user.username):
                messages.error(
                    request, 'Username has already been taken, '
                    'please choose a different username.'
                )
                return redirect('register')
            else:
                user.save()

            messages.success(request, f'new user {user.username} was created.')
            return redirect('home')

    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)


def login_user(request):
    """
    A view for logging in a user.
    Prevents a logged in user from logging in again.
    Also, makes sure that the user exists
    and has enterred the correct credentials.
    """
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
                messages.success(
                    request,
                    f"You are now logged in as {username}."
                    )
                return redirect('profile')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")

    context = {'page': page, 'form': form, }
    return render(request, 'users/login_register.html', context)


def logout_user(request):
    """
    A view for logging out a user.
    Can only be accessed by users that are logged in.
    """
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'You are now logged out!')
        return redirect('login')

    else:
        messages.warning(
            request,
            'You must be logged in to perform that action!'
        )
        return redirect('login')


def user_profile(request):
    """
    A view for rendering a user profile.
    Can only be accessed by users that are logged in.
    Alters data displayed based on user if the user is a staff member or not.
    """
    if request.user.is_authenticated:
        user = User.objects.filter(username=request.user.username).first()
        profile = user.userprofile
        approvals = Comment.objects.filter(approved=False).count()

        if user.is_staff:
            reservations = Reservation.objects.all().count()
        else:
            reservations = Reservation.objects. \
                filter(email=request.user.email).count()
        comments = 0
        likes = 0
        posts = Post.objects.all()
        for post in posts:
            comments += post.comments.filter(author=request.user).count()
            likes += post.likes.filter(username=request.user.username).count()

        context = {
            'profile': profile, 'reservations': reservations,
            'comments': comments, 'likes': likes, 'approvals': approvals,
        }
        return render(request, 'users/profile_page.html', context)

    else:
        messages.warning(
            request,
            'You must be logged in to access this page!'
        )
        return redirect('login')


def edit_profile(request):
    """
    A view for editing a user profile.
    Can only be accessed by users that are logged in.
    Returns a prepoluated form with the
    current profile information available in the database.
    """
    if request.user.is_authenticated:
        user = UserProfile.objects.filter(
            username=request.user.username
        ).first()
        form = UserProfileForm(instance=user)

        if request.method == 'POST':
            form = UserProfileForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile Updated.')
                return redirect('profile')

        context = {'form': form, }
        return render(request, 'users/profile_form.html', context)

    else:
        messages.warning(
            request,
            'You must be logged in to access this page!'
        )
        return redirect('login')


def delete_profile(request):
    """
    A view for deleting a user profile.
    Can only be accessed by users that are logged in.
    """
    if request.user.is_authenticated:
        user = UserProfile.objects.filter(
            username=request.user.username
        ).first()

        if request.method == 'POST':
            user.delete()
            logout(request)
            messages.success(request, 'Profile Deleted.')
            return redirect('home')

        context = {'user': user}
        return render(request, 'users/delete_profile.html')

    else:
        messages.warning(
            request,
            'You must be logged in to access this page!'
        )
        return redirect('login')


def change_password(request):
    """
    A view for changing a user password.
    Can only be accessed by users that are logged in.
    """
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                messages.success(
                    request,
                    'Your password was successfully updated!'
                    )
                return redirect('profile')
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = PasswordChangeForm(request.user)
        context = {'form': form, }
        return render(request, 'users/change_password.html', context)
    else:
        messages.warning(
            request,
            'You must be logged in to perform that action!'
        )
        return redirect('login')


def approve_comments(request):
    """
    A view for staff members to approve user comments.
    Alters comments approved status from False to True.
    """
    comments = Comment.objects.filter(approved=False)

    if request.user.is_staff:

        if request.method == 'POST':
            post_comment = request.POST.get('id')

            comment = Comment.objects.get(id=post_comment)
            comment.approved = True
            comment.save()
            messages.success(request, 'Comment has been approved')
            return redirect('approve_comments')

        context = {'comments': comments}
        return render(request, 'users/approve_comments.html', context)

    else:
        messages.warning(request, 'You do not have access to this page!')
        return redirect('profile')


def delete_comment(request, pk):
    """
    A view for staff members to delete user comments in the approval queue.
    """
    if request.user.is_staff:

        comment = Comment.objects.get(id=pk)

        if request.method == 'POST':
            comment.delete()
            messages.success(request, 'Comment Deleted.')
            return redirect('approve_comments')

        context = {'comment': comment}
        return render(request, 'users/delete_comment.html', context)

    else:
        messages.warning(request, 'You do not have access to this page!')
        return redirect('profile')


def view_users(request):
    """
    A view for staff members that displays all currently registered users.
    """
    if request.user.is_staff:
        profiles = UserProfile.objects.all()

        context = {'profiles': profiles, }
        return render(request, 'users/user_accounts.html', context)

    else:
        messages.warning(request, 'You do not have access to this page!')
        return redirect('profile')
