from django.urls import path
from . import views

urlpatterns = [
    path('/<str:name>/', views.haccphome, name='haccp_home'),
    path('/<str:name>/<str:status>/', views.storagelocation, name='storage_location'),
    path('/admin/<str:name>/<str:status>/', views.storagelocationAdminData, name='storage_data_admin_data'),
]
