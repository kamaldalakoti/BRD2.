from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from Teachers import views

app_name = "Teachers"

urlpatterns = [
    path('Dashboard', views.Dashboard , name='Teachers_Dashboard'  ) ,
    path('TEST', views.TEST , name='TEST'  ) ,
    # path('Home', views.Student_Admission , name="Home"  ),
]