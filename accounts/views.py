
# Create your views here.

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib import messages
from Student.models import Student_detail


def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username = request.POST['username'])
                return render (request,'accounts/signup.html', {'error':'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('/')
        else:
            return render (request,'accounts/signup.html', {'error':'Password does not match!'})
    else:
        return render(request,'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        # USERS = User.objects.filter(user , is_superuser=True).exists()
        if user is not None:
            auth.login(request,user)
            print(User.objects.all())
            # if not user.is_superuser and not user.is_staff:
            if request.user.is_superuser:
            # if user is user.is_superuser:
                return redirect('Student:Admin-Dashboard')
                # return redirect('/Recheck')
            elif request.user.is_staff:
                auth.login(request,user)
                return redirect('/Dashboard')
            else:
                # if Student_detail.objects.filter(Payment=True).exists():
                auth.login(request,user)
                return redirect('student_dashboard:student_dashboard')
                # else:
                #     return redirect('/Recheck')

        # if user.is_superuser is not None:
            
        #     print('super working' )
        else:

           
            message = messages.warning(request , 'Username or password is incorrect!')
            # return render (request,'accounts/login.html', {'error':'Username or password is incorrect!'})
            return render (request,'accounts/login.html', message)
    else:
        return render(request,'accounts/login.html')

def logout(request):
        if request.method == 'POST':
            auth.logout(request)
            return redirect('Student:HOME')
        else:
            return render(request, 'accounts/logout.html') 

