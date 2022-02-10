from pyexpat import model
from turtle import TurtleGraphicsError
from django.db import models
from django.urls import reverse
# from ckeditor.fields import RichTextField
from ckeditor.fields import RichTextField
from django.utils import timezone




class query_form(models.Model):
    form_name = models.CharField(max_length=100,null=True)
    form_email = models.CharField(max_length=100,null=True)
    form_subject = models.CharField(max_length=100,null=True)
    form_message = models.CharField(max_length=1000,null=True)
    created = models.DateTimeField(auto_now_add=True,null=True)


    def __str__(self):
        return self.form_subject


class ckeditor_test(models.Model):
    post = RichTextField(blank=True, null=True)

class courses_det(models.Model):
    course_img = models.ImageField(upload_to='static/course_img',null=True,max_length=100)
    course_details = RichTextField(blank=True , null=True)
    course_no = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.course_no

class slider(models.Model):
    slider_name = models.CharField(null=True , max_length = 50 )
    slider_img = models.ImageField(upload_to='static/slider', null=True ,max_length = 100)
    Details = RichTextField(blank=True , null=True)
    
    def __str__(self):
        return self.slider_name


# class Course(models.Model):
#     Course_name = models.CharField(max_length = 40 , null= True )
#     Price = models.IntegerField(null=True)
#     Thumb = models.ImageField(upload_to='static/img', null=True ,max_length = 100)
#     Details = RichTextField(blank=True , null=True)
#     duration = {
#         ('1 mon','1 MONTH'),
#         ('3 mon','3 MONTH'),
#         ('6 mon','6 MONTH'),
#     }
#     Duration = models.CharField(max_length=100,choices=duration,null=True)

    
#     def __str__(self):
#         return self.Course_name
    # def __str__(self):
    #     return self.id
    
    
    
    #new added
class Course(models.Model):

    id = models.AutoField(primary_key=True)
    Course_name = models.CharField(max_length = 40 , null= True )
    Price = models.IntegerField(null=True)
    Thumb = models.ImageField(upload_to='static/img', null=True ,max_length = 100)
    Details = RichTextField(blank=True , null=True)
    duration = {
        ('1 mon','1 MONTH'),
        ('3 mon','3 MONTH'),
        ('6 mon','6 MONTH'),
    }
    Duration = models.CharField(max_length=100,choices=duration,null=True)
    title = models.CharField(max_length=127)
    sub_title = models.CharField(max_length=127)
    # category = models.CharField(max_length=127, choices=COURSE_CATEGORY_TYPES, default='General Education')
    # description = models.TextField(null=True)
    start_date = models.DateField(null=True)
    finish_date = models.DateField(null=True)
    is_official = models.BooleanField(default=False)
    # status = models.PositiveSmallIntegerField(default=settings.COURSE_UNAVAILABLE_STATUS)
    # image = models.ImageField(upload_to='static/img', null=True, blank=True)
    # students = models.ManyToManyField(Student)
    # teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)

    
    def __str__(self):
        return self.title
   
    #new added   



# Create your models here.
class Student_detail(models.Model):
    Name = models.CharField(max_length = 50 ,null=True )
    Email = models.CharField(max_length = 30 ,null=True)
    Number = models.CharField(max_length = 12 ,null=True)
    # Number2 = models.CharField(max_length = 12 ,null=True)
    # Date = models.DateField(null=True)
    
    Aadhaar = models.CharField(max_length = 12 ,null=True)
    Enrollment_date = models.DateTimeField(auto_now_add=True , null=True)
    GENDER_CHOICES = (
        # ('NONE', 'Gender'),
        ('M', 'Male'),
        ('F', 'Female'),
        (')', 'Other'),
    )
    Gender = models.CharField(max_length = 4 ,null=True  ,choices=GENDER_CHOICES )
    # Father = models.CharField(max_length = 50 ,null=True)
    education = (
        ('10th','Secondary education'),
        ('12th','Senior secondary education'),
        ('Grad','Graduation education'),
        ('P.Grad','Post Graduation education'),
    )
    Education = models.CharField(max_length = 50 ,null=True,choices=education)
    Course_name = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    doc_10 = models.FileField(upload_to='static/docs',  null=True ,max_length = 100)
    doc_12 =  models.FileField(upload_to='static/docs', null=True ,max_length = 100)
    doc_ug =  models.FileField(upload_to='static/docs', null=True ,max_length = 100)
    doc_pg =  models.FileField(upload_to='static/docs', null=True ,max_length = 100)
    Address = models.TextField(max_length = 200 ,null=True)
    # State = models.CharField(max_length= 20 , null=True)
    # City = models.CharField(max_length = 15 , null=True)
    # House = models.CharField(max_length = 15 , null=True)
    # Post_office = models.CharField(max_length = 15 , null=True)
    # Block = models.CharField(max_length = 15 , null=True)
    # District = models.CharField(max_length = 15 , null=True)
    # Pincode = models.CharField(max_length = 15 , null=True)
    # Locality = models.CharField(max_length = 15 , null=True)
    Payment = models.BooleanField(default='False')
    Trm = models.BooleanField(default='False')
    

    def __str__(self):
        return self.Email

    