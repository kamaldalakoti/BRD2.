
from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.shortcuts import render,redirect
from django.template import context
from Student.models import Student_detail, Course, courses_det ,slider,query_form
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from Admission.settings import EMAIL_HOST_USER
import string
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
import datetime
from django.urls import reverse
from Student.forms import CourseForm, Student_detailForm,Student_detail_editForm , newuserform
from django.forms.models import model_to_dict
import random
import razorpay 
from Admission.settings import RAZORPAY_API_KEY ,RAZORPAY_API_SECRET_KEY

# Create your views here.
@login_required
def Recheck(request):
    return render(request,'recheck.html')
@login_required
def Student_Admission_recheck(request):
    User = request.user.username

    # if Student_detail.objects.filter(Email = User).exists():
        # print (Student_detail.objects.filter(Email=User))
    test = Student_detail.objects.get(Email=User).id
    test2 = Student_detail.objects.get(pk=test)
    print(test,test2)
    if request.method == 'POST':
        if request.POST.get('logout_form') == 'LOGOUT':
            auth.logout(request)
            return redirect('Student:HOME')
           
            
            # return HttpResponseRedirect('Recheck' , message)
        else:    
            # recheck = Student_detail.objects.filter(Email = User)
            # data = {  'recheck' : recheck }
        # id = Student_detail.objects.only('id').get(Email=User).id
        
        # print(recheck)
        # student  = Student_detail(Name=name, Number=number, 
        # Email= email, Father= father, Education=education, doc_10=doc_10 , doc_12=doc_12 , doc_ug=doc_ug , Address=address)
        # student.save()
            return render(request, 'student/student_dashboard.html')

        # return render(request, 'recheck.html', data )

    return render(request, 'student/student_dashboard.html',{'Test':test2})

# 
def Payment(request):
    

    #
    User = request.user.username
    test = Student_detail.objects.get(Email=User).id
    test2 = Student_detail.objects.get(pk=test)
    course = test2.Course_name
    course_price = test2.Course_name.Price
    Date = datetime.datetime.now()
    User = request.user.username
    test = Student_detail.objects.get(Email=User).id
    test2 = Student_detail.objects.get(pk=test)
    # course = test2.Course_name
        
    course_price = test2.Course_name.Price

        # print(cor)
        # print(cor2)
        # test3 = test2.
    name_b = test2.Name
    number_b = test2.Number
    email_b = test2.Email
    Pincode = test2.Pincode
    City = test2.City
    Price = course_price

    # payment gateway
    client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY ,))
    # print(RAZORPAY_API_KEY)

    order_amount = course_price ,
    order_currency = "INR"
    payment_capture = 1
    # not paymentgate way
    tax = course_price*0.18
    order_amount = 100*(course_price + tax) 
    order_amount_display = course_price + tax
    # not paymentgate way
    payment_order = client.order.create(dict(amount = order_amount , currency = order_currency , payment_capture = payment_capture ))
    payment_order_id = payment_order['id']
    print(order_amount)
    order_amount = round(order_amount)
    user_info = Student_detail.objects.get(pk=test)
    DATA = {

        "amount": order_amount ,
        "currency": "INR",
        
    #    
    }
    client.order.create(data=DATA)

    # payment gateway
    # if request.method == "POST":
    #     f = open(f"static/{User}.txt", "w")
    #     # f.write("Woops! I have deleted the content!" + " " + course +" " + course_price)
    #     f.write("Name : " + " " + str(User) + "\n" +
    #         "Course : " + str(course ) + " " + " \n" + "Course Price : "+ str(course_price) + " \n" + "Payment Status : "+ " Paid" )
    #     f.close()

    # # data for payment     
    #     return HttpResponseRedirect('invoice')
        # return HttpResponseRedirect('/')
    context =   { 'user_info': user_info ,'tax':tax , 'API_KEY' : RAZORPAY_API_KEY, 'order_amount':order_amount_display, 'order_id' : payment_order_id , 'Date':Date , 'User':User ,'name_b' : name_b , 'number_b' : number_b ,'email_b':email_b ,'Pincode':Pincode , 'City':City , 'Price':Price , "course":course , }  
    return render(request, 'payment.html' , context )
    
        

        # print(f)
        # return HttpResponseRedirect(f'static/{User}.txt' )
def invoice(request):

    Date = datetime.datetime.now()
    User = request.user.username
    test = Student_detail.objects.get(Email=User).id
    test2 = Student_detail.objects.get(pk=test)
    course = test2.Course_name
        
    course_price = test2.Course_name.Price

        # print(cor)
        # print(cor2)
        # test3 = test2.
    name_b = test2.Name
    number_b = test2.Number
    email_b = test2.Email
    Pincode = test2.Pincode
    City = test2.City
    Price = course_price

    
        # return HttpResponseRedirect('/' )
    return render(request, 'invoice.html' , {'Date':Date , 'User':User ,'name_b' : name_b , 'number_b' : number_b , 'email_b' : email_b , 'Pincode':Pincode , 'City':City , 'Price':Price , "course":course })

