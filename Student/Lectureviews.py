from email import message
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template import context

from Student.models import Course
from .lecturemodels import Lecture
from Student.lectureforms import LectureForm
from django.contrib import messages

from Student import lecturemodels





def Lectures(request):
    form = LectureForm()
    if request.method == 'POST':
       
        course = request.POST['course']
        # course_id = request.POST['course_id']
        lecture_num = request.POST['lecture_num']
        week_num = request.POST['week_num']
        title = request.POST['title']
        description = request.POST['description' ]
        youtube_url = request.POST[ 'youtube_url' ]
        vimeo_url = request.POST[ 'vimeo_url' ]
        preferred_service = request.POST[ 'preferred_service' ]
        # notes = request.POST[ 'notes' ]
        course = Course.objects.get(id = course)
        if Lecture.objects.filter(lecture_num = lecture_num ).exists():
            message =  messages.success(request, 'filter' )
            return redirect('Student:Lecture')
            # return HttpResponse('change')

        else:    
            Lecture.objects.create( lecture_num = lecture_num, week_num = week_num, title = title, description = description, youtube_url = youtube_url, vimeo_url = vimeo_url, preferred_service = preferred_service , course = course).save()
            # 'lecture_id', 'lecture_num', 'week_num', 'title', 'description', 'youtube_url', 'vimeo_url', 'preferred_service'
            print(course , lecture_num ,week_num ,title , youtube_url ,vimeo_url ,description,preferred_service )
            return redirect('Lecture-home')
    return render(request, 'Lecture/lecture.html',{
        'form' : form,
    } )
def Lecture_edit(request , id ):

    item = Lecture.objects.get(id = id)
    form = LectureForm(instance=item)
    if request.method == 'POST':
        course = request.POST['course']
        # course_id = request.POST['course_id']
        lecture_num = request.POST['lecture_num']
        # lecture_id = request.POST['lecture_id']
        week_num = request.POST['week_num']
        title = request.POST['title']
        description = request.POST['description']
        youtube_url = request.POST['youtube_url']
        vimeo_url = request.POST[ 'vimeo_url' ]
        preferred_service = request.POST['preferred_service']
        # notes = request.POST[ 'notes' ]
        course = Course.objects.get(id = course)
        update = Lecture.objects.get(pk = id)
        update.lecture_num = lecture_num
        update.title = title
        update.week_num = week_num
        update.description = description
        update.youtube_url = youtube_url
        update.vimeo_url = vimeo_url
        update.preferred_service = preferred_service
        update.course = course
        update.save()

        return redirect('Student:Manage-Lecture')
    else:
        form = LectureForm(instance=item)



    context = {
        'form' : form
    }

    return render(request , 'Lecture/lecture_edit.html' , context  )


def Lecture_manage(request):
    form = LectureForm()
    lecture = Lecture.objects.all()
    context = {
        'Lecture' : lecture ,
         'form' : form
    }
    # if request.method == ' POST':
    #     pass
    #     form = LectureForm()
    # else:
    #     form = LectureForm(instance=)
    #     pass

    return render(request , 'Lecture/lecture_manage.html' , context  )

def Lecture_home(request):
    LectureCount = Lecture.objects.all().count()
    context = {

        'LectureCount':LectureCount
    }
    return render(request,'Lecture/lectureIndex.html' , context)
