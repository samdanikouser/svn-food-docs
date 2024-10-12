from django.urls import path

from . import views

urlpatterns = [
    path('/addMore', views.add_more, name='add_more'),
]