from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.models import Group
from django.contrib import messages
from location.models import Location



from .forms import UserRegistrationForm, UsernamePasswordResetForm
from .models import UserProfile


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

@login_required
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(username=request.POST["username"])
            Userprofile = UserProfile.objects.get(user=user)
            Userprofile.role = request.POST["selected_options"]
            Userprofile.save()
            return redirect('register')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration.html', {'form': form})


@login_required
# @user_passes_test(manager_required)
def home(request):
    locations= Location.objects.all()
    return render(request, 'dashboard/dashboard.html',{"locations":locations})


def createGroup(request):
    if request.method == 'POST':
        role = request.POST["role"]
        group = Group.objects.create(name=role)
        group.save()
        return render(request, 'dashboard/dashboard.html')


def PasswordChangeView(request):
    if request.method == 'POST':
        form = UsernamePasswordResetForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user = User.objects.get(username=username)
            new_password = form.cleaned_data['new_password1']
            user.set_password(new_password)
            user.save()
            messages.success(request, 'Your action was successful!')
            return redirect("/")
        else:
            form = UsernamePasswordResetForm()
        return render(request, 'dashboard/dashboard.html',{"form":form})


def user_list():
    return None


def delete_user():
    return None