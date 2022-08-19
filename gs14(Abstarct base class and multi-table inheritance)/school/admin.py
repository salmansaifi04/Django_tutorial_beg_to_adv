from django.contrib import admin
from .models import Contractor, Teacher, Student, ExamCenter, MyExamCenter


## Abstract Base class Start 
@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'date', 'payment']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'fees']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'date', 'salary']
## Abstract Base class End


## Multi-table inheritance Start
@admin.register(ExamCenter)
class ExamCenterAdmin(admin.ModelAdmin):
    list_display = ['id', 'cname', 'city']

@admin.register(MyExamCenter)
class MyExamCenterAdmin(admin.ModelAdmin):
    list_display = ['id', 'cname', 'city', 'name', 'roll']
## Multi-table inheritance End



# salman
# salman@123