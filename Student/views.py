from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.shortcuts import render,redirect
from django.template import context
from .models import Student_detail, Course, courses_det ,slider,query_form
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
from .forms import CourseForm, Student_detailForm,Student_detail_editForm , newuserform
from django.forms.models import model_to_dict
import random
import razorpay 
from Admission.settings import RAZORPAY_API_KEY ,RAZORPAY_API_SECRET_KEY
import math
# from notifications.signals import notify




# from django.contrib.auth.forms import UserCreationForm

# Create your views here.
# def Student_Admission(request):
    
#     Users = get_user_model()
#     users = Users.objects.all()
#     list_course = Course.objects.all()
#     # print(users)
#     if request.method == 'POST':
#         name = request.POST.get("name")
#         number = request.POST.get("number")
#         # number = request.POST.get("number")
#         email = request.POST.get("email")
#         father = request.POST.get("father")
#         education = request.POST.get("education")
#         doc_10 = request.POST.get("doc_10")
#         doc_12 = request.POST.get("doc_12")
#         doc_ug = request.POST.get("doc_ug")
#         address = request.POST.get("address")
#         # new added
#         number2 = request.POST.get("number2")
#         date = request.POST.get("date")
#         gender = request.POST.get("gender")
#         aadhaar = request.POST.get("aadhaar")
#         state = request.POST.get("state")
#         city = request.POST.get("city")
#         house = request.POST.get("house")
#         town = request.POST.get("town")
#         post_office = request.POST.get("post_office")
#         block = request.POST.get("block")
#         district = request.POST.get("district")
#         pincode = request.POST.get("pincode")
#         locality = request.POST.get("locality")
#         trm = request.POST.get("trm")
#         course = request.POST.get("course")
#         course = Course.objects.get(id = course)
#         print(course)
#         if trm == 'on':
#             trm_ = True
#         else :
#             trm_ = False     
#         print(trm)
#         if Student_detail.objects.filter(Email = email).exists():
#             message = messages.warning(request , email + " " + 'is already used')
#             return HttpResponseRedirect('/' , messages)
#         else:    
#         # new added
#             student  = Student_detail(Name=name, Number=number, 
#             Email= email, Father= father,Education=education,doc_10=doc_10,
#             doc_12=doc_12,doc_ug=doc_ug, Address=address,
#             Number2 = number2, Date = date , Course_name = course,  Aadhaar = aadhaar , Gender = gender, State = state, City = city, House = house , Post_office = post_office , Block = block , District = district, Pincode = pincode, Locality= locality, 
#             Trm = trm_
#             )
#             student.save()
#             # email = EmailMessage('title', 'body', to=[email])
#             # email.send()
#             # generating random strings 
#             N = 7
#             res = ''.join(random.choices(string.ascii_uppercase +
#                     string.digits, k = N))

            

#             print("The generated random string : " + str(res))


#             message = "your id and password is : " + " " + email + " " + res
#             subject = ' Student Admission'
            
#             # user create 
#             user = User.objects.create_user(email,password=res)

#             send_mail(subject, 
#                 message, EMAIL_HOST_USER, [email], fail_silently = False)
#             send_mail(subject, 
#                 message, EMAIL_HOST_USER, [EMAIL_HOST_USER], fail_silently = False)
#             messages.success(request, 'Your Form is Submited , Your loging id password is sent to your email @' + " " + email )
#             return HttpResponseRedirect('/' , messages)

#     return render(request, 'index.html' , { 'list_course': list_course , 'users' : users})


# @login_required
# def Student_Admission_recheck(request):
#     User = request.user.username

#     if Student_detail.objects.filter(Email = User).exists():
#         print (Student_detail.objects.filter(Email=User))
#         test = Student_detail.objects.get(Email=User).id
#         test2 = Student_detail.objects.get(pk=test)
#         course = test2.Course_name
        
#         course_price = test2.Course_name.Price

#         # print(cor)
#         # print(cor2)
#         # test3 = test2.
#         name_b = test2.Name
#         number_b = test2.Number
#         email_b = test2.Email
#         # father_b = test2.Father
#         # education_b = test2.Education
#         # address_b = test2.Address
        
#         data = { 'name_b' : name_b , 'number_b' : number_b , 'email_b' : email_b , 'course' :course, 'course_price' : course_price   }
#         # message =  messages.success(request, 'filter' )

#         if request.method == 'POST':
#             name_re = request.POST.get("name_re")
#             number_re = request.POST.get("number_re")
#             # number = request.POST.get("number")
#             email_re = request.POST.get("email_re")
#             father_re = request.POST.get("father_re")
#             education_re = request.POST.get("education_re")
#             doc_10_re = request.POST.get("doc_10_re")
#             doc_12_re = request.POST.get("doc_12_re")
#             doc_ug_re = request.POST.get("doc_ug_re")
#             address_re = request.POST.get("address_re")
#             # User = request.user()
#             test2.Name  = name_re
#             test2.Number = number_re
#             test2.Email = email_re
#             test2.Father = father_re
#             test2.Education = education_re
#             test2.Address = address_re
#             test2.save()
#             message =  messages.success(request, 'Changes Applied' )
#             return HttpResponseRedirect('Recheck' , message)
#         else:    
#             # recheck = Student_detail.objects.filter(Email = User)
#             # data = {  'recheck' : recheck }
#         # id = Student_detail.objects.only('id').get(Email=User).id
        
#         # print(recheck)
#         # student  = Student_detail(Name=name, Number=number, 
#         # Email= email, Father= father, Education=education, doc_10=doc_10 , doc_12=doc_12 , doc_ug=doc_ug , Address=address)
#         # student.save()
#             return render(request, 'recheck.html', data )

#         # return render(request, 'recheck.html', data )

#     return render(request, 'recheck.html')

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


@login_required
@user_passes_test(lambda u: u.is_superuser)
def admintm(request):
    User = get_user_model()
    users = User.objects.all()
    no_of_u = User.objects.count()
    no_of_courses = Course.objects.all()
    no_of_courses = no_of_courses.count()

    # print(no_of_u)
    form = query_form.objects.all()
    if request.method == 'POST':
        if request.POST.get('form_name')=="LOGOUT":
            auth.logout(request)
            return redirect('Student:HOME')
        elif request.POST.get('form_name') == "DELETE":
            ID = request.POST.get('id')
            DELETE = query_form.objects.get(pk = ID)
            print(ID)
            # course_del1 = query_form.objects.get(id = DELETE).delete()
            DELETE = query_form.objects.get(pk = ID).delete()
            message = messages.warning(request , 'running')
            print('running')
        # course_del = query_form.objects.get(id = ID).delete()
        # message = messages.warning(request, str( course_del1 )+ " " +  'Deleted' )
    return render(request, 'admintm/index.html', {'no_of_u' : no_of_u , 'no_of_courses' : no_of_courses,'form_query':form })

def data_tables(request):
    form = newuserform(request.POST)
    # if request.POST.get('form_name')=="ADD":
    if request.method=="POST":
        if form.is_valid():
            email = form.cleaned_data['username']
            
            pwd = form.cleaned_data['password1']
            message = "your id and password is : " + " " + email + " " + pwd
            subject = ' Student Admission'
            send_mail(subject,message, EMAIL_HOST_USER, [email], fail_silently = False)
            send_mail(subject,message, EMAIL_HOST_USER, [EMAIL_HOST_USER], fail_silently = False)
            form.save()
    User = get_user_model() 
    users = User.objects.all()
    return render(request, 'admintm/data-tables.html', {'user_list' : users ,'form' : form})



# delete course    
def Delete_course(request, id):
    DELETE = Course.objects.get(pk = id)
     
    if request.method == 'POST':
        ID = request.POST.get('ID')
        print(ID)
        course_del1 = Course.objects.get(id = ID)
        course_del = Course.objects.get(id = ID).delete()
        print(course_del1)
        
        message = messages.warning(request, str( course_del1 )+ " " +  'Deleted' )
        return HttpResponseRedirect('/courses_table' )
    return render(request, 'delete_course.html' , {"DELETE":DELETE}  ) 
def Edit_course(request , id):
    Edit = Course.objects.get(pk = id) 
    item = Course.objects.get(pk = id) 
    
    form = CourseForm(request.POST , instance = item )
    if request.method == "POST":
        name = request.POST.get("Name_edit")
        price = request.POST.get("price_edit")
        Edit.Course_name = name
        Edit.Price = price
        Edit.save()
        # item = Course.objects.get(pk = id)  
        # form = CourseForm(request.POST , instance = item )
        # if form.is_valid():
        #     form.save()
        message = messages.warning(request, 'EDITED' )
        return HttpResponseRedirect('/courses_table')
    else:
        form = CourseForm(request.POST  , instance = item )
        # message = messages.warning(request, 'EDITED' )
        # return HttpResponseRedirect('/courses_table' , message)
    

    context = {
        'form' : form,
        'ID' : item , 
    }    
    print(Edit.Course_name)
   

    return render(request , 'edit_course.html'  , context )

def courses_table(request):
    Course_list = Course.objects.all()
    form = CourseForm(request.POST , request.FILES)
    if request.method == 'POST':
        if request.POST.get('form_name') == 'DELETE':
            ID = request.POST.get('ID')
            print(ID)
            course_del1 = Course.objects.get(id = ID)
            course_del = Course.objects.get(id = ID).delete()
            print(course_del1)
            message = messages.warning(request, str( course_del1 )+ " " +  'Deleted' )
            return HttpResponseRedirect('courses_table' , message )
        
        elif request.POST.get('form_name') == 'ADD':
            form = CourseForm(request.POST , request.FILES)
            if form.is_valid():
                form.save()
                messages.warning(request,'Added')
                return redirect('/courses_table')
    return render(request, 'admintm/courses_table.html', {'courses_list' : Course_list ,'form' : form,'message':messages})


# edit course


# edit course

def user_details(request):
    users_details = Student_detail.objects.all()

    return render(request, 'admintm/user-details.html', {'user_details' : users_details })



# 
def Edit_course2(request , id):
    item = Course.objects.get(pk = id) 
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = CourseForm(request.POST , instance=item)
        if form.is_valid():
            form.save()
            message = messages.warning(request, 'EDITED' )
            return HttpResponseRedirect('/courses_table')
            # pass

    else:
        form = CourseForm(initial = {
        'Course_name': item.Course_name,
        'Price': item.Price,
        'Details' : item.Details
        })  
        # form = CourseForm(request.POST ,  initial=model_to_dict(item))        

    context = {
        'form' : form
    }
    return render(request, 'edit_course2.html' , context)

# admin student
def Student(request):
    # User = get_user_model()
    # users = User.objects.all()
    # no_of_u = User.objects.count()
    # no_of_courses = Course.objects.all()
    # no_of_courses = no_of_courses.count()
    return render(request, 'student.html')


def Add_student(request):
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = Student_detailForm(request.POST,request.FILES )
        

        # print(form)
        if form.is_valid():
            fm = form.cleaned_data['Email']
            # fc = Student_detailForm.Email
            print(fm)
            email = fm
            if Student_detail.objects.filter(Email = email).exists():
                message = messages.warning(request , email + " " + 'is already used')
                return HttpResponseRedirect('add-student' , messages)
            else:    
                fm = form.cleaned_data
                form.save()
                    # fm.save()
                print(fm)

                # user create
                N = 7
                res = ''.join(random.choices(string.ascii_uppercase +
                    string.digits, k = N))

            

                print("The generated random string : " + str(res))


                message = "your id and password is : " + " " + email + " " + res
                subject = ' Student Admission'
            
            # user create 
                User.objects.create_user(email,password=res)

                send_mail(subject, 
                message, EMAIL_HOST_USER, [email], fail_silently = False)
                send_mail(subject, 
                message, EMAIL_HOST_USER, [EMAIL_HOST_USER], fail_silently = False)
            
                # user create

                return HttpResponseRedirect('admin-student')
            # pass

    else:
        # message = messages.warning('Please fill the form')
        #
        form = Student_detailForm(request.POST)        

    context = {
        'form' : form,
        
    }
    return render(request,'student_add.html',context)    
def manage_student(request):
    students = Student_detail.objects.all()

    return render(request , 'manage_student.html' , {'students':students})    
def student_del(request , id):
    DELETE = Student_detail.objects.get(pk = id)
    if request.method == 'POST':
        ID = request.POST.get('ID')
        print(ID)
        student_del1 = Student_detail.objects.get(id = ID)
        email = student_del1.Email
        user = User.objects.get(username = email).id
        user = User.objects.get(username = email).delete()
        # User_id = user
        # user.delete()
        course_del = Student_detail.objects.get(id = ID).delete()
        
        
        message = messages.warning(request, str( student_del1 )+ " " +  'Deleted' )
        return HttpResponseRedirect('/admin-manage_student' )

    return render(request , 'manage_student_del.html',{'DELETE':DELETE} )    

def admin_student_edit(request , id):
    EDIT = Student_detail.objects.get(pk = id)
    if request.method == 'POST':
        form = Student_detail_editForm(request.POST,request.FILES, instance=EDIT  )
        

        # print(form)
        if form.is_valid():
            print('i am working')
            # fm = form.cleaned_data['Email']
            # fc = Student_detailForm.Email
            # print(fm)
            # email = fm
            
            # fm = form.cleaned_data
            form.save()
            # fm.save()
            # print(fm)

        
        message = messages.warning(request,'EDITED' )
        return HttpResponseRedirect('/admin-manage_student' )
    else:
        # message = messages.warning('Please fill the form')
        
        form = Student_detail_editForm( instance=EDIT )  
        print('not working')


    context = {
        'form' : form,
        
    }
    return render(request , 'manage_student_edit.html' , context )    

def admin_new_student(request):
    student = Student_detail.objects.filter(Payment=False)
    context = {
        'student' : student
    }

    return render(request, 'admin_new_student.html' , context)        
def admin_paid_student(request):
    student = Student_detail.objects.filter(Payment=True)
    context = {
        'student' : student
    }

    return render(request, 'admin_paid_student.html' , context)        

def HOME(request):
    images = slider.objects.all()
    courses_details = courses_det.objects.all()
    if request.method =="POST":
        if request.POST.get('query') =="QUERY":
            name = request.POST.get('form_name')
            email = request.POST.get('form_email')
            subject = request.POST.get('form_subject')
            message = request.POST.get('form_message')
            # form = {name,email,subject,message}
            query_form(form_name=name,form_email=email,form_subject=subject,form_message=message).save()
            send_mail(subject, 
            message, EMAIL_HOST_USER, [EMAIL_HOST_USER], fail_silently = False)
            message = "Your message has been sucessfully submited"
            send_mail(subject, 
            message, EMAIL_HOST_USER, [email], fail_silently = False)


    return render(request, 'Home/index.html',{'images': images,'courses':courses_details} )

def logout(request):
        if request.method == 'POST':
            auth.logout(request)
            return redirect('Student:HOME')
def revenue(request):
    return render(request,'admintm/revenue.html')

def totalrevenue(request):
    # id = Student_detail.objects.filter(Student_detail.Course_name)

    pay =  Student_detail.objects.get(Payment=True).id
    pay2 = Student_detail.objects.get(pk=pay)
    course_name = pay2.Course_name
    payment = pay2.Payment

    # print(course_name,payment)
    return render(request,'admintm/totalrevenue.html')