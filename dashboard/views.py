from django.shortcuts import render


# Create your views here.
def add_more(request):
    return render(request, "add_more/addMore.html")
