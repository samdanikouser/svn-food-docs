from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from location.models import Location
from correctiveaction.models import CorrectiveAction
from roles.models import Roles
from haccp.models import HaccpAdminData,AssignUsers,CorrectiveAction


@login_required
# Create your views here.
def haccphome(request, name):
    locations = Location.objects.all()
    return render(request, 'haccphome.html', {"name": name, "locations": locations})


def storagelocation(request, name, status):
    locations = Location.objects.all()
    actions = CorrectiveAction.objects.all()
    roles = Roles.objects.all()
    return render(request, 'storageName/storageData.html',
                  {"actions": actions, "roles": roles, "name": name, "status": status, "locations": locations})


def storagelocationAdminData(request, name, status):
    if request.method == "POST":
        storage_location = name
        sub_storage_location = status
        task_name = request.POST.get("taskName")
        used_for = request.POST.get("used_for")
        no_of_used_for = int(request.POST.get("no_of_used_for"))
        assign_task_to = request.POST.get("assign_task_to")
        repeat_every = request.POST.get("period")
        repeat_frequency = request.POST.get("repeat_frequency")
        time_on = request.POST.getlist("time_on")
        min_temp = request.POST.get("max_value")
        max_temp = request.POST.get("max_value")
        corrective_actions = request.POST.getlist("corrective_action")
        assign_verifier = request.POST.get("select_verifier")
        for num_of_sub_storage in range(1,no_of_used_for+1):
            admin_data = HaccpAdminData()
            admin_data.storage_location = storage_location
            admin_data.sub_storage_location =sub_storage_location
            admin_data.name =task_name
            admin_data.used_for =used_for+str(num_of_sub_storage)
            admin_data.assign_task_to =assign_task_to
            admin_data.repeat_every =repeat_every
            admin_data.repeat_frequency =repeat_frequency
            admin_data.time_on =time_on
            admin_data.min_temp =min_temp
            admin_data.max_temp =max_temp
            admin_data.assign_verifier =AssignUsers.objects.get(name=assign_verifier)
            admin_data.save()
            admin_data.corrective_action.set(corrective_actions)
    locations = Location.objects.all()
    return render(request, 'storageName/storageData.html', {"locations": locations, "status": status, "name": name})
