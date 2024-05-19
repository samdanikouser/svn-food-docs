from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
# Create your views here.
def haccphome(request):
    return render(request, 'haccphome.html')


def backBurner(request):
    return render(request, 'backBurner.html')


def beachKitchen(request):
    return render(request, 'beachKitchen.html')


def santolinaKitchen(request):
    return render(request, 'santolinaKitchen.html')


def santolinaRestaurant(request):
    return render(request, 'santolinaRestaurant.html')


def basementKitchen(request):
    return render(request, 'basementKitchen.html')


def backeryKitchen(request):
    return render(request, 'backeryKitchen.html')


def pastryKitchen(request):
    return render(request, 'pastryKitchen.html')
