from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from student_dashboard import views


app_name = "student_dashboard"

urlpatterns = [
    path('student_dashboard', views.Student_Admission_recheck , name='student_dashboard' ),
    path('Recheck', views.Recheck , name='Recheck' ),
    
    path('Payment', views.Payment , name='Payment' ),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)