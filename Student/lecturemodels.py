from pyexpat import model
from turtle import TurtleGraphicsError
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Course
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

import os


class FileUpload(models.Model):
    upload_id = models.AutoField(primary_key=True)
    type = models.PositiveSmallIntegerField(default=settings.UNKNOWN_FILE_UPLOAD_TYPE)
    title = models.CharField(max_length=127, null=True)
    description = RichTextField(null=True)
    upload_date = models.DateField(auto_now= True, null=True)
    file = models.FileField(upload_to='uploads', null=True)
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def delete(self, *args, **kwargs):
        """
            Overrided delete functionality to include deleting the local file
            that we have stored on the system. Currently the deletion funciton
            is missing this functionality as it's our responsibility to handle
            the local files.
        """
        if self.file:
            if os.path.isfile(self.file.path):
                os.remove(self.file.path)
        super(FileUpload, self).delete(*args, **kwargs) # Call the "real" delete() method
    
    def __str__(self):
        return self.title


class Lecture(models.Model):
    lecture_num = models.PositiveSmallIntegerField(null=True,
        # validators=[MinValueValidator(1)],
        # default=1
    )
    week_num = models.PositiveSmallIntegerField(null=True,
        # validators=[MinValueValidator(1)],
        # default=1
    )
    title = models.CharField(max_length=63, default='', null=True)
    description = RichTextField(default='', null=True)
    youtube_url = models.URLField(null=True, blank=True)
    vimeo_url = models.URLField(null=True, blank=True)
    bliptv_url = models.URLField(null=True, blank=True)
    VIDEO_PLAYER_CHOICES = (
        (settings.YOUTUBE_VIDEO_PLAYER, 'YouTube'),
        (settings.VIMEO_VIDEO_PLAYER, 'Vimeo')
    )
    preferred_service = models.CharField(
        max_length=1,
        choices=VIDEO_PLAYER_CHOICES,
        default=settings.YOUTUBE_VIDEO_PLAYER
    )
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    # notes = models.ManyToManyField(FileUpload)
    # class Notes(models.Model):
    #     upload_id = models.AutoField(primary_key=True)
    #     # type = models.PositiveSmallIntegerField(default=settings.UNKNOWN_FILE_UPLOAD_TYPE)
    #     title = models.CharField(max_length=127, null=True)
    #     description = RichTextField(null=True)
    #     upload_date = models.DateField(auto_now= True, null=True)
    #     file = models.FileField(upload_to='uploads', null=True)

        
    
        # def __str__(self):
        #     return 
    
        # def __unicode__(self):
        #     return 
    

    def delete(self, *args, **kwargs):
        for note in self.notes.all():
            note.delete()
        super(Lecture, self).delete(*args, **kwargs) # Call the "real" delete() method

    def __str__(self):
        return 'Week: ' + str(self.week_num) + ' Lecture: ' + str(self.lecture_num) + ' Title: ' +self.title;
