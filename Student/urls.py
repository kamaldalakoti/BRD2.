from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from Student import Lectureviews, views

app_name = "Student"

urlpatterns = [
    # path('Student_Admission', views.Student_Admission , name='Student_Admission'  ),
    # path('Home', views.Student_Admission , name="Home" ),
    # path('Recheck', views.Student_Admission_recheck , name='Recheck' ),
    path('Payment', views.Payment , name='Payment' ),
    path('Revenue',views.revenue,name='Revenue'),
    path('totalrevenue',views.totalrevenue,name='totalrevenue'),
    path('invoice', views.invoice , name='invoice' ),
    path('admintm', views.admintm , name='Admin-Dashboard'  ),
    path('Admin-Dashboard', views.admintm , name='Admin-Dashboard'  ),
    path('data-tables', views.data_tables, name= 'data-tables'),
    path('edit-course/<int:id>/', views.Edit_course , name='edit-course' ),
#
    path('edit-course2/<int:id>/', views.Edit_course2 , name='edit-course2' ),#form pass
    path('delete_course/<int:id>/', views.Delete_course , name='delete_course' ),
    path('courses_table', views.courses_table, name= 'courses_table'),
    # path('course_edit_test/<ID>', views.course_edit_test , name='course_edit_test' ) ,
    path('user_details', views.user_details, name= 'user_details'),
    
    # admin student page 
    path('admin-student' , views.Student , name="admin-student"),
    path('admin-manage_student' , views.manage_student , name="admin-manage_student"),
    path('admin_student_edit/<int:id>/' , views.admin_student_edit , name="admin_student_edit"),
    path('manage_student_del/<int:id>/' , views.student_del , name="manage_student_del"),
    path('admin_new_student' , views.admin_new_student , name="admin_new_student"),
    path('admin_paid_student' , views.admin_paid_student , name="admin_paid_student"),
    path('add-student' , views.Add_student , name="add-student"),
    path('HOME' , views.HOME , name="HOME"),
    path('' , views.HOME , name="HOME"),
    # Lecture
    path('Lecture',Lectureviews.Lectures ,name='Lecture'),
    path('Lecture-home',Lectureviews.Lecture_home ,name='Lecture-home'),
    path('Manage-Lecture',Lectureviews.Lecture_manage ,name='Manage-Lecture'),
    path('Lecture_edit/<int:id>/',Lectureviews.Lecture_edit ,name='Lecture_edit')


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)