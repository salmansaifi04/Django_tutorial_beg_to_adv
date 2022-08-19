from django.db import models

# Create your models here.
## ------- Abstract Base Class Model Inhertiance Start ------ ##
class CommonInfo(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    date = models.DateField()
    class Meta:
        abstract = True

class Student(CommonInfo):
    fees = models.IntegerField()
    date = None

class Teacher(CommonInfo):
    salary = models.IntegerField()

class Contractor(CommonInfo):
    date = models.DateTimeField()
    payment = models.IntegerField()
## ----- Abstract Base Class Model Inhertiance End ------ ##


## ------ Multilabel Inhertance Start ------ ##
class ExamCenter(models.Model):
    cname = models.CharField(max_length=70) #centername
    city = models.CharField(max_length=70) 

class MyExamCenter(ExamCenter):
    name = models.CharField(max_length=70) 
    roll = models.IntegerField() 
    
## ------ Multilabel Inhertance End ------ ##
