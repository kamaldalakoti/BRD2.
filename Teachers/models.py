from django.db import models
from Student.models import Course
from ckeditor.fields import RichTextField


# Create your models here.
class study_material(models.Model):
    Name_i = models.CharField(max_length=30,  null=True)
    Details = RichTextField(blank=True , null=True)
    
    Course_name = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    FileName = models.FileField(upload_to='static', max_length = 100)
    
    

    def __str__(self):
        return self.Name_i

    # def __unicode__(self):
    #     return 
    
