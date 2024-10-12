from django.shortcuts import render, redirect, HttpResponse
from .models import CorrectiveAction
from .forms import ActionForm


# Create your views here.

def action_list(request):
    action = CorrectiveAction.objects.all()
    return render(request, "action/list.html", {'action': action})


# add employee function
def add_action(request):
    if request.method == "POST":
        form = ActionForm(request.POST)
        if form.is_valid():
            action = form.save(commit=False)
            action.save()
            return redirect("/action/list")
        else:
            return render(request, "action/add.html",
                          {"form": form})
    return render(request, "action/add.html", {"form": ActionForm()})


# employee delete function
def delete_action(request, id):
    # listings/views.py
    action = CorrectiveAction.objects.get(pk=id)
    if request.method == "POST":
        action.delete()
        return redirect("/action/list")
    return render(request,
                  'action/delete.html',
                  {'action': action})


# update employee
def update_action(request, id):
    action = CorrectiveAction.objects.get(pk=id)
    if request.method == "POST":
        form = ActionForm(request.POST, instance=action)
        if form.is_valid():
            form.save()
            return redirect("/action/list")
        else:
            return render(request, "action/update.html",
                          {"action": action, "form": form})
    return render(request, "action/update.html", {"action": action, "form": ActionForm(instance=action)})