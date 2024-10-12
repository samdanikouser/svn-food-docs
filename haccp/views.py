from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from location.models import Location
from correctiveaction.models import CorrectiveAction
from roles.models import Roles
from haccp.models import HaccpAdminData


@login_required
# Create your views here.
def haccphome(request,name):
    locations= Location.objects.all()
    return render(request, 'haccphome.html',{"name":name,"locations":locations})

def storagelocation(request,name , status):
    locations= Location.objects.all()
    actions= CorrectiveAction.objects.all()
    roles = Roles.objects.all()
    return render(request, 'storageName/storageData.html',{"actions":actions,"roles":roles,"name":name,"status":status,"locations":locations})

def storagelocationAdminData(request,name,status):
    locations = Location.objects.all()
    return render(request, 'storageName/storageData.html',{"locations":locations,"status":status,"name":name})

