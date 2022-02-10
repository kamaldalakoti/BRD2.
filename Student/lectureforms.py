from django.db import models
from django import forms
# from django.forms.extras.widgets import Select, SelectDateWidget
from django.conf import Settings, settings
from django.forms import ModelForm, Select, Textarea, TextInput, NumberInput
# from django.forms.extras.widgets import Select, SelectDateWidget
from .lecturemodels import FileUpload


from .lecturemodels import Lecture

# class SettingForm(forms.Form):
#     class Meta:
#         model = Settings

    # def clean_computer(self):
    #     computer = self.cleaned_data.get('computer')
    #     if not self.instance.scenario.demo.computers.filter(computer=computer).count():
    #         raise forms.ValidationError("Computer not in demo")
    #     return computer

# class SettingInline(admin.TabularInline):
#     model = Settings
#     form = SettingForm



class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = [ 'lecture_num', 'week_num', 'title', 'course', 'description', 'youtube_url', 'vimeo_url', 'preferred_service']
        # fields = '__all__'
        labels = {
            'lecture_num': 'Lecture Number',
            'week_num': 'Week Number',
            'youtube_url': 'YouTube URL',
            'vimeo_url': 'Vimeo URL',
        }
        widgets = {
            'lecture_num': NumberInput(attrs={'class': ' border border-dark form-control','placeholder': 'Enter Lecture Number'}),
            'week_num': NumberInput(attrs={'class': ' text-center border border-dark form-control','placeholder': 'Enter Week Number'}),
            'title': TextInput(attrs={'class': ' text-center border border-dark form-control','placeholder': 'Enter Title'}),
            'description': Textarea(attrs={'class': ' text-center border border-dark form-control','placeholder': 'Enter Description'}),
            'youtube_url': TextInput(attrs={'class': ' text-center border border-dark form-control','placeholder': 'Enter YouTube URL'}),
            'vimeo_url': TextInput(attrs={'class': ' text-center border border-dark form-control','placeholder': 'Enter Vimeo URL'}),
            'preferred_service': Select(attrs={'class': ' text-center border border-dark form-control'}),
            # 'course': Select(attrs={'class': 'text-center border border-dark form-control'}),
        }

    def clean(self):
        youtube_url = self.cleaned_data['youtube_url']
        if youtube_url is not '':
            if "https://www.youtube.com/embed/" not in youtube_url:
                raise forms.ValidationError("YouTube URL needs to be a embedded URL.")


class NoteUploadForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ['upload_id', 'title', 'description', 'file']
        labels = {
            'file': 'PDF',
        }
        widgets = {
            'title': TextInput(attrs={'class': u'form-control','placeholder': u'Enter Title'}),
            'description': Textarea(attrs={'class': u'form-control','placeholder': u'Enter Description'}),
        }

    # Function will apply validation on the 'file' upload column in the table.
    def clean_file(self):
        upload = self.cleaned_data['file']
        content_type = upload.content_type
        if content_type in ['application/pdf']:
            if upload._size <= 20971520:
                return upload
            else:
                raise forms.ValidationError("Cannot exceed 20MB size")
        else:
            raise forms.ValidationError("Only accepting PDF files for course notes.")
