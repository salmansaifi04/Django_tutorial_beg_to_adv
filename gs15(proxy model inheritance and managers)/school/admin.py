from django.contrib import admin
from .models import ExamCenter, MyExamCenter, Student
# Register your models here.


## proxy model inheritance 
@admin.register(ExamCenter)
class ExamCenterAdmin(admin.ModelAdmin):
    list_display = ['id', 'cname', 'city']


@admin.register(MyExamCenter)
class MyExamCenterAdmin(admin.ModelAdmin):
    list_display = ['id', 'cname', 'city']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll']

# salman
# salman@123