from cProfile import label
from dataclasses import fields
from pyexpat import model
from xml.dom.minidom import Attr
from django.core import validators
from django import forms
from .models import Student_detail , Course , ckeditor_test
# from django import ModelForm
from django.forms import ModelForm
from ckeditor.fields import RichTextField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class newuserform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2','is_staff']
        widgets = {
            'username':forms.TextInput(attrs={'type':'email'})
        }

# class ckeditor_test_Form(forms.ModelForm):
#     class Meta:
#         model = ckeditor_test
#         fields = ['post']
        

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        widgets = {
            'Course_name': forms.TextInput(attrs={'class': 'w-100 p-2 mb-4 col-6'}),
            'Price': forms.TextInput(attrs={'class': 'w-100 p-2 mb-4 col-6'}),
            'start_date': forms.DateInput(attrs={
                
                'type':'date',
                
            }),
            'finish_date': forms.DateInput(attrs={
                'type':'date',
            }
            ),
            # 'Details': forms.RichTextField(attrs={'class': 'p-2 mb-4 col-6'}),
            

        }

class Student_detailForm(forms.ModelForm):
    class Meta:
        cls_sty = 'gridsys p-2 mb-4 col-4'
        model = Student_detail
        # fields = ['Name','Email', 'Number' ,'Number2'   , 'Aadhaar' , 'Aadhaar' , 'Gender', 'Father' , 'Education', 'Course_name' , 'doc_10','doc_12','doc_ug','doc_pg',  'State' , 'City' , 'House' ,'Post_office' ,'Block','District' ,'Pincode' , 'Locality'   ]
        fields = '__all__'
        label = {
            'Gender':'Gender',
            'Date':'Date'
        }
        widgets = { 
             'Name' : forms.TextInput(attrs={'class': cls_sty ,'placeholder':'Name'}),
             'Email' : forms.TextInput(attrs={'class': cls_sty , 'type' : 'email' , 'placeholder':'Email'}),
             'Number' : forms.TextInput(attrs={'class': cls_sty ,'type':'phone', 'placeholder':'Number'}),
            #  'Number2' : forms.TextInput(attrs={'class': cls_sty ,'type':'phone' ,'placeholder':'Alternate No.'}),
            #  'Gender' : forms.ChoiceField(attrs={'class': cls_sty ,'type':'choice' ,'placeholder':'Gender'}),
             'Date' : forms.TextInput(attrs={
                 'type':'date'
             }),
             
             'Aadhaar' : forms.TextInput(attrs={'class': cls_sty  , 'placeholder':'Aadhaar No.'}),
           

         }
class Student_detail_editForm(forms.ModelForm):
    class Meta:
        cls_sty = 'gridsys p-2 mb-4 col-4'
        model = Student_detail
        # fields = ['Name','Email', 'Number' ,'Number2'   , 'Aadhaar' , 'Aadhaar' , 'Gender', 'Father' , 'Education', 'Course_name' , 'doc_10',  'State' , 'City' , 'House' ,'Post_office' ,'Block','District' ,'Pincode' , 'Locality'   ]
        fields = '__all__'

        widgets = { 
             'Name' : forms.TextInput(attrs={'class': cls_sty ,'placeholder':'Name'}),
             'Email' : forms.TextInput(attrs={'class': cls_sty , 'readonly': 'True', 'type' : 'email' , 'placeholder':'Email'}),
             'Number' : forms.TextInput(attrs={'class': cls_sty ,'type':'phone', 'placeholder':'Number'}),
            #  'Number2' : forms.TextInput(attrs={'class': cls_sty ,'type':'phone' ,'placeholder':'Alternate No.'}),
           

         }
        
    
   