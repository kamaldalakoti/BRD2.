from django.contrib import admin
from .models import Student_detail ,Course,slider,courses_det,query_form
from .lecturemodels import Lecture , FileUpload 

# Register your models here.

admin.site.register(Student_detail),
admin.site.register(Course),
admin.site.register(slider),
admin.site.register(courses_det),
admin.site.register(query_form),
admin.site.register(FileUpload),
admin.site.register(Lecture),
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('id' , 'Name' , 'EMAIL')

# class Student_detail()