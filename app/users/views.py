from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from . import forms


def home(request):
    return render(request, 'users/home.html')


def about(request):
    return render(request, 'users/about.html')


def register(request):
    if request.method == 'POST':
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You are now able to log in'
            )
            return redirect('login')
    else:
        form = forms.UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    # If user submits the form
    if request.method == 'POST':
        user_update_form = forms.UserUpdateForm(
            request.POST, instance=request.user)
        if user_update_form.is_valid():
            user_update_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        # Else show the user's current info
        user_update_form = forms.UserUpdateForm(instance=request.user)

    context = {
        'user_update_form': user_update_form
    }
    return render(request, 'users/profile.html', context)
