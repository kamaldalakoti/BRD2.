from django.contrib import admin
from django.urls import path

from Student import views
from accounts import views

# app_name = "accounts"

urlpatterns = [
    # path('', views.Student_Admission  ) ,
    path('accounts/', views.signup  ) ,
    path('signup/' ,views.signup, name='signup'),
    path('login/' ,views.login, name='login'),
    path('logout/' ,views.logout, name='logout')
]