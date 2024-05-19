from django.urls import path
from . import views

urlpatterns = [
    path('/', views.haccphome, name='haccphome'),
    path('/backBurner', views.backBurner, name='back_burner'),
    path('/beachKitchen', views.beachKitchen, name='beach_kitchen'),
    path('/santolinaKitchen', views.santolinaKitchen, name='santolina_kitchen'),
    path('/santolinaRestaurant', views.santolinaRestaurant, name='santolina_restaurant'),
    path('/basementKitchen', views.basementKitchen, name='basement_kitchen'),
    path('/backeryKitchen', views.backeryKitchen, name='backery_kitchen'),
    path('/pastryKitchen', views.pastryKitchen, name='pastry_kitchen'),

]
