from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                login(request, user)
                return redirect('home')
            else:
                error_message = 'Invalid password'
        except User.DoesNotExist:
            error_message = 'User does not exist'
    else:
        error_message = None
    return render(request, 'login.html', {'error_message': error_message})

def user_logout(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration.html', {'form': form})


@login_required
def home(request):
    return render(request, 'home.html')
