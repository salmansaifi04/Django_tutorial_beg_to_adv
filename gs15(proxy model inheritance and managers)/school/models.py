from django.db import models
from .managers import CustomManager, Custom1Manager

# Create your models here.
class ExamCenter(models.Model):
    cname = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    ## model manager name
    # objects = models.Manager()  
    Exam = models.Manager()  

class MyExamCenter(ExamCenter):
    stud = Custom1Manager()
    class Meta:
        proxy = True
        ordering = ['city']

## custom manager 
class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()
    objects = models.Manager()
    students = CustomManager()