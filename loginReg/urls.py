from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('createRole/', views.createGroup, name='createGroup'),
    path('password_change/', views.PasswordChangeView, name='password_change'),
    path('', views.home, name='home'),
    path('/list', views.user_list, name='user_list'),
    path('register/', views.register, name='register'),
    path('/delete/<int:id>', views.delete_user, name='delete_user'),
    # path('/update/<int:id>', views.update_user, name='update_user'),

]
