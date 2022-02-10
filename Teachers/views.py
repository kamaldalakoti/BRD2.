from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.
@login_required
@staff_member_required
def Dashboard(request):
    return render(request , 'Teachers/teachers_dashboard.html')


@login_required
@staff_member_required
def TEST(request):
    return HttpResponse('I am TEST')